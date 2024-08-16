from crewai import Process, Crew
from agents import GameAgents
from tasks import GameTasks
from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the language model
llm = ChatOpenAI(model="gpt-4o-mini")

# Initialize agents and tasks
agents = GameAgents()
tasks = GameTasks()

def create_crew_for_game(instructions):
    # Define agents and tasks for game development
    senior_software_engineer = agents.create_senior_software_engineer_agent()
    qa_engineer = agents.create_qa_engineer_agent()
    senior_qa_engineer = agents.create_senior_qa_engineer_agent()

    code_generator = tasks.generate_game_code_task(agent=senior_software_engineer, instructions=instructions)
    code_reviewer = tasks.review_game_code_task(agent=qa_engineer, instructions=instructions)
    final_reviewer = tasks.finalize_game_code_review_task(agent=senior_qa_engineer, instructions=instructions)

    return Crew(
        agents=[senior_software_engineer, qa_engineer, senior_qa_engineer],
        tasks=[code_generator, code_reviewer, final_reviewer],
        process=Process.sequential,
        verbose=True
    )

def create_crew_for_general_task(instructions):
    # Define agents and tasks for general inquiries
    normal_agent = agents.create_general_inquiry_agent()
    general_task = tasks.handle_general_query_task(agent=normal_agent, instructions=instructions)

    return Crew(
        agents=[normal_agent],
        tasks=[general_task],
        process=Process.sequential,
        verbose=True
    )

def main():
    print("The crew is starting.")
    print("----------------------------------")

    instructions = input("Enter your desired game's description: ")

    # Determine which crew to use based on instructions
    if "game" in instructions.lower() or "develop" in instructions.lower():
        crew = create_crew_for_game(instructions)
        result = crew.kickoff()
        print("\n\n########################")
        print("## Here is the result")
        print("########################\n")
        print("Final code for the game:")
        print(result)
    else:
        crew = create_crew_for_general_task(instructions)
        response = crew.kickoff()
        print(response)

if __name__ == "__main__":
    main()
