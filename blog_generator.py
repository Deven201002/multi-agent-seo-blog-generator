import openai
from agents.research_agent import fetch_trending_hr_topics, scrape_hr_information
from agents.content_planning_agent import generate_blog_outline
from agents.content_generation_agent import generate_blog_content
from agents.seo_optimization_agent import optimize_for_seo
from agents.review_agent import review_and_improve


openai.api_key = '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'

def main():
  
    trending_topic = fetch_trending_hr_topics()
    print(f"Trending HR Topic: {trending_topic}")
    
   
    outline = generate_blog_outline(trending_topic)
    print(f"Blog Outline: {outline}")
    
   
    content = generate_blog_content(outline)
    print(f"Blog Content: {content[:500]}...")
    
    
    keywords = "HR trends, employee wellbeing, leadership development"
    seo_content = optimize_for_seo(content, keywords)
    print(f"SEO Optimized Content: {seo_content[:500]}...")
    
   
    final_blog = review_and_improve(seo_content)
    print(f"Final Blog Post: {final_blog[:500]}...")
    
    
    with open('final_blog_post.txt', 'w') as f:
        f.write(final_blog)

if __name__ == "__main__":
    main()
