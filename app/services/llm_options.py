from utils.config import app_config

def fetch_llm_options():
    """
    Fetches the LLM options from the app configuration.
    """
    llm_config = app_config["llm"]
    return llm_config