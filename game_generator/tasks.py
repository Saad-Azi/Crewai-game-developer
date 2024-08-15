from textwrap import dedent
from crewai import Task

class GameTasks():
    def code_generator(self,agent,instructions):
        return Task(
            description=dedent(
                f"""\
                Your task is to analyze the query first, if it is regarding a game then generate a quality code written in python to develop a game.
                The code should be very clean and flawless.
                These are the instructions to develop a game: {instructions}.
                Return the code in python to develop that game. Do not return anything else.
                """
            ),
            expected_output="Only the code of the game written in the python.",
            agent=agent
        )
    
    def code_reviewer(self,agent,instructions):
        return Task(
            description=dedent(
                f"""\
                Your task is to analyze the query first, if it is regarding a game then identify and fix the potential errors in the game  icluding the import errors,not defined variables, syntax errors and indentation errors.
                These are the instructions of the game to be developed: {instructions}.
                Return only the code of the game with the errors fixed.
                """
            ),
            expected_output="Only the code of the game with the errors fixed.",
            agent=agent
        )
    
    def final_reviewr(self,agent,instructions):
        return Task(
            description=dedent(
                f"""\
                Your task is to analyze the query first, if it is regarding a game then ensure the quality of the code written in python.You should give ita  final review and check if this code will work as expected. You are allowed to make changes in the code to increase it's quality if needed.
                These are the instructions of teh game: {instructions},
                Return the code of the game with the changes made to increase it's quality if needed.
                """
            ),
            expected_output="Only the code of the game with the changes made to increase it's quality if needed.",
            agent=agent,
            output_file="./game.py"
        )
    def general_task(self,agent,instructions):
        return Task(
            description=dedent(
                f"""\
                    Your task is to provide useful and accurate information according to the user's query: {instructions}.
                """
            ),
            expected_output="Only the information that answers the user's query.",
            agent=agent,
        )