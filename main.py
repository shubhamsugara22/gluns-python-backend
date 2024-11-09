from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from .routers import ai_api

app = FastAPI()
#app.include_router(ai_api.router, prefix="/api/v1/chat", tags=["Chat"])

# Define response models

# Define an Enum for contexts
class ContextEnum(str, Enum):
    CAPITAL_MANAGEMENT = "CAPITAL_MANAGEMENT"
    INVESTMENT = "INVESTMENT"
    SAVE_MONEY = "SAVE_MONEY"
    BILLS_BALANCE = "BILLS_BALANCE"
    SUMMARY_INVOICES = "SUMMARY_INVOICES"

# Define the request model for user input and context
class UserInputRequest(BaseModel):
    context: ContextEnum
    input: str

class ContextResponse(BaseModel):
    message: str
    body: List[str]

class ChatResponse(BaseModel):
    message: str
    body: dict
    
# Request model for input
class InputRequest(BaseModel):
    context: ContextEnum
    input: str

# Response model for output
class OutputResponse(BaseModel):
    output: str

@app.get("/")
async def root():
	return {"message": "FastAPI is running"}

# 1. GET /api/v1/chat/contexts - Retrieve list of contexts
@app.get("/api/v1/chat/contexts", response_model=ContextResponse)
async def get_contexts():
    return {
        "message": "Contexts retrieved successfully",
        "body": [
            ContextEnum.CAPITAL_MANAGEMENT,
            ContextEnum.INVESTMENT,
            ContextEnum.SAVE_MONEY,
            ContextEnum.BILLS_BALANCE,
            ContextEnum.SUMMARY_INVOICES
        ]
    }

# 2. POST /api/v1/chat - Handle user input with a context and text
@app.post("/api/v1/chat", response_model=ChatResponse)
async def post_chat(user_input: UserInputRequest):
    # Here we will simulate processing the input based on the context
    response_data = {
        "context": user_input.context,
        "input": user_input.input,
        "response": f"Processed input for {user_input.context}"
    }
    return {
        "message": "User input processed successfully",
        "body": response_data
    }

# Dummy endpoint for testing
@app.post("/api/v1/output", response_model=OutputResponse)
async def get_output(request: InputRequest):
    # Here you can implement your logic, for now we are returning dummy output
    return OutputResponse(output="DummyInput")