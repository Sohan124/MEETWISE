import os
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

# Azure OpenAI credentials
openai.api_type = "azure"
openai.api_key = os.getenv("AZURE_API_KEY")
openai.api_base = os.getenv("AZURE_ENDPOINT")
openai.api_version = os.getenv("AZURE_API_VERSION")
deployment_name = os.getenv("AZURE_DEPLOYMENT_NAME")

# DEBUG PRINT
print("Deployment Name:", deployment_name)

def process_meeting(transcript):
    response = openai.ChatCompletion.create(
        deployment_id=deployment_name,
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant that summarizes meetings and assigns tasks."
            },
            {
                "role": "user",
                "content": f"Analyze this meeting transcript and provide a summary and tasks:\n\n{transcript}"
            }
        ]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    with open("transcript.txt", "r", encoding="utf-8") as file:
        transcript = file.read()

    result = process_meeting(transcript)

    print("\n📝 AI Summary & Tasks:\n")
    print(result)
