import streamlit as st

from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import (
                                        SystemMessagePromptTemplate,
                                        HumanMessagePromptTemplate,
                                        ChatPromptTemplate,
                                        MessagesPlaceholder
                                        )

from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

user_id = 1
def get_session_history(session_id):
    return SQLChatMessageHistory(session_id, "sqlite:///memory.db")

st.title("Your Own Private Chatbot")
st.write("Chat with me! Catch me at https://youtube.com/kgptalkie")

if st.button("Start New Conversation"):
    st.session_state.chat_history = []
    history = get_session_history(user_id)
    # st.write(history.get_messages())
    history.clear()

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat_history from history on app rerun
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


### LLM Setup
llm = ChatOllama(model="llama3.2:1b", base_url="http://localhost:11434/")

system = SystemMessagePromptTemplate.from_template("You are helpful assistant.")
human = HumanMessagePromptTemplate.from_template("{input}")

messages = [system, MessagesPlaceholder(variable_name='histroy'), human]
prompt = ChatPromptTemplate(messages=messages)

chain = prompt | llm  | StrOutputParser()

runnable_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key='input',
    history_messages_key='histroy'
)

def chat_with_llm(session_id, input):
    for s in runnable_with_history.stream(
                                    {"input": input},
                                    config={"configurable": {"session_id": session_id}}):
        yield s


# Accept user input
prompt = st.chat_input("What is up?")
if prompt:
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(chat_with_llm(user_id, prompt))

    # Add assistant response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": response})



