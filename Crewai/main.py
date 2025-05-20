from fastapi import FastAPI, UploadFile, File
from dotenv import load_dotenv
import os
import pandas as pd
from crew import run_csv_crew

load_dotenv()
app = FastAPI()

@app.post("/run-agents")
async def run_agents(file: UploadFile = File(...)):
    os.makedirs("temp", exist_ok=True)
    file_path = f"temp/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    df = pd.read_csv(file_path)
    sample_data = df.head(10).to_string(index=False)

    result = run_csv_crew(sample_data)
    return {"response": result}
