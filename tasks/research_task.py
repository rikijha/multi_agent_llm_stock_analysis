from crewai import Task
from agents.research_agent import get_research_agent


def get_research_task(llm):
    return Task(
        description=(
            "Conduct research on {stock_symbol}. Your analysis should include:\n"
            "1. Current stock price and historical performance (5 years).\n"
            "2. Key financial metrics (P/E, EPS growth, revenue growth, margins).\n"
            "3. Recent news and press releases (1 month).\n"
            "4. Analyst ratings and price targets (min 3 analysts).\n"
            "5. Reddit sentiment analysis (100 posts).\n"
            "6. Major institutional holders and recent changes.\n"
            "7. Competitive landscape and {stock_symbol}'s market share.\n"
            "Use reputable financial websites for data."
        ),
        expected_output='A detailed 150-word research report with data sources and brief analysis.',
        agent=get_research_agent(llm)
    )