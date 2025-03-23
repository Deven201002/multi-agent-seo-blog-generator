import openai

def review_and_improve(content):
    prompt = f"Proofread this content and make necessary improvements to grammar, spelling, and readability."
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1000
    )
    improved_content = response.choices[0].text.strip()
    return improved_content
