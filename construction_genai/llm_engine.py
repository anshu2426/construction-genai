from google import genai
from prompts import site_report_prompt
import os
from dotenv import load_dotenv
# Load .env file
load_dotenv()

# Get API key from environment
API_KEY = os.getenv("GOOGLE_API_KEY")

# Create Client
client = genai.Client(
    api_key= API_KEY # or api_key="YOUR_API_KEY"
)

def generate_report(topic, context):
    prompt = site_report_prompt(topic, context)

    # Generate content using Gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
