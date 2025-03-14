import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=API_KEY)

# Function to generate blog content
def generate_blog(topic, length):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Write a {length}-word blog post about '{topic}'. Make it engaging, well-structured, and informative."
        
        response = model.generate_content(prompt)
        
        return response.text if response else "Failed to generate content."
    
    except Exception as e:
        return f"Error: {str(e)}"
