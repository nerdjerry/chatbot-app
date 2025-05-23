import os
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage

class GPTHandler:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.endpoint = os.getenv("OPENAI_API_BASE")

    def get_explanation(self, code_snippet):

        try: 
            chat = AzureChatOpenAI(
                deployment_name = 'gpt-35-turbo',
                openai_api_type='azure',
                openai_api_key=self.api_key,
                openai_api_base=self.endpoint)

            messages = [HumanMessage(content=f"Explain the following code:\n{code_snippet}")]
            response = chat(messages=messages)
            return response.content
        except Exception as e:
            print(f"Error in GPTHandler: {e}")
            return "Error: Unable to process the code snippet."
