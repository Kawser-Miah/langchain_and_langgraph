from langchain_google_genai import ChatGoogleGenerativeAI # type: ignore
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv

import os
load_dotenv()

try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not found in .env file")
    else:
        model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=api_key
        )
        chat_history = [
            SystemMessage(content="You are a helpful assistant."),
        ]
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting chat.")
                break
            chat_history.append(HumanMessage(content=user_input))
            response = model.invoke(chat_history)
            chat_history.append(AIMessage(content=response.content))
            print(f"AI: {response.content}")
        print("Chat History:", chat_history)
except Exception as e:
    print(f"Error: {e}")