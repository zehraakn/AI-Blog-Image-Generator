import random

BLOG_POST_PROMPTS = [
    """
    Write an in-depth blog post about "{topic}". Use these keywords strategically: {keywords}. 
    The post should have:
    1. Introduction
    2. Key Trends and Insights
    3. Practical Advice
    4. Real-world Examples
    5. Summary with a call to action
    Use headings and bullet points for clarity.
    """,
    """
    Create a detailed and engaging blog post on "{topic}" with keywords: {keywords}. 
    Structure it as:
    - Overview
    - Challenges and Solutions
    - Expert Tips
    - Case Studies
    - Final Thoughts and Recommendations
    """
]

META_DESCRIPTION_PROMPT = """
Generate a concise meta description (max 160 characters) for a blog post about "{topic}" that includes these keywords: {keywords}.
"""

IMAGE_DESCRIPTION_PROMPT = """
Create a vivid and detailed image description for a blog post titled "{topic}". The image should visually represent the key ideas.
"""

def get_random_blog_prompt():
    return random.choice(BLOG_POST_PROMPTS)
