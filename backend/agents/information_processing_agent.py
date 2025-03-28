from agno.agent import Agent, RunResponse
from agno.models.together import Together
from agno.utils.pprint import pprint_run_response
from dotenv import load_dotenv
import os

load_dotenv()

# Define the information processing agent
info_processing_agent = Agent(
    name="info-search-agent",
    model=Together(id="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free", api_key=os.getenv("TOGETHER_API_KEY")),
    description=
    '''
        You are an information processing agent that structures the information about universities' admissions and programs in JSON format. 
    ''',
    instructions=[
        "Structure the information received about universities' admissions and programs in JSON format.",
        "Important: Your final response MUST be in JSON format with the following structure:",
        "{"
            "universities: ["
                "{"
                "   'name': 'Name of the University',"
                "   'location': 'Location[City, Country] of the University',"
                "   'status': 'Public or Private',"
                "   'founded': 'Year of Foundation',"
                "   'us_news_ranking': 'Ranking by US News',"
                "   'qs_ranking': 'Ranking by QS',"
                "   'times_ranking': 'Ranking by Times Higher Education',"
                "   'program': 'Program Name',"
                "   'program_begins': 'Month and Year',"
                "   'gre_requirement': 'GRE Required/Not Required',"
                "   'toefl_score': 'Min TOEFL Score',"
                "   'ielts_score': 'Min IELTS Score',"
                "   'duolingo_accepted': 'Yes/No',"
                "   'english_proficiency_waiver': 'Waiver Available/Not Available',"
                "   'application_fee': 'Application Fee',"
                "   'application_fee_waiver': 'Waiver Available/Not Available',"
                "   'tuition_stipend': 'Tuition/Stipend Available/Not Available',"
                "   'application_opens': 'Month and Year',"
                "   'application_deadline': 'Deadline',"
                "   'office_contact_and_email': 'Contact and Email',"
                "   'acceptance_rate': 'Acceptance Rate',"
                "   'required_documents': 'List of Required Documents',"
                "   'number_of_lors': 'Number of LoRs',"
                "   'additional_notes': 'Notes of any additional important information',"
                "   'link': 'Link to the Program'"
                "},"
                "{...}"
            "]"
        "}",
         "The response MUST be in proper JSON format with keys and values in double quotes.",
        "The final response MUST not include anything else other than the JSON response."
    ],
    markdown=True,
    show_tool_calls=True,
    debug_mode=True
)