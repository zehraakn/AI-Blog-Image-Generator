from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def optimize_blog_post(blog_post):
    prompt = f"""
    You are an expert editor. Improve this blog post by making it more clear, engaging, and easy to understand for a general audience. Use simple language:

    {blog_post}

    Return only the improved blog post.
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert editor."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    sample = "This is a sample blog text that needs to be improved for clarity and simplicity."
    improved = optimize_blog_post(sample)
    print(improved)
