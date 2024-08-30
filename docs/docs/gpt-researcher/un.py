import asyncio

from fastapi import FastAPI

from gpt_researcher import GPTResearcher

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the GPT Researcher API"}

@app.get("/report/{report_type}")
async def get_report(query: str, report_type: str) -> dict:
    researcher = GPTResearcher(query, report_type)
    research_result = await researcher.conduct_research()
    report = await researcher.write_report()
    return {"report": report}

# Run the server