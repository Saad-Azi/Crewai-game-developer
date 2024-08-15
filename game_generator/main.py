from crewai import Process,Crew
from agents import GameAgents
from tasks import GameTasks
from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
llm=ChatOpenAI(model="gpt-4o-mini")


agnets=GameAgents()
tasks=GameTasks()


print("The crew is starting.")
print("----------------------------------")
instructions=input("Enter your desired game's description: ")

senior_software_engineer=agnets.create_senior_software_engineer_agent()
qa_engineer=agnets.create_qa_engineer_agent()
senior_qa_engineer=agnets.create_senior_qa_engineer_agent()
normal_agent=agnets.create_general_inquiry_agent()

code_generator=tasks.generate_game_code_task(agent=senior_software_engineer,instructions=instructions)
code_reviewer=tasks.review_game_code_task(agent=qa_engineer,instructions=instructions)
final_reviewr=tasks.finalize_game_code_review_task(agent=senior_qa_engineer,instructions=instructions)
general_task=tasks.handle_general_query_task(agent=normal_agent,instructions=instructions)

if "game" in instructions.lower() or "develop" in instructions.lower():
    game_crew=Crew(
        agents=[senior_software_engineer,qa_engineer,senior_qa_engineer],
        tasks=[code_generator,code_reviewer,final_reviewr],
        process=Process.sequential,
        verbose=True
    )

    game=game_crew.kickoff()

    print("\n\n########################")
    print("## Here is the result")
    print("########################\n")
    print("final code for the game:")
    print(game)
else:
    general_crew=Crew(
        agents=[normal_agent],
        tasks=[general_task],
        process=Process.sequential,
        verbose=True
    )
    response=general_crew.kickoff()
    print(response)