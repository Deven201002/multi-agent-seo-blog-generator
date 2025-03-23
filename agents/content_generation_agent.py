import openai

def generate_blog_content(outline):
    prompt = f"Write a detailed blog post based on this outline: {outline}. Make sure it is SEO-friendly and includes headings and subheadings."
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1500
    )
    content = response.choices[0].text.strip()
    return content
