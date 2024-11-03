### Question Answering using LLM
from langchain_ollama import ChatOllama

from langchain_core.prompts import (SystemMessagePromptTemplate, 
                                    HumanMessagePromptTemplate,
                                    ChatPromptTemplate)



from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

base_url = "http://localhost:11434"
# model = 'llama3.2:3b'
model = 'qwen2.5:7b'
llm = ChatOllama(base_url=base_url, model=model)


system = SystemMessagePromptTemplate.from_template("""You are helpful AI assistant who answer user question based on the provided context.""")

prompt = """
            **Task:** Extract key information from the following resume text.

            **Resume Text:**
            {context}

            **Instructions:**
            Please extract the following information and format it in a clear structure:

            1. **Contact Information:**
            - Name:
            - Email:
            - Phone Number:
            - Website/Portfolio:

            2. **Education:**
            - Institution Name:
            - Degree:
            - Field of Study:
            - Graduation Dates:

            3. **Experience:**
            - Job Title:
            - Company Name:
            - Location:
            - Dates of Employment:
            - Responsibilities/Projects:

            4. **Projects:**
            - Project Title:
            - Description/Technologies Used:
            - Outcomes/Results:

            5. **Skills:**
            - Programming Languages:
            - Technologies/Tools:

            6. **Additional Information:** (if applicable)
            - Certifications:
            - Awards or Honors:
            - Professional Affiliations:
            - Languages:

            **Question:**
            {question}

            **Extracted Information:**
        """

prompt = HumanMessagePromptTemplate.from_template(prompt)

messages = [system, prompt]
template = ChatPromptTemplate(messages)

# qna_chain = template | llm | StrOutputParser()
qna_chain = template | llm | JsonOutputParser()

def ask_llm(context, question):
    return qna_chain.invoke({'context': context, 'question': question})