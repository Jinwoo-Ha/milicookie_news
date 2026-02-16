import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	FirecrawlScrapeWebsiteTool
)





@CrewBase
class MultiSiteNewsArticleScrapingAutomationCrew:
    """MultiSiteNewsArticleScrapingAutomation crew"""

    
    @agent
    def news_article_url_extractor(self) -> Agent:
        
        return Agent(
            config=self.agents_config["news_article_url_extractor"],
            
            
            tools=[				FirecrawlScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def article_content_scraper(self) -> Agent:
        
        return Agent(
            config=self.agents_config["article_content_scraper"],
            
            
            tools=[				FirecrawlScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4.1",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def news_article_url_extractor_2(self) -> Agent:
        
        return Agent(
            config=self.agents_config["news_article_url_extractor_2"],
            
            
            tools=[				FirecrawlScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def article_content_scraper_2(self) -> Agent:
        
        return Agent(
            config=self.agents_config["article_content_scraper_2"],
            
            
            tools=[				FirecrawlScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def news_article_url_extractor_3(self) -> Agent:
        
        return Agent(
            config=self.agents_config["news_article_url_extractor_3"],
            
            
            tools=[				FirecrawlScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def article_content_scraper_3(self) -> Agent:
        
        return Agent(
            config=self.agents_config["article_content_scraper_3"],
            
            
            tools=[				FirecrawlScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def news_article_url_extractor_4(self) -> Agent:
        
        return Agent(
            config=self.agents_config["news_article_url_extractor_4"],
            
            
            tools=[				FirecrawlScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def article_content_scraper_4(self) -> Agent:
        
        return Agent(
            config=self.agents_config["article_content_scraper_4"],
            
            
            tools=[				FirecrawlScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    

    
    @task
    def extract_article_urls(self) -> Task:
        return Task(
            config=self.tasks_config["extract_article_urls"],
            markdown=False,
            
            
        )
    
    @task
    def extract_article_urls_2(self) -> Task:
        return Task(
            config=self.tasks_config["extract_article_urls_2"],
            markdown=False,
            
            
        )
    
    @task
    def extract_article_urls_3(self) -> Task:
        return Task(
            config=self.tasks_config["extract_article_urls_3"],
            markdown=False,
            
            
        )
    
    @task
    def extract_article_urls_4(self) -> Task:
        return Task(
            config=self.tasks_config["extract_article_urls_4"],
            markdown=False,
            
            
        )
    
    @task
    def scrape_article_contents(self) -> Task:
        return Task(
            config=self.tasks_config["scrape_article_contents"],
            markdown=False,
            
            
        )
    
    @task
    def scrape_article_contents_2(self) -> Task:
        return Task(
            config=self.tasks_config["scrape_article_contents_2"],
            markdown=False,
            
            
        )
    
    @task
    def scrape_article_contents_3(self) -> Task:
        return Task(
            config=self.tasks_config["scrape_article_contents_3"],
            markdown=False,
            
            
        )
    
    @task
    def scrape_article_contents_4(self) -> Task:
        return Task(
            config=self.tasks_config["scrape_article_contents_4"],
            markdown=False,
            
            
        )
    
    @task
    def final_output(self) -> Task:
        return Task(
            config=self.tasks_config["final_output"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the MultiSiteNewsArticleScrapingAutomation crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )


