import openai

def optimize_for_seo(content, keywords):
    prompt = f"Optimize this content for SEO. Make sure to incorporate keywords like {keywords}. Ensure the content follows SEO best practices like header tags, proper keyword density, and readability."
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1000
    )
    optimized_content = response.choices[0].text.strip()
    return optimized_content
