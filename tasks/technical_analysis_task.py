from crewai import Task
from agents.technical_analyst_agent import get_technical_analyst_agent


def get_technical_analysis_task(llm):
    return Task(
        description=(
            "Perform technical analysis on {stock_symbol}. Include:\n"
            "1. 50-day and 200-day moving averages (1 year).\n"
            "2. Key support and resistance levels (3 each).\n"
            "3. RSI and MACD indicators.\n"
            "4. Volume analysis (3 months).\n"
            "5. Significant chart patterns (6 months).\n"
            "6. Fibonacci retracement levels.\n"
            "7. Comparison with sector's average.\n"
            "Use the yf_tech_analysis tool for data."
        ),
        expected_output='A 100-word technical analysis report with buy/sell/hold signals and annotated charts.',
        agent = get_technical_analyst_agent(llm)
    )