from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Create a ReAct-style prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful AI assistant that can use tools to answer user queries.
When you use tools, think step-by-step:
1. What tool would help answer this?
2. What input should I give the tool?
3. How do I use the tool's output to help the user?

Tools available: {tools}"""),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

print(prompt)