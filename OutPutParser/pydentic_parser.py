from langchain_google_genai import ChatGoogleGenerativeAI  # type: ignore
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
import os
from pydantic import BaseModel, Field

load_dotenv()
# Define Pydantic model
class Persion(BaseModel):
    name: str = Field(description="The person's full name.")
    age: int = Field(gt=18, lt=100, description="The person's age must be greater than 18.")
    city: str = Field(description="The city where the person lives.")
# Create parser
parser = PydanticOutputParser(pydantic_object=Persion)    
# Create model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"))
# Create prompt template
template = PromptTemplate(      
    template="""Give me the name, age, and city of a fictional {place} persion.
    Make sure the age is between 18 and 100.
    Return your response in following formet:{response_format}
    """,
    input_variables=["place"],
    partial_variables={"response_format": parser.get_format_instructions()}
)
# Create chain
chain = template | model | parser
# Invoke
final_output = chain.invoke({"place": "New York"})
print("Final Structured Output:", final_output)     
