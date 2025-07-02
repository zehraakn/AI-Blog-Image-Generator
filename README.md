# AI Blog & Image Generator

This project leverages OpenAI’s GPT-4o model to generate SEO-optimized blog posts and DALL·E 3 to create relevant images for those posts. It automates the creation of high-quality, engaging content that is ready for publishing.

## Features
- **Blog Post Generation:** Creates detailed, SEO-friendly blog articles based on given topics and keywords.

- **Content Auditing & Optimization:** Improves readability and clarity of the generated content.

- **Image Generation:** Produces original images based on blog post descriptions using DALL·E 3.

- **File System Storage:** Saves original and optimized blog posts, image descriptions, and image URLs to local directories.
## Example: 'sustainable_travel_trends'
![image](https://github.com/user-attachments/assets/25d2b647-1bf7-46c0-9205-6ebf2d671402)
![image](https://github.com/user-attachments/assets/140699fa-b1a4-4f49-949a-aa7f38cfa2ac)

## Getting Started

### Requirements
- Python 3.6+
- OpenAI API key

## Local Setup

### Update the Keywords List

To generate blog posts, the `keywords.py` file must be populated with topics and their associated keywords. This list is crucial as it directs the content generation process for each blog post.

### Guidelines for Keywords
- **Relevance:** Ensure that the keywords are highly relevant to the topic to maintain the focus and quality of the generated content.
- **Variety:** Use a mix of broad and specific keywords to cover the topic comprehensively.
- **Limitation:** While it's important to include multiple keywords, avoid overstuffing to keep the content natural and engaging.

By carefully selecting topics and corresponding keywords, you can tailor the content generation to meet specific themes and focus areas, enhancing the relevance and quality of your blog posts.


### Install Required Libraries

```
pip install openai requests
```

### Set Up Your OpenAI API Key
Replace 'your-openai-api-key' in the `config.py` file with your actual OpenAI API key.

### Run the Main Script
Navigate to your project directory in the terminal and execute:
```
python main.py
```

This will generate blog posts, audit them, create image descriptions, generate images, and save all these contents into their respective directories on the file system.


## Cost Estimation
- **DALL-E 3:** Approximately $0.08 per image.
- **GPT-4o:** Approximately $0.01 per blog post.
