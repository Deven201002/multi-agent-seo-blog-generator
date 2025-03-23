import openai
import requests
from bs4 import BeautifulSoup


def fetch_trending_hr_topics():
  
    prompt = "What are the most discussed HR topics currently in the news?"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    topics = response.choices[0].text.strip()
    return topics


def scrape_hr_information():
    url = "https://www.shrm.org/ResourcesAndTools/hr-topics/pages/default.aspx"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    hr_info = soup.find_all('a', class_='view-link') 
    return [link.get_text() for link in hr_info]
