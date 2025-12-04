from langchain_google_genai import ChatGoogleGenerativeAI # type: ignore
from dotenv import load_dotenv
from pathlib import Path
import os

# Load .env from the project root
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not found in .env file")
    else:
        model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=api_key
        )
        prompt = "Explain the theory of relativity in simple terms."
        response = model.invoke(prompt)
        print(response.content)
        print("Gemini model response generated successfully.")
except Exception as e:
    print(f"Error: {e}")