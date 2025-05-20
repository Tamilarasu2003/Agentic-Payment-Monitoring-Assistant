from crewai import Crew
from task import create_all_tasks
from agents import issue_identifier, failure_quantifier, solution_provider

def run_csv_crew(sample_data: str):
    tasks = create_all_tasks(sample_data)

    crew = Crew(
        agents=[issue_identifier, failure_quantifier, solution_provider],
        tasks=tasks,
    )

    result = crew.kickoff()
    return result
