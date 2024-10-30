from langchain_ollama import ChatOllama

from langchain_core.prompts import (SystemMessagePromptTemplate, HumanMessagePromptTemplate,
                                    ChatPromptTemplate)



from langchain_core.output_parsers import StrOutputParser

base_url = "http://localhost:11434"
model = 'llama3.2:3b'

llm = ChatOllama(base_url=base_url, model=model)

system = SystemMessagePromptTemplate.from_template("""You are helpful AI assistant who answer user question based on the provided context.""")

# Below context is the text data extracted from the website. You need to think carefully while selecting relevant text.

prompt = """Answer user question based on the provided context ONLY! If you do not know the answer, just say "I don't know".
            ### Context:
            {context}

            ### Question:
            {question}

            ### Answer:"""

prompt = HumanMessagePromptTemplate.from_template(prompt)

messages = [system, prompt]
template = ChatPromptTemplate(messages)

qna_chain = template | llm | StrOutputParser()

def ask_llama(context, question):
    response = qna_chain.invoke({'context': context, 'question': question})
    return response