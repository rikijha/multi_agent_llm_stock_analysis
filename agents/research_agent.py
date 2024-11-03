from crewai import Agent
from tools.sentiment_analysis_tool import reddit_sentiment_analysis
from crewai_tools import SerperDevTool
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from dotenv import load_dotenv
import os

load_dotenv(".env")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")
os.environ["REDDIT_CLIENT_SECRET"] = os.getenv("REDDIT_CLIENT_SECRET")
os.environ["REDDIT_USER_AGENT"] = os.getenv("REDDIT_USER_AGENT")


def get_research_agent(llm):
    reddit_tool = reddit_sentiment_analysis
    serper_tool = SerperDevTool()
    researcher = Agent(
        role='Senior Stock Market Researcher',
        goal='Gather and analyze comprehensive data about {stock_symbol}',
        verbose=True,
        memory=True,
        backstory="With a Ph.D. in Financial Economics and 15 years of experience in equity research, you're known for your meticulous data collection and insightful analysis.",
        tools=[reddit_tool, serper_tool, YahooFinanceNewsTool()],
        llm=llm
    )
    return researcher