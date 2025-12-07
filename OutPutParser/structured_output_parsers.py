from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import os

load_dotenv()

# Create parser
parser = JsonOutputParser()

# Create model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"))

# Create prompt template
template = PromptTemplate(
    input_variables=["topic"],
    template="""Provide three interesting facts about {topic}.
    
Return your response as JSON with this exact structure:
{{
    "fact1": "first fact here",
    "fact2": "second fact here",
    "fact3": "third fact here"
}}

{format_instructions}""",
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# Create chain
chain = template | model | parser

# Invoke
final_output = chain.invoke({"topic": "black hole"})
print("Final Structured Output:", final_output)