# Import necessary modules from langchain_core
from langchain_core.prompts import PromptTemplate

# Base template for SQL query generation
base_template = """
You are an SQL query generator. Generate an SQL query based on the following user prompt. 

**User Prompt**: {description}

### Instructions for SQL Generation:
1. **Understand the Request**: Analyze the user prompt for SQL-related content.
2. **Generate SQL Query**: Create a SQL query that corresponds to the user's request.
3. **Output**: Format the SQL query properly and return it only code.

**Note**: Don't add any comments or extra information in the SQL query.
"""

def create_sql_prompt_template(description, table_name=None, table_structure=None):
    """
    Create a prompt template for SQL query generation.

    Args:
        description (str): The user's request description that guides SQL query generation.
        table_name (str, optional): The name of the table involved in the SQL query. Defaults to None.
        table_structure (str, optional): A string representation of the table's columns and types. Defaults to None.

    Returns:
        str: A formatted prompt string ready for the SQL query generator.
    """

    # Initialize a variable to hold the table structure section of the prompt
    table_section = ""

    # Set up table structure text if provided, otherwise leave it blank
    if table_name and table_structure:
        table_section = (
            f"**Table Structure**:\n- Table: {table_name}\n  - Columns: {table_structure}\n"
        )

    # Log the creation of the prompt template
    print("Creating SQL prompt template...")

    # Create the final prompt template using the PromptTemplate class
    prompt_template = PromptTemplate(
        input_variables=["description", "table_section"],
        template=base_template
    )

    # Log the prompt creation with provided inputs
    print(f"Prompt created with description: {description} and table section: {table_section}")

    # Format the prompt with the description and optional table section
    formatted_prompt = prompt_template.format(description=description, table_section=table_section)

    # Log the final formatted prompt for debugging
    print("Final formatted prompt:", formatted_prompt)

    return formatted_prompt


# Example usage of the function to demonstrate its functionality
if __name__ == "__main__":
    # User input for SQL query generation
    user_description = "Select all records from the hotels table where the city is 'Paris'."
    user_table_name = "hotels"
    user_table_structure = "hotel_id INT, name VARCHAR(255), address VARCHAR(255), city VARCHAR(100), country VARCHAR(50)"

    # Call the function to create the SQL prompt template
    sql_prompt = create_sql_prompt_template(
        description=user_description,
        table_name=user_table_name,
        table_structure=user_table_structure
    )

    # Print the generated SQL prompt for the user
    print("\nGenerated SQL Prompt Template:\n")
    print(sql_prompt)

    # Additional comments or explanations can be added here if needed
    print("\n**Note**: Use the generated SQL prompt to interact with the SQL query generator.")
