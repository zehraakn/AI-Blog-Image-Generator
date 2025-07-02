import os
import uuid
from keywords import KEYWORDS_LIST
from generate_blog import generate_blog_post, generate_meta_description
from optimize_blog import optimize_blog_post
from generate_image import generate_image_description, generate_image

def save_text(path, filename, content):
    with open(os.path.join(path, filename), "w", encoding="utf-8") as f:
        f.write(content)

def main():
    base_dir = "generated_blogs"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    for item in KEYWORDS_LIST:
        topic = item['topic']
        keywords = item['keywords']

        folder_name = f"{topic.replace(' ', '_')}_{uuid.uuid4().hex[:6]}"
        folder_path = os.path.join(base_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        print(f"Generating blog for: {topic}")
        blog = generate_blog_post(topic, keywords)
        save_text(folder_path, "blog_original.txt", blog)

        optimized = optimize_blog_post(blog)
        save_text(folder_path, "blog_optimized.txt", optimized)

        meta_desc = generate_meta_description(topic, keywords)
        save_text(folder_path, "meta_description.txt", meta_desc)

        image_desc = generate_image_description(topic)
        save_text(folder_path, "image_description.txt", image_desc)

        image_url = generate_image(image_desc)
        save_text(folder_path, "image_url.txt", image_url)

        print(f"Done for topic: {topic}\n{'='*40}")

if __name__ == "__main__":
    main()
