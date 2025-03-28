from agno.agent import Agent, RunResponse
from agno.models.together import Together
from agno.tools.googlesearch import GoogleSearchTools
from agno.utils.pprint import pprint_run_response
from dotenv import load_dotenv
import os

load_dotenv()

# Define the university search agent
university_search_agent = Agent(
    name="university-search-agent",
    model=Together(id="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free", api_key=os.getenv("TOGETHER_API_KEY")), 
    tools=[GoogleSearchTools()],
    description=
    '''
        You are a university search agent that will search for the top universities based on a given discipline from top university ranking websites.
        You will generate a list of universities with their names, rankings, and official website links based on the given preferences.
    ''',
    instructions=[
        "Search the following university ranking websites one by one based on the given preferences:",
        "Preferences include discipline, education level, location, and maximum number of universities.",
            "US News Rankings: https://www.usnews.com",
            "QS Rankings: https://www.topuniversities.com",
            "Times Higher Education Rankings: https://www.timeshighereducation.com",
        "If the location is not specified, consider all locations.",
        "Search for the best universities for the given discipline and education level from each ranking website.",
        "The rankings MUST be according to the latest information available on the ranking websites",
        "Select the top ranked universities from the extracted information from each ranking website.",
        "The response MUST be in the following JSON format:",
            "{",
                '"universities": [',
                    '"https://university1.com",',
                    '"https://university2.com",',
                    '"https://university3.com",',
                    '"https://university4.com",',
                    '"https://university5.com",',
                "]",
                '"discipline": [DISCIPLINE],',
                '"education_level": [EDUCATION_LEVEL],',
            "}",
        "The response MUST NOT include ranking websites as universities.",
        "The response MUST only include top universities found from the ranking websites.",
        "The response MUST be in proper JSON format with keys and values in double quotes.",
        "The final response MUST not include any other text or anything else other than the JSON response."
    ],
    markdown=True,
    show_tool_calls=True,
    debug_mode=True
)
