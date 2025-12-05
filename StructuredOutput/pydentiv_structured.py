from langchain_google_genai import ChatGoogleGenerativeAI  # type: ignore
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
import os
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"))
#schema definition
class ReviewModel(BaseModel):
    key_themes: list[str] = Field(description="Must write down List of key themes mentioned in the review")
    summary: str = Field(description="Must write down a brief summary of the review")
    sentiment: Literal["Positive", "Negative"] = Field(description="Must write down the overall sentiment of the review, either Positive, Negative")
    name: Optional[str] = Field(description="Write down the name of the reviewer")

structured_model = model.with_structured_output(ReviewModel)
prompt = """
The Google Pixel 7 Pro is Google's flagship smartphone offering a premium blend of hardware and AI-driven software experiences. Its defining feature is a top-tier camera system, comprising a 50MP main lens, a 12MP ultrawide lens, and a 48MP telephoto lens with 5x optical zoom. These cameras leverage Google's computational photography and AI tools, powered by the custom Google Tensor G2 chip, to enable unique post-processing effects like Magic Eraser and Photo Unblur. The device sports a large, immersive 6.7-inch QHD+ 120Hz LTPO OLED display, offering smooth visuals in a sleek aluminum frame with an IP68 water resistance rating. Running a clean, stock Android interface, the Pixel 7 Pro prioritizes a seamless user experience with features like Live Translate and Call Screening. It is powered by a reliable 5,000mAh battery offering multi-day longevity with the Extreme Battery Saver mode. While praised universally for its exceptional photography prowess and clean software, potential drawbacks include slower charging speeds compared to some competitors and performance benchmarks that lag slightly behind the absolute fastest chips on the market.

reviewed by Kawser!
"""

result = structured_model.invoke(prompt)
print("Structured Output:", result)