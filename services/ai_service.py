# import openai  # Assuming you're using OpenAI API; replace with your model 
from enum import Enum
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List

# Define an Enum for contexts
class ContextEnum(str, Enum):
    CAPITAL_MANAGEMENT = "CAPITAL_MANAGEMENT"
    INVESTMENT = "INVESTMENT"
    SAVE_MONEY = "SAVE_MONEY"
    BILLS_BALANCE = "BILLS_BALANCE"
    SUMMARY_INVOICES = "SUMMARY_INVOICES"

# Request model for input
class InputRequest(BaseModel):
    context: ContextEnum
    input: str
    userId: int


USER_PROMPT = """
Answer the user question based on the above provided history and below context

CONTEXT:
{context}

USER_QUESTION:
{query}
"""



llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)


def process_with_llm(user_request: InputRequest, history: List[List[str]]) -> str:
    try:
        conversation_list = []

        for human_message, ai_message in history:
            conversation_list.append(("human", human_message))
            conversation_list.append(("ai", ai_message))

        chat_template = ChatPromptTemplate([
            ("system", "You are a helpful Bank Assistant. Answer in short responses."),
            ("placeholder", "{conversation}"),
            ("human", f"{USER_PROMPT}"),
        ])


        messages = chat_template.invoke({
                        "conversation": conversation_list,
                        "context":user_request.context.value,
                        "query":user_request.input
                    })

        response = llm.invoke(messages)
        
        return response.content
    except Exception as e:
        print(f"Error during LLM processing: {e}")
        return "Error in processing"



# Depricated
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def process_with_llm(text: str) -> str:
#     # Placeholder for actual model call
#     try:
#         # Example API call to OpenAI GPT-3 (replace with your model if different)
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=text,
#             max_tokens=100
#         )
#         return response.choices[0].text.strip()
#     except Exception as e:
#         print(f"Error during LLM processing: {e}")
#         return "Error in processing"

