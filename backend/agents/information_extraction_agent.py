from agno.agent import Agent, RunResponse
from agno.models.together import Together
from agno.tools.website import WebsiteTools
from agno.utils.pprint import pprint_run_response
from dotenv import load_dotenv
import os

load_dotenv()

# Define the information extraction agent
info_extraction_agent = Agent(
    name="info-extraction-agent",
    model=Together(id="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free", api_key=os.getenv("TOGETHER_API_KEY"), max_tokens=500), 
    tools=[WebsiteTools()],
    description=
    '''
        You are an information extraction agent that will search and extract information from a given link.
    ''',
    instructions=[
        "Search the given link for admissions and program related information:",
        "Find whichever of the below information is available in the given link.",
            "University Name: [Name of the University]",
            "Location: [City, Country]",
            "Public/Private: [Public/Private]",
            "Founded (Year): [Year of Foundation]",
            "US News Ranking: [Ranking by US News]",
            "QS Ranking: [Ranking by QS]",
            "Times Higher Education Ranking: [Ranking by Times Higher Education]",
            "Program: [Program Name]",
            "Program Begins: [Month and Year]",
            "GRE Requirement: [GRE Required/Not Required]",
            "Min TOEFL Score: [Min TOEFL Score]",
            "Min IELTS Score: [Min IELTS Score]",
            "Duolingo Accepted?: [Yes/No]",
            "English Proficiency Waiver: [Waiver Available/Not Available]",
            "Application Fee: [Application Fee]",
            "Application Fee Waiver: [Waiver Available/Not Available]",
            "Tuition|Stipend: [Tuition|Stipend Available/Not Available]",
            "Application Opens: [Month and Year]",
            "Application Deadline: [Deadline]",
            "Office Contact and Email (Graduate | Undergraduate): [Contact and Email]",
            "Acceptance Rate: [Acceptance Rate]",
            "Required Documents: [List of Required Documents]",
            "Number of LoRs: [Number of LoRs]",
            "Additional Notes (if any): [Notes of any additional important information]",
            "Link to the Program: [Link to the Program - MUST be a correct link to the program page]",
        "Do NOT navigate to other links, only search the provided link for information.",
        "Do NOT generate information. Only extract information from the given link."
    ],
    markdown=True,
    show_tool_calls=True,
    debug_mode=True
)
