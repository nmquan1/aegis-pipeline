import re
from config.config import gemini_model


def get_friendliness_score(text, community):
    prompt = f"""
    Rate the offensiveness towards {community} strictly from 0.01 to 0.39.
    of the following comment:   
    Comment: "{text}"
    If it's negative but irrelevant to this community, return 0.4
    """
    try:
        response = gemini_model.generate_content(prompt)
        matches = re.findall(r"[0-9]*\.?[0-9]+", response.text.strip())

        if matches:
            score = float(matches[0])
            return score
    except Exception as e:
        print(f"Friendliness score failed: {e}")
    return 0.5  # Return a default score if the model fails



def generate_summary(comments):
    joined = "\n".join(comments)
    prompt = f"""Summarize the following comments:\n{joined} Only include the most relevant information. 
    Provide just the summary, nothing else."""

    try:
        response = gemini_model.generate_content(prompt)

        if hasattr(response, 'text') and response.text.strip():
            return response.text.strip()
    except Exception as e:
        print(f"Summary generation failed: {e}")

    return "No summary available."