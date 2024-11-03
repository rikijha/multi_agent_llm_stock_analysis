from crewai import Agent
from tools.yf_tech_analysis_tool import yf_tech_analysis


def get_technical_analyst_agent(llm):
    yf_tech_tool = yf_tech_analysis
    technical_analyst = Agent(
        role='Expert Technical Analyst',
        goal='Perform an in-depth technical analysis on {stock_symbol}',
        verbose=True,
        memory=True,
        backstory="As a Chartered Market Technician (CMT) with 15 years of experience, you have a keen eye for chart patterns and market trends.",
        tools=[yf_tech_tool],
        llm=llm
    )
    return technical_analyst