import os
import datetime

# Firecrawl API Key is now loaded from .env

import yaml
from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FirecrawlScrapeWebsiteTool

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

    def _get_url(self, agent_id):
        """
        Get the target URL based on the day of the week (KST) and agent ID.
        agent_id: 1, 2, 3, or 4
        """
        # 한국 시간(KST) 설정 (UTC+9)
        kst = datetime.timezone(datetime.timedelta(hours=9))
        today = datetime.datetime.now(kst).weekday() # 0=Mon, 1=Tue, ..., 6=Sun
        
        # 0: Mon, 3: Thu
        if today in [0, 3]:
            urls = {
                1: "https://www.defensenews.com/",
                2: "https://breakingdefense.com/",
                3: "https://www.shephardmedia.com/news/",
                4: "https://www.janes.com/osint-insights/defence-news"
            }
        # 1: Tue, 4: Fri, 6: Sun
        elif today in [1, 4, 6]:
            urls = {
                1: "https://thedefensepost.com/",
                2: "https://defence-industry.eu/",
                3: "https://www.cnbc.com/defense/",
                4: "https://www.defenseone.com/"
            }
        # 2: Wed, 5: Sat
        elif today in [2, 5]:
             urls = {
                1: "https://www.navalnews.com/",
                2: "https://www.reuters.com/business/aerospace-defense/",
                3: "https://www.nationaldefensemagazine.org/",
                4: "https://www.twz.com/"
            }
        else:
            # Fallback (should not happen with logic above covering 0-6)
            urls = {
                1: "https://www.defensenews.com/",
                2: "https://breakingdefense.com/",
                3: "https://www.shephardmedia.com/news/",
                4: "https://www.janes.com/osint-insights/defence-news"
            }
            
        return urls.get(agent_id)

    @agent
    def news_article_url_extractor(self) -> Agent:
        config = self.agents_config["news_article_url_extractor"]
        url = self._get_url(1)
        config["goal"] = f"Extract exactly 3 article URLs from the main page of {url} by analyzing the website structure and identifying the most recent and relevant news articles"
        
        return Agent(
            config=config,
            tools=[FirecrawlScrapeWebsiteTool()],
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
    def article_content_scraper(self) -> Agent:
        return Agent(
            config=self.agents_config["article_content_scraper"],
            tools=[FirecrawlScrapeWebsiteTool()],
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

    @agent
    def news_article_url_extractor_2(self) -> Agent:
        config = self.agents_config["news_article_url_extractor_2"]
        url = self._get_url(2)
        config["goal"] = f"Extract exactly 3 article URLs from the main page of {url} by analyzing the website structure and identifying the most recent and relevant news articles"

        return Agent(
            config=config,
            tools=[FirecrawlScrapeWebsiteTool()],
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
    def article_content_scraper_2(self) -> Agent:
        return Agent(
            config=self.agents_config["article_content_scraper_2"],
            tools=[FirecrawlScrapeWebsiteTool()],
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
    def news_article_url_extractor_3(self) -> Agent:
        config = self.agents_config["news_article_url_extractor_3"]
        url = self._get_url(3)
        config["goal"] = f"Extract exactly 3 article URLs from the main page of {url} by analyzing the website structure and identifying the most recent and relevant news articles"
        
        return Agent(
            config=config,
            tools=[FirecrawlScrapeWebsiteTool()],
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
    def article_content_scraper_3(self) -> Agent:
        return Agent(
            config=self.agents_config["article_content_scraper_3"],
            tools=[FirecrawlScrapeWebsiteTool()],
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
    def news_article_url_extractor_4(self) -> Agent:
        config = self.agents_config["news_article_url_extractor_4"]
        url = self._get_url(4)
        config["goal"] = f"Extract exactly 3 article URLs from the main page of {url} by analyzing the website structure and identifying the most recent and relevant news articles"

        return Agent(
            config=config,
            tools=[FirecrawlScrapeWebsiteTool()],
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
    def article_content_scraper_4(self) -> Agent:
        return Agent(
            config=self.agents_config["article_content_scraper_4"],
            tools=[FirecrawlScrapeWebsiteTool()],
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
    def extract_article_urls(self) -> Task:
        config = self.tasks_config["extract_article_urls"]
        url = self._get_url(1)
        config["description"] = f"""Navigate to the news website main page at {url} and extract exactly 3 REAL, EXISTING article URLs. You must:

    1. **ACTUALLY SCRAPE** the website using the scraping tool - do not generate or fabricate URLs
    2. **VERIFY** each URL leads to a real article by checking the scraped content
    3. **EXTRACT** only URLs that appear in the actual website content (links, href attributes)
    4. **VALIDATE** that URLs are complete and functional (include full domain)

    **CRITICAL**: You must use the scraping tool to get the actual website content, then extract real article URLs from that content. DO NOT create hypothetical or example URLs.

    Steps:
    1. Scrape the homepage to get actual content
    2. Look for article links in the scraped content (URLs containing /2024/, /2025/, /news/, etc.)
    3. Extract exactly 3 real article URLs
    4. Format as a simple list"""
        return Task(
            config=config,
            markdown=False,
        )

    @task
    def scrape_article_contents(self) -> Task:
        return Task(
            config=self.tasks_config["scrape_article_contents"],
            markdown=False,
        )

    @task
    def extract_article_urls_2(self) -> Task:
        config = self.tasks_config["extract_article_urls_2"]
        url = self._get_url(2)
        config["description"] = f"""Navigate to the news website main page at {url} and extract exactly 3 REAL, EXISTING article URLs. You must:

    1. **ACTUALLY SCRAPE** the website using the scraping tool - do not generate or fabricate URLs
    2. **VERIFY** each URL leads to a real article by checking the scraped content
    3. **EXTRACT** only URLs that appear in the actual website content (links, href attributes)
    4. **VALIDATE** that URLs are complete and functional (include full domain)

    **CRITICAL**: You must use the scraping tool to get the actual website content, then extract real article URLs from that content. DO NOT create hypothetical or example URLs.

    Steps:
    1. Scrape the homepage to get actual content
    2. Look for article links in the scraped content (URLs containing /2024/, /2025/, /news/, etc.)
    3. Extract exactly 3 real article URLs
    4. Format as a simple list"""
        return Task(
            config=config,
            markdown=False,
        )

    @task
    def scrape_article_contents_2(self) -> Task:
        return Task(
            config=self.tasks_config["scrape_article_contents_2"],
            markdown=False,
        )

    @task
    def extract_article_urls_3(self) -> Task:
        config = self.tasks_config["extract_article_urls_3"]
        url = self._get_url(3)
        config["description"] = f"""Navigate to the news website main page at {url} and extract exactly 3 REAL, EXISTING article URLs. You must:

    1. **ACTUALLY SCRAPE** the website using the scraping tool - do not generate or fabricate URLs
    2. **VERIFY** each URL leads to a real article by checking the scraped content
    3. **EXTRACT** only URLs that appear in the actual website content (links, href attributes)
    4. **VALIDATE** that URLs are complete and functional (include full domain)

    **CRITICAL**: You must use the scraping tool to get the actual website content, then extract real article URLs from that content. DO NOT create hypothetical or example URLs.

    Steps:
    1. Scrape the homepage to get actual content
    2. Look for article links in the scraped content (URLs containing /2024/, /2025/, /news/, etc.)
    3. Extract exactly 3 real article URLs
    4. Format as a simple list"""
        return Task(
            config=config,
            markdown=False,
        )

    @task
    def scrape_article_contents_3(self) -> Task:
        return Task(
            config=self.tasks_config["scrape_article_contents_3"],
            markdown=False,
        )

    @task
    def extract_article_urls_4(self) -> Task:
        config = self.tasks_config["extract_article_urls_4"]
        url = self._get_url(4)
        config["description"] = f"""Navigate to the news website main page at {url} and extract exactly 3 REAL, EXISTING article URLs. You must:

    1. **ACTUALLY SCRAPE** the website using the scraping tool - do not generate or fabricate URLs
    2. **VERIFY** each URL leads to a real article by checking the scraped content
    3. **EXTRACT** only URLs that appear in the actual website content (links, href attributes)
    4. **VALIDATE** that URLs are complete and functional (include full domain)

    **CRITICAL**: You must use the scraping tool to get the actual website content, then extract real article URLs from that content. DO NOT create hypothetical or example URLs.

    Steps:
    1. Scrape the homepage to get actual content
    2. Look for article links in the scraped content (URLs containing /2024/, /2025/, /news/, etc.)
    3. Extract exactly 3 real article URLs
    4. Format as a simple list"""
        return Task(
            config=config,
            markdown=False,
        )

    @task
    def scrape_article_contents_4(self) -> Task:
        return Task(
            config=self.tasks_config["scrape_article_contents_4"],
            markdown=False,
        )

    @task
    def analyze_and_prioritize_top_7_articles(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_and_prioritize_top_7_articles"],
            context=[
                self.scrape_article_contents(),
                self.scrape_article_contents_2(),
                self.scrape_article_contents_3(),
                self.scrape_article_contents_4(),
            ],
            markdown=False,
        )
        
    @task
    def rewrite_articles_in_korean(self) -> Task:
        return Task(
            config=self.tasks_config["rewrite_articles_in_korean"],
            context=[
                self.scrape_article_contents(),
                self.scrape_article_contents_2(),
                self.scrape_article_contents_3(),
                self.scrape_article_contents_4(),
                self.analyze_and_prioritize_top_7_articles()
            ],
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
