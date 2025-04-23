# Gemini Function Calling Chatbot

This project demonstrates a simple Python chatbot using the Google Gemini API with function calling capabilities. The bot can interact in a conversation and also call predefined functions to get the current time or a future time in a specific timezone (Asia/Jakarta).

## Features

*   **Conversational AI:** Leverages the Gemini model for natural language interaction.
*   **Function Calling:** Demonstrates how to integrate custom functions (tools) with the Gemini API.
    *   `get_current_time`: Fetches the current time in Asia/Jakarta. 
    *   `get_future_time`: Calculates the time N hours from now in Asia/Jakarta.
*   **Interactive Chat:** Allows users to chat with the bot via the command line.
*   **Timezone Aware:** Uses `pytz` for accurate timezone handling.

## Setup

1.  **Clone the repository (if applicable) or download the script.**
2.  **Install dependencies:**
    ```bash
    pip install google-generativeai pytz
    ```
3.  **Get a Google API Key:**
    *   Obtain an API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
4.  **Configure API Key:**
    *   Open the `gmenini_bot.py` script.
    *   Replace `'YOUR_API_KEY'` in the `if __name__ == "__main__":` block with your actual Google API key:
        ```python
        # Replace with your key
        bot = GeminiBot(api_key='YOUR_API_KEY')
        ```
    *   Alternatively, you can set the `GOOGLE_API_KEY` environment variable and uncomment the corresponding line in the script.

## Usage

Run the script from your terminal:

```bash
python gmenini_bot.py