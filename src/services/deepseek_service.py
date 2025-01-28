import requests
import os

class DeepSeekService:
    def __init__(self):
        self.api_key = os.getenv("DEEPSEEK_API_KEY", "sk-e7873548576047718a7b8930018f0380")
        self.api_url = os.getenv("DEEPSEEK_API_URL", "https://api.deepseek.com/v1/chat/completions")
        self.chat_history = ""

    def get_response(self, question):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"之前的聊天记录：\n{self.chat_history}\n用户的新问题：\n{question}"},
            ],
            "stream": False,
        }

        response = requests.post(self.api_url, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            answer = data["choices"][0]["message"]["content"]
            self.chat_history += f"用户: {question}\n助手: {answer}\n"
            return answer
        else:
            return f"Error: {response.status_code}, {response.text}" 