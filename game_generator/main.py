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

senior_software_engineer=agnets.senior_software_engineer()
qa_engineer=agnets.qa_engineer()
senior_qa_engineer=agnets.senior_qa_engineer()
normal_agent=agnets.normal_agent()

code_generator=tasks.code_generator(agent=senior_software_engineer,instructions=instructions)
code_reviewer=tasks.code_reviewer(agent=qa_engineer,instructions=instructions)
final_reviewr=tasks.final_reviewr(agent=senior_qa_engineer,instructions=instructions)
general_task=tasks.general_task(agent=normal_agent,instructions=instructions)

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