from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful Customer Support Agent.'),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human', '{query}'),
])

chat_history = []
with open("chat_history.txt") as file:
    chat_history.extend(file.readlines())

print("Chat History from file:", chat_history)

prompt = chat_template.invoke({
    'chat_history': chat_history,
    'query': "Where is my refund?"
})

print(prompt.messages)