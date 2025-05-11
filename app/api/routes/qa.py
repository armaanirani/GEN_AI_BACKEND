from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.api.deps.auth import verify_api_key
from app.services.qa_service import get_answer
from utils.logger import logger

router = APIRouter()

class AnswerRequest(BaseModel):
    provider: str
    model: str
    question: str
    
class AnswerResponse(BaseModel):
    answer: str
    
@router.post("/llm/get_answer", tags=["LLM"], response_model=AnswerResponse,
             dependencies=[Depends(verify_api_key)])
async def get_answer_from_llm(request: AnswerRequest):
    """
    Get an answer from the specified LLM provider with the given model name and parameters.
    
    Args:
        request (AnswerRequest): The request object containing provider, model, and question.
    
    Returns:
        AnswerResponse: The response object containing the answer from the LLM.
    """
    logger.info(f"Received request to get answer from {request.provider} model: {request.model} for the question: {request.question}")
    
    try:
        answer = get_answer(provider=request.provider, model=request.model, question=request.question)
        logger.info(f"Answer generated successfully.")
        return answer
    except Exception as e:
        logger.exception(f"Error generating answer: {e}")
        raise