import subprocess
import time


def install_ollama():
    """Install Ollama using the official shell script."""
    print("Installing Ollama...")
    subprocess.run("curl -fsSL https://ollama.com/install.sh | sh", shell=True, check=True)
    print("Ollama installed successfully.")


def start_ollama_server():
    """Start Ollama server in a background process."""
    print("Starting Ollama server...")
    process = subprocess.Popen(
        "ollama serve", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    time.sleep(5)  # Wait for the server to be ready
    print("Ollama server is running.")
    return process


def pull_model(model_name="gemma3:1b"):
    """Pull a specified Ollama model."""
    print(f"Pulling model: {model_name}")
    subprocess.run(f"ollama pull {model_name}", shell=True, check=True)
    print(f"Model '{model_name}' pulled successfully.")


def get_llm(model_name="gemma3:1b"):
    from langchain_ollama.llms import OllamaLLM

    """Initialize the LangChain Ollama LLM."""
    print(f"Loading LLM model: {model_name}")
    return OllamaLLM(model=model_name)


if __name__ == "__main__":
    # install_ollama()
    # server_process = start_ollama_server()
    # pull_model()

    llm = get_llm()
    print(llm.invoke("who are you?"))
    print("LLM is ready to use.")
