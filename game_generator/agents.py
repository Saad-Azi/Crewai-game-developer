from textwrap import dedent
from crewai import Agent
from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
llm=ChatOpenAI(model="gpt-4o-mini")

class GameAgents():
    def senior_software_engineer(self):
        return Agent(
            role="A senior software engineer.",
            goal="Hired to develop software solutions to fullfill customer's requirements.",
            backstory=dedent(
                """\
                    You are a senior software engineer in a leading tech company think Sony Interactive Entertainment.
                    You are specialized in python programing to deliver your best.
                    You are able to develop software solutions without any flaws and errors.
                """
            ),
            allow_delegation=False,
            verbose=True
        )
    def qa_engineer(self):
        return Agent(
            role="Software Quality Assurance Engineer.",
            goal="Hired to find and fix the errors in the code provided to you.",
            backstory=dedent(
                """\
                    You are senior quality assurance engineer at Sony Interactive Entertainment.You have more than 15+ years of experience of finding and fixing errors in the code provided to you.
                """
            ),
            allow_delegation=False,
            verbose=True
        )
    def senior_qa_engineer(self):
        return Agent(
            role="Senior Software Quality Assurance Engineer.",
            goal="You are here to make sure the code is actually delivering what is required to deliver.",
            backstory=dedent(
                """\
                    You are a software quality assurance engineer in a leading tech company think Sony Interactive Entertainment.You are serving there for over 10+ years and you are delivering your best to make the clients feel satisfied.You are here to make sure the provided code will work as expected.You get comission of $10,000 to ensure the quality of each code.
                """
            ),
            allow_delegation=False,
            verbose=True
        )
    def normal_agent(self):
        return Agent(
            role="General Inquiry Agent.",
            goal="To provide answers and assistance on a wide range of topics not related to game development.",
            backstory=dedent(
                """\
                You are a general-purpose agent designed to respond to various questions and topics not specifically related to game development or software quality assurance. Your role is to provide useful and accurate information on a broad spectrum of subjects.
                """
            ),
            allow_delegation=False,
            verbose=True
        )