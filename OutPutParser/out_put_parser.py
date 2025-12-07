from langchain_google_genai import ChatGoogleGenerativeAI  # type: ignore
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser

load_dotenv() 
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"))

#first prompt
prompt_template_1 = PromptTemplate(
    input_variables=["topic"],
    template="Write a detailed report on {topic}"
)

# prompt1 = prompt_template_1.invoke({"topic": "The impact of climate change on global agriculture"})
# print("Prompt 1:", prompt1)

# response1 = model.invoke(prompt1).content
# print("Response 1:", response1)

prompt_template_2 = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text(At least 4 points): {text}"
)


# prompt2 = prompt_template_2.invoke({"text": str(response1)})
# print("Prompt 2:", prompt2)

# response2 = model.invoke(prompt2).content
# print("Response 2:", response2)

# Define the output parser schema
parser = StrOutputParser()
#chain

chain = prompt_template_1 | model | parser | prompt_template_2 | model | parser

final_output = chain.invoke({"topic": "The impact of climate change on global agriculture"})
print("Final Structured Output:", final_output)