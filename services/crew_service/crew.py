import os
import yaml
from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool

# Define paths relative to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AGENTS_CONFIG = os.path.join(BASE_DIR, "config", "agents.yaml")
TASKS_CONFIG = os.path.join(BASE_DIR, "config", "tasks.yaml")

@CrewBase
class DefenseNewsKoreanDailyDigestCrew:
    """DefenseNewsKoreanDailyDigest crew"""
    
    # Paths to configuration files
    agents_config = AGENTS_CONFIG
    tasks_config = TASKS_CONFIG

    @agent
    def defense_news_web_scraper(self) -> Agent:
        return Agent(
            config=self.agents_config["defense_news_web_scraper"],
            tools=[ScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            verbose=True,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def defense_news_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["defense_news_analyst"],
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            verbose=True,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def korean_defense_content_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["korean_defense_content_writer"],
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            verbose=True,
            llm=LLM(
                model="openai/gpt-4.1",
                temperature=0.7,
            ),
        )
    
    @task
    def scrape_defense_news_articles(self) -> Task:
        return Task(
            config=self.tasks_config["scrape_defense_news_articles"],
            markdown=False,
        )
    
    @task
    def analyze_and_prioritize_top_7_articles(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_and_prioritize_top_7_articles"],
            markdown=False,
        )
        
    @task
    def rewrite_articles_in_korean(self) -> Task:
        return Task(
            config=self.tasks_config["rewrite_articles_in_korean"],
            markdown=False,
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
