from langchain_core.prompts import PromptTemplate

base_template = """
You are an SQL query generator. Generate an SQL query based on the following user prompt. 

**User Prompt**: {description}

### Instructions for SQL Generation:
1. **Understand the Request**: Analyze the user prompt for SQL-related content.
2. **Generate SQL Query**: Create a SQL query that corresponds to the user's request.
3. **Output**: Format the SQL query properly and return it.

"""


def create_sql_prompt_template(description, table_name=None, table_structure=None):
    # Set up table structure text if provided, otherwise leave it blank
    table_section = (
        f"**Table Structure**:\n- Table: {table_name}\n  - Columns: {table_structure}\n"
        if table_name and table_structure else ""
    )
    
    # Create the final prompt template
    prompt_template = PromptTemplate(
        input_variables=["description", "table_section"],
        template=base_template
    )
    
    # Format the prompt with the description and optional table section
    return prompt_template.format(description=description, table_section=table_section)

