from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
import logging

from utils.prompts import create_sql_prompt_template
from utils.engine import chat

# Initialize FastAPI application
app = FastAPI()

# Set up Jinja2 template directory for rendering HTML pages
templates = Jinja2Templates(directory="templates")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the Pydantic model for incoming prompt data
class Prompt(BaseModel):
    user_prompt: str = Field(..., example="Select all records from the hotels table where the city is 'Paris'.")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Render the root HTML page.

    Args:
        request (Request): The HTTP request object.

    Returns:
        HTMLResponse: The rendered HTML template for the root page.
    """
    logger.info("Rendering root page.")
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate")
async def generate_sql_query(prompt: Prompt):
    """
    Generate SQL query based on user prompt.

    Args:
        prompt (Prompt): The Pydantic model containing user prompt data.

    Returns:
        JSONResponse: The generated SQL query.
    
    Raises:
        HTTPException: If the SQL generation fails for any reason.
    """
    logger.info(f"Received prompt: {prompt.user_prompt}")
    
    try:
        # Create SQL prompt template
        sql_prompt_template = create_sql_prompt_template(prompt.user_prompt)

        # Generate SQL query using the chat engine
        generated_query = chat(sql_prompt_template)

        logger.info(f"Generated SQL Query: {generated_query}")

        return JSONResponse(content={"sql_query": generated_query})

    except Exception as e:
        logger.error(f"Error generating SQL query: {str(e)}")
        raise HTTPException(status_code=500, detail="An error occurred while generating the SQL query.")

@app.get("/healthcheck")
async def healthcheck():
    """
    Simple health check endpoint.

    Returns:
        JSONResponse: A health check message.
    """
    logger.info("Health check called.")
    return JSONResponse(content={"status": "healthy"})

if __name__ == "__main__":
    import uvicorn
    # Start the FastAPI application with Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
