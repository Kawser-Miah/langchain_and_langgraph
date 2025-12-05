# from langchain_google_genai import ChatGoogleGenerativeAI  # type: ignore
# from dotenv import load_dotenv
# from typing import TypedDict
# import os

# load_dotenv()
# try:
#     api_key = os.getenv("GOOGLE_API_KEY")
#     if not api_key:
#         print("Error: GOOGLE_API_KEY not found in .env file")
#     else:
#         model = ChatGoogleGenerativeAI(
#             model="gemini-2.5-flash",
#             google_api_key=api_key
#         )

#         #schema definition
#         class Review(TypedDict):
#             summary: str
#             sentiment: str
            
#         structured_model = model.with_structured_output(Review)
#         prompt = """
#         The hardware was great, but the software feels kind of bloated. So many boilerplate apps.and my phone keeps hanging when i play PUBG.
#         """

#         result = structured_model.invoke(prompt)
#         print("Structured Output:", result)

#         new_prompt = f"generate sentiment and summary for this review given. The review is  '{prompt}'"
#         new_result = model.invoke(new_prompt)
#         print("Unstructured Output:", new_result.content)
        
# except Exception as e:
#     print(f"Error: {e}")



from langchain_google_genai import ChatGoogleGenerativeAI  # type: ignore
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional
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

        #schema definition
        class Review(TypedDict):
            key_themes: Annotated[list[str], "Must write down List of key themes mentioned in the review"]
            summary: Annotated[str, "Must write down a brief summary of the review"]
            sentiment: Annotated[str, "Must write down the overall sentiment of the review, either Positive, Negative"]
            pros: Annotated[Optional[list[str]], "Must write down List of pros mentioned in the review"]
            cons: Annotated[Optional[list[str]], "Must write down List of cons mentioned in the review minimum 5 cons"]
            
        structured_model = model.with_structured_output(Review)
        prompt = """
The Google Pixel 7 Pro is Google's flagship smartphone offering a premium blend of hardware and AI-driven software experiences. Its defining feature is a top-tier camera system, comprising a 50MP main lens, a 12MP ultrawide lens, and a 48MP telephoto lens with 5x optical zoom. These cameras leverage Google's computational photography and AI tools, powered by the custom Google Tensor G2 chip, to enable unique post-processing effects like Magic Eraser and Photo Unblur. The device sports a large, immersive 6.7-inch QHD+ 120Hz LTPO OLED display, offering smooth visuals in a sleek aluminum frame with an IP68 water resistance rating. Running a clean, stock Android interface, the Pixel 7 Pro prioritizes a seamless user experience with features like Live Translate and Call Screening. It is powered by a reliable 5,000mAh battery offering multi-day longevity with the Extreme Battery Saver mode. While praised universally for its exceptional photography prowess and clean software, potential drawbacks include slower charging speeds compared to some competitors and performance benchmarks that lag slightly behind the absolute fastest chips on the market.        """

        result = structured_model.invoke(prompt)
        print("Structured Output:", result)

        # new_prompt = f"generate sentiment and summary for this review given. The review is  '{prompt}'"
        # new_result = model.invoke(new_prompt)
        # print("Unstructured Output:", new_result.content)
        
except Exception as e:
    print(f"Error: {e}")