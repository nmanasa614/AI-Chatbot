print("NEW CHATBOT FILE LOADED")
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=API_KEY
)

def get_response(
    prompt,
    pdf_text="",
    image=None,
    meeting_mode=False,
    email_mode=False,
    report_mode=False,
    translator_mode=False,
    sentiment_mode=False
):
    if sentiment_mode:

        final_prompt = f"""
Analyze the sentiment of the following text.

Provide:
1. Sentiment
2. Confidence
3. Explanation

Text:
{prompt}
"""
    elif translator_mode:

        final_prompt = f"""
You are a translator.

Translate the user's text to the language requested.

User:
{prompt}
"""
    elif report_mode:

        final_prompt = f"""
Create a professional report.

Include:

1. Title
2. Introduction
3. Objectives
4. Analysis
5. Findings
6. Conclusion
7. Recommendations

Content:
{prompt}
"""

    elif email_mode:

        final_prompt = f"""
Write a professional email.

User Request:
{prompt}

Include:
- Subject
- Greeting
- Body
- Closing
"""

    elif meeting_mode:

        final_prompt = f"""
You are an AI Meeting Summarizer.

Summarize the following content.

Provide:
1. Meeting Summary
2. Key Discussion Points
3. Decisions Taken
4. Action Items
5. Conclusion

User:
{prompt}
"""

    else:

        final_prompt = f"""
You are a multilingual AI assistant.

Rules:
- Reply in the same language used by the user.
- Support English, Telugu, Hindi and other languages.

PDF Content:
{pdf_text}

User:
{prompt}
"""

    try:

        if image:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[prompt, image]
            )

        else:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=final_prompt
            )

        return response.text

    except Exception as e:

        return str(e)