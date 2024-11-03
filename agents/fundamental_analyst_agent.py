from crewai import Agent
from tools.yf_fundamental_analysis_tool import yf_fundamental_analysis



def get_fundamental_analyst_agent(llm):
    yf_fundamental_tool = yf_fundamental_analysis
    fundamental_analyst = Agent(
        role='Senior Fundamental Analyst',
        goal='Conduct a comprehensive fundamental analysis of {stock_symbol}',
        verbose=True,
        memory=True,
        backstory="With a CFA charter and 15 years of experience in value investing, you dissect financial statements and identify key value drivers.",
        tools=[yf_fundamental_tool],
        llm=llm
    )
    return fundamental_analyst

