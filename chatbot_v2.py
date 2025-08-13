from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Check if API key is set
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    print("Error: OPENAI_API_KEY not found in environment variables.")
    print("Please create a .env file with your OpenAI API key:")
    print("OPENAI_API_KEY=your_api_key_here")
    print("Get your API key from: https://platform.openai.com/account/api-keys")
    exit(1)

client = OpenAI(api_key=api_key)

def get_response(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print(get_response("Hello, how are you?"), flush=True)
