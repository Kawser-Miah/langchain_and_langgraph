from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI # type: ignore 
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

chat_template = ChatPromptTemplate(
    [
        ('system', 'You are a helpful {domain} expert.'),
        ('human', 'Explain {topic} in simple terms.'),
    ]
)

prompt= chat_template.invoke(
    {
        'domain': 'science',
        'topic': 'the theory of relativity'
    }
)

print(prompt.messages)