from langchain_community.llms import Ollama


def get_llm(model_name):
    try:
        llm = Ollama(model=model_name)
        return llm

    except Exception as e:
        print(f"Error: {e}")    
