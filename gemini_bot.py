import os
import google.generativeai as genai
from google.generativeai.types import Tool
from dotenv import load_dotenv # Import load_dotenv

from time_tool import TimeTool

load_dotenv() # Load environment variables from .env file

class GeminiBot:
    """Wraps Gemini chat with support for multiple function tools."""

    def __init__(self, api_key: str, model_name: str = "gemini-2.5-pro-exp-03-25"):
        genai.configure(api_key=api_key)
        # register all function declarations in one Tool
        tool = Tool(function_declarations=[
            TimeTool.GET_CURRENT_TIME,
            TimeTool.GET_FUTURE_TIME
        ])
        self.model = genai.GenerativeModel(
            model_name=model_name,
            tools=[tool]
        )
        # map names to callables
        self.functions = {
            "get_current_time": TimeTool.get_current_time,
            "get_future_time": TimeTool.get_future_time
        }

    def start_chat(self, auto_func=False):
        self.chat = self.model.start_chat(enable_automatic_function_calling=auto_func)

    def ask(self, prompt: str):
        resp = self.chat.send_message(prompt)
        part = resp.candidates[0].content.parts[0]

        if part.function_call:
            name = part.function_call.name
            args = part.function_call.args or {}
            result = self.functions[name](**args)
            # send function result back
            resp = self.chat.send_message({
                "function_response": {"name": name, "response": {"result": result}}
            })
            part = resp.candidates[0].content.parts[0]

        return part.text

if __name__ == "__main__":
    api_key = os.getenv("GOOGLE_API_KEY") # Get key from environment
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in .env file or environment variables.")

    bot = GeminiBot(api_key=api_key) # Use the loaded key
    bot.start_chat()

    print("Chat started. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = bot.ask(user_input)
        print(f"Bot: {response}")