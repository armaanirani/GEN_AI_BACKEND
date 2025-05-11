from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from utils.logger import logger

def load_llm(provider: str, model: str) -> object:
    """
    Load the specified LLM provider with the given model name and parameters.
    
    Args:
        provider (str): The LLM provider to use (e.g., 'Groq', 'Ollama', 'OpenAI').
        model_name (str): The name of the model to load.
    
    Returns:
        object: The loaded LLM instance.
    """
    logger.info(f"Loading {provider} model: {model}")
    
    try:
        if provider == "Groq":
            llm = ChatGroq(model=model, temperature=0)
        elif provider == "Ollama":
            llm = ChatOllama(model=model, temperature=0)
        elif provider == "OpenAI":
            llm = ChatOpenAI(model=model, temperature=0)
        else:
            logger.error(f"Unsupported LLM provider: {provider}")
            raise ValueError(f"Unsupported LLM provider: {provider}")
        
        logger.info(f"Loaded {provider} model: {model}")
        return llm
    
    except Exception as e:
        logger.exception(f"Error loading {provider} model: {model}")
        raise

