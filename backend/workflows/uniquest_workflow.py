from agno.agent import Agent
from agno.workflow import Workflow, RunResponse, RunEvent
from agno.storage.workflow.sqlite import SqliteWorkflowStorage
from agno.utils.pprint import pprint_run_response
from agno.utils.log import logger
import json

from agents.university_search_agent import university_search_agent
from agents.program_search_agent import program_search_agent
from agents.information_extraction_agent import info_extraction_agent
from agents.information_processing_agent import info_processing_agent


class UniquestWorkflow(Workflow):
    university_search_agent: Agent = university_search_agent
    program_search_agent: Agent = program_search_agent
    info_extraction_agent: Agent = info_extraction_agent
    info_processing_agent: Agent = info_processing_agent

    def run(self, discipline: str, education_level: str, location: str, max_universities: int = 5) -> RunResponse:
        logger.info(f"Generating a list of top {max_universities} universities for a {education_level} in {discipline}")

        # Step 1: Generate a list of top universities for the given education level, discipline and location
        prompt = f"Search for {max_universities} top universities for a {education_level} in {discipline} based in {location}."
        top_universities: RunResponse = self.university_search_agent.run(prompt)
        # If no universities are found, end the workflow
        if top_universities is None:
            return RunResponse(
                event=RunEvent.workflow_completed,
                content=f"Sorry, could not find any universities for {education_level} in {discipline}",
            )
       
        print("Top universities:", top_universities.content)

        # Step 2: Find the admission and program links for each university
        prompt = f"Search for the admission and program page links for a {education_level} in {discipline} for the following universities: {top_universities.content}"
        links: RunResponse = self.program_search_agent.run(prompt)
        if links is None:
            return RunResponse(
                event=RunEvent.workflow_completed,
                content="Sorry, could not find the admission and program links for the universities.",
            )
        
        print("Links:", links.content)
       
        links_content = json.loads(links.content)
        links = links_content["links"]

        # Step 3: Extract the information from each admission and program link for each university
        information = []
        for link in links:
            logger.info(f"Extracting information for {link['university']}")

            # Initialize with default values
            admission_info_content = "No information found"
            program_info_content = "No information found"

            try:
                prompt = f"Search for the admission and program related information of {link["university"]} from the following link: {link['admission']}."
                admission_info: RunResponse = self.info_extraction_agent.run(prompt)
                admission_info_content = admission_info.content
            except Exception as e:
                logger.error(f"Error extracting admission information for {link['university']}: {e}")
            
            try:
                prompt = f"Search for the admission and program related information of {link['university']} from the following link: {link['program']}."
                program_info: RunResponse = self.info_extraction_agent.run(prompt)
                program_info_content = program_info.content
            except Exception as e:
                logger.error(f"Error extracting program information for {link['university']}: {e}")

            information.append({"university":link["university"], "admission_info": admission_info_content, "program_info": program_info_content})

        print("Information:", information)

        # Step 4: Process the information and structure it in JSON format.
        prompt = f"Process the following information: {information}"
        processed_info: RunResponse = info_processing_agent.run(prompt)
        if processed_info is None:
            return RunResponse(
                event=RunEvent.workflow_completed,
                content="Sorry, could not process the information.",
            )

        print("Processed information:", processed_info.content)

        return RunResponse(
            event=RunEvent.workflow_completed,
            content={"universities": top_universities.content, "links": links, "information": information, "processed_info": processed_info.content},
        )
    
# Initialize the Uniquest workflow
uniquest_workflow = UniquestWorkflow(
        session_id="find-top-universities",
        storage=SqliteWorkflowStorage(
            table_name="generate_uniquest_workflows",
            db_file="workflows/db/workflows.db",
        ),
    )
