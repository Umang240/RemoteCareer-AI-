import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_career_advice(
    education: str,
    skills: list,
    target_role: str
):

    prompt = f"""
    Return ONLY valid JSON in the following format:

    {{
      "career_advice": "",
      "next_skills": [],
      "recommended_projects": [],
      "interview_tips": []
    }}

    Education: {education}
    Skills: {', '.join(skills)}
    Target Role: {target_role}

    Do not include markdown formatting.
    Do not use code blocks.
    Return only JSON.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    try:
        cleaned_text = (
            response.text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return json.loads(cleaned_text)

    except json.JSONDecodeError:
        return {
            "error": "Failed to parse Gemini response",
            "raw_response": response.text
        }