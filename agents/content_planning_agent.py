import openai

def generate_blog_outline(topic):
    prompt = f"Create a structured blog outline about {topic}. Include an introduction, key discussion points, and a conclusion."
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    outline = response.choices[0].text.strip()
    return outline
