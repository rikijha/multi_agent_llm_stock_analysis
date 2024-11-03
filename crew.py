import os
from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from agents.research_agent import get_research_agent
from agents.fundamental_analyst_agent import get_fundamental_analyst_agent
from agents.technical_analyst_agent import get_technical_analyst_agent
from agents.reporter_agent import get_reporter_agent
from tasks.research_task import get_research_task
from tasks.technical_analysis_task import get_technical_analysis_task
from tasks.fundamental_analysis_task import get_fundamental_analysis_task
from tasks.report_task import get_report_task
load_dotenv(".env")

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_MODEL="gpt-3.5-turbo-0125"

def create_crew(stock_symbol):
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model='gpt-4o-mini', temperature=0.1)
    crew = Crew(
        agents=[get_research_agent(llm), get_technical_analyst_agent(llm), get_fundamental_analyst_agent(llm), get_reporter_agent(llm)],
        tasks=[get_research_task(llm), get_technical_analysis_task(llm), get_fundamental_analysis_task(llm), get_report_task(llm)],
        process=Process.sequential,
        cache=True
    )
    result = crew.kickoff(inputs={'stock_symbol': stock_symbol})
    os.makedirs('./crew_results', exist_ok=True)
    file_path = f"./crew_results/crew_result_{stock_symbol}.md"
    result_str = str(result)
    with open(file_path, 'w') as file:
        file.write(result_str)

    return file_path
