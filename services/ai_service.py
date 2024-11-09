# import openai  # Assuming you're using OpenAI API; replace with your model 
from prompts import USER_PROMPT
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from main import UserInputRequest

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)


def process_with_llm(user_request: UserInputRequest) -> str:
    # Placeholder for actual model call
    try:
        chat_template = ChatPromptTemplate([
            ("system", "You are a helpful Bank Assistant. Answer in short responses."),
            ("human", f"{USER_PROMPT}"),
        ])


        messages = chat_template.invoke({
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

