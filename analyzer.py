import os
from pathlib import Path

from google import genai
from google.genai import types

from schemas import CodeReview

from dotenv import load_dotenv


SYSTEM_INSTRUCTION = """
You are a senior software engineer reviewing a single source code file.

Analyze the code and return:
- overall_quality_summary
- general_score (from 1 to 5)
- estimated_complexity (Big O notation)
- strengths
- issues
- improvements

Rules:
- Be concise and objective.
- Base your analysis only on the provided code.
- Do not invent project context.
- Return only valid JSON.
"""


def analyze_code(file_path: str) -> CodeReview:
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY must be set")

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError("File not found")

    code = path.read_text(encoding="utf-8")

    prompt = f"""
    Review the following code and return the JSON output:

    Code:
    {code}
    """

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            response_mime_type="application/json",
            response_json_schema=CodeReview.model_json_schema(),
        ),
    )

    return CodeReview.model_validate_json(response.text)
