from openai import OpenAI
from config import OPENAI_API_KEY
from prompts import IMAGE_DESCRIPTION_PROMPT

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_image_description(topic):
    prompt = IMAGE_DESCRIPTION_PROMPT.format(topic=topic)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a creative image description writer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )
    return response.choices[0].message.content

def generate_image(image_description):
    response = client.images.generate(
        model="dall-e-3",
        prompt=image_description,
        n=1,
        size="1024x1024",
        quality="standard"
    )
    return response.data[0].url

if __name__ == "__main__":
    desc = generate_image_description("remote work productivity")
    print(desc)
