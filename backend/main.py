from fastapi import FastAPI
from pydantic import BaseModel

from agno.agent import RunResponse
from workflows.uniquest_workflow import uniquest_workflow
from utils import save_info_to_excel

app = FastAPI()

class SearchRequest(BaseModel):
    discipline: str
    education_level: str
    location: str
    max_universities: int = 5

@app.post("/search/")
async def search_universities(request: SearchRequest):
    # Execute the workflow
    # Returns a RunResponse object containing the generated content
    response: RunResponse = uniquest_workflow.run(discipline=request.discipline, education_level=request.education_level, location=request.location, max_universities=request.max_universities)

    if response:
        print("Response:", response.content)
         
        # Save the universities info to an Excel file
        excel_path = save_info_to_excel(response.content["processed_info"], request.discipline, request.education_level, request.location)
        return {"message": "Top universities found!", "response": response.content, "excel_path": excel_path}
    else:
        return {"error": "No universities found"}
