from agno.agent import Agent, RunResponse
from agno.models.together import Together
from agno.tools.googlesearch import GoogleSearchTools
from agno.utils.pprint import pprint_run_response
from dotenv import load_dotenv
import os

load_dotenv()

# Define the link browsing agent
program_search_agent = Agent(
    name="program-search-agent",
    model=Together(id="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free", api_key=os.getenv("TOGETHER_API_KEY")), 
    tools=[GoogleSearchTools()],
    description=
    '''
        You are a program search agent that will search for the admission and program page links for a given list of universities based on the given preferences.
        You will generate a list of universities with their admission and program page links in JSON format.
    ''',
    instructions=[
        "Search the given university websites one by one based on the given preferences",
        "For each university, search for the admission page link based on the given education level.",
        "For each university, search for the program page link based on the given discipline and education level.",
        "Do NOT generate links. Instead, search them directly from the official university website.",
        "The links MUST depict the latest admissions and program information available on the university website.",
        "Do NOT retrieve links having old or outdated admissions and program information.",
        "If you don't find a specific program in a university, search for the most similar or closest related program page link.",
        "Validate the links by ensuring they do NOT return 404 errors or redirects to unrelated pages.",
        "Double-check that the links are correct and functional.",
        "The response MUST be in the following JSON format:",
        "{"
        "    'links': [",
        "       {",
        "           'university': '[Official website link]',",
        "           'admission': '[Admission page link]',",
        "           'program': '[Program page link]'",
        "       }",
        "       {...}",
        "    ]",
        "}",
        "The response MUST be in proper JSON format with keys and values in double quotes.",
        "The final response MUST not include any other text or anything else other than the JSON response."
    ],
    markdown=True,
    show_tool_calls=True,
    debug_mode=True
)
