from dotenv import load_dotenv
from openai import OpenAI
import json
import os
import csv
from datetime import datetime
import requests
from pypdf import PdfReader
import gradio as gr

load_dotenv(override=True)

# --- Tool Definitions ---
def push(text):
    """Sends a notification to your phone via Pushover."""
    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": os.getenv("PUSHOVER_TOKEN"),
            "user": os.getenv("PUSHOVER_USER"),
            "message": text,
        }
    )

def record_user_details(email, name="Name not provided", notes="not provided"):
    """Records recruiter/user contact info and notifies you immediately."""
    push(f"🎯 LEAD: {name} ({email}) - {notes}")
    return {"status": "User details recorded successfully"}

def record_unknown_question(question):
    """Logs questions the agent couldn't answer so you can improve the Knowledge Base."""
    # Send mobile notification
    push(f"❓ UNKNOWN QUESTION: {question}")
    
    # Log to CSV file
    csv_file = "unknown_questions.csv"
    file_exists = os.path.exists(csv_file)
    
    with open(csv_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "question"])
        writer.writerow([datetime.now().isoformat(), question])
    
    return {"status": "Question logged for review"}

tools = [
    {
        "type": "function",
        "function": {
            "name": "record_user_details",
            "description": "Use this tool to record that a user is interested in being in touch. ALWAYS ask for their email if the conversation is going well.",
            "parameters": {
                "type": "object",
                "properties": {
                    "email": {"type": "string", "description": "The email address of the user"},
                    "name": {"type": "string", "description": "The user's name"},
                    "notes": {"type": "string", "description": "Context about why they want to connect"}
                },
                "required": ["email"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "record_unknown_question",
            "description": "Use this tool if the user asks a specific factual question about Reid that is NOT in your context. Do not make up facts.",
            "parameters": {
                "type": "object",
                "properties": {
                    "question": {"type": "string", "description": "The question you could not answer"}
                },
                "required": ["question"]
            }
        }
    }
]

class Me:
    def __init__(self):
        # Using Gemini-2.5-pro via Google's OpenAI-compatible API
        self.client = OpenAI(
            api_key=os.getenv("GEMINI_API_KEY"),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
        self.name = "Reid Caulder"
        
        # Load LinkedIn (Resume Data)
        reader = PdfReader("me/linkedin.pdf")
        self.linkedin = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                self.linkedin += text
        
        # Load Knowledge Base (Philosophy & Projects)
        try:
            with open("me/Knowledge Base.md", "r", encoding="utf-8") as f:
                self.knowledge_base = f.read()
        except FileNotFoundError:
            self.knowledge_base = "Knowledge base file not found."

    def system_prompt(self):
        return f"""You are acting as {self.name}'s AI "Digital Twin." 
You are answering questions on {self.name}'s portfolio website to potential employers, collaborators, and recruiters.

**YOUR GOAL:**
Represent {self.name} professionally, highlighting his unique dual-major background (Finance + Accounting) and his technical skills (Python, Agentic AI, Data Viz).
Be engaging. If the user seems interested, try to get their email address using the `record_user_details` tool.

**CONTEXT SOURCES:**
1. **Knowledge Base (Philosophy & Deep Dives):** Use this for questions about his investment philosophy, specific projects (like the Equity Analyst Agent), and technical approach.
2. **LinkedIn Profile:** Use this for dates, specific job titles, and education history.

**DATA:**
--- BEGIN KNOWLEDGE BASE ---
{self.knowledge_base}
--- END KNOWLEDGE BASE ---

--- BEGIN LINKEDIN PROFILE ---
{self.linkedin}
--- END LINKEDIN PROFILE ---

If a question is not answered by this context, admit you don't know and use `record_unknown_question`.
"""

    def handle_tool_call(self, tool_calls):
        results = []
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            
            tool_func = globals().get(function_name)
            if tool_func:
                result = tool_func(**arguments)
                results.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result)
                })
        return results

    def chat(self, message, history):
        messages = [{"role": "system", "content": self.system_prompt()}]
        # Gradio with type="messages" passes history as list of dicts
        for msg in history:
            messages.append({"role": msg["role"], "content": msg["content"]})
        messages.append({"role": "user", "content": message})

        # API Call using Gemini-2.5-pro
        response = self.client.chat.completions.create(
            model="gemini-2.5-pro",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )
        
        msg = response.choices[0].message
        
        if msg.tool_calls:
            messages.append(msg)
            tool_results = self.handle_tool_call(msg.tool_calls)
            messages.extend(tool_results)
            
            stream = self.client.chat.completions.create(
                model="gemini-2.5-pro",
                messages=messages,
                stream=True
            )
            partial_message = ""
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    partial_message += chunk.choices[0].delta.content
                    yield partial_message
        else:
            yield msg.content

if __name__ == "__main__":
    me = Me()
    
    # Updated Examples per your request
    examples = [
        "Tell me about the Agentic AI projects you're working on.",
        "What are your technical skills?",
        "What is your investment philosophy?",
        "Tell me about your time as an Audit Intern."
    ]
    
    chat_interface = gr.ChatInterface(
        fn=me.chat,
        type="messages",
        title="Reid Caulder's Digital Twin",
        description="Ask me anything about Reid's projects, background, or the technical architecture of this agent!",
        examples=examples,
    )
    
    chat_interface.launch()
    