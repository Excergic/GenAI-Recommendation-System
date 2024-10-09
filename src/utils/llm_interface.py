import requests
import yaml
from pathlib import Path

class LLMInterface:
    def __init__(self, api_url=None):
        # Load configuration from config.yaml
        config_path = Path("D:\Project 1\config\config.yaml")
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        
        self.api_url = api_url or config['models']['llm']['api_url']
        self.default_model = config['models']['llm']['default_model']

    def generate_recommendations(self, prompt: str, system_prompt: str) -> str:
        try:
            response = requests.post(self.api_url, json={
                "prompt": prompt,
                "system_prompt": system_prompt,
                "model": self.default_model  # Include the model in the request
            })

            if response.status_code == 200:
                return response.json().get('text', "No recommendations generated")
            else:
                return f"Error: {response.status_code} - {response.text}"

        except Exception as e:
            return f"Error: {str(e)}"
