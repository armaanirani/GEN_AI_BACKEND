from utils.logger import logger
from app.llm.llm_factory import load_llm

def get_answer(provider, model, question):
    """
    Get an answer from the specified LLM provider with the given model name and parameters.

    Args:
        provider (str): The LLM provider to use (e.g., 'Groq', 'Ollama', 'OpenAI').
        model (str): The name of the model to load.
        question (str): The question to ask the LLM.

    Returns:
        str: The answer from the LLM.
    """
    logger.info(f"Getting answer from {provider} model: {model} for the question: {question}")
    
    try:
        llm = load_llm(provider=provider, model=model)
        logger.debug(f"Loaded {provider} model: {model}")

        response = llm.invoke(question)
        answer = response.content
        
        logger.info(f"Answer generated successfully from {provider} model: {model}")
        logger.debug(f"Answer: {answer}")
        
        return {"answer": answer}
    except Exception as e:
        logger.exception(f"Error generating answer: {e}")
        return {"error": "Failed to generate answer."}