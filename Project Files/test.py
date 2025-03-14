from gemini_api import generate_blog

topic = "Benefits of AI in Healthcare"
length = 500

blog_content = generate_blog(topic, length)
print(blog_content)