from crewai import Agent
from crewai_tools import SerperDevTool
from tools.sentiment_analysis_tool import reddit_sentiment_analysis
from tools.yf_tech_analysis_tool import yf_tech_analysis
from tools.yf_fundamental_analysis_tool import yf_fundamental_analysis
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from dotenv import load_dotenv
import os

load_dotenv(".env")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")
os.environ["REDDIT_CLIENT_SECRET"] = os.getenv("REDDIT_CLIENT_SECRET")
os.environ["REDDIT_USER_AGENT"] = os.getenv("REDDIT_USER_AGENT")


def get_reporter_agent(llm):
    reddit_tool = reddit_sentiment_analysis
    serper_tool = SerperDevTool()
    yf_tech_tool = yf_tech_analysis
    yf_fundamental_tool = yf_fundamental_analysis
    reporter = Agent(
        role='Chief Investment Strategist',
        goal='Synthesize all analyses to create a definitive investment report on {stock_symbol}',
        verbose=True,
        memory=True,
        backstory="As a seasoned investment strategist with 20 years of experience, you weave complex financial data into compelling investment narratives.",
        tools=[reddit_tool, serper_tool, yf_fundamental_tool, yf_tech_tool, YahooFinanceNewsTool()],
        llm=llm
    )
    return reporter
