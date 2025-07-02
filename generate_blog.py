from openai import OpenAI
from config import OPENAI_API_KEY
from prompts import get_random_blog_prompt, META_DESCRIPTION_PROMPT
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_blog_post(topic, keywords):
    prompt_template = get_random_blog_prompt()
    prompt = prompt_template.format(topic=topic, keywords=", ".join(keywords))
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a professional content writer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500
    )
    return response.choices[0].message.content

def generate_meta_description(topic, keywords):
    prompt = META_DESCRIPTION_PROMPT.format(topic=topic, keywords=", ".join(keywords))
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a SEO expert."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    for item in [ {"topic": "remote work productivity", "keywords": ["remote work", "productivity", "work from home"]} ]:
        blog = generate_blog_post(item['topic'], item['keywords'])
        meta = generate_meta_description(item['topic'], item['keywords'])
        print("Blog Post:\n", blog)
        print("\nMeta Description:\n", meta)
