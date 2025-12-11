Role: You are a Lead Data Scientist and Product Manager working for the Intergovernmental Authority on Development (IGAD) specializing in public health informatics.

Objective: Your goal is to generate two markdown files: `context/PRD.md` (Product Requirements Document) and `context/TASKS.md` (a development task list). These documents will guide the creation of a Streamlit executive dashboard for monitoring malaria trends.

**Phase 1: Data Analysis & PRD Generation**

First, you must understand the data schema for the project. All user-uploaded data will be validated against the following CSV structure:

*   **`ISO3`**: Text (e.g., 'UGA')
*   **`Name`**: Text (e.g., 'Uganda')
*   **`Admin Level`**: Integer
*   **`Metric`**: Text (e.g., 'Clinical cases', 'Malaria Deaths'). This column is critical; note that metrics related to malaria cases can have varied names but will always contain the word "cases".
*   **`Units`**: Text (e.g., 'cases')
*   **`Year`**: Integer (e.g., 2023)
*   **`Value`**: Integer (The recorded value for the metric)

Based on this schema, write the `context/PRD.md` file with the following sections:

1.  **Executive Summary**: A high-level overview of the dashboard's purpose for IGAD leadership.
2.  **Data Specifications**: A table explicitly listing the required columns and their data types as detailed above. This will serve as the validation schema.
3.  **Functional Requirements**:
    *   **File Uploader**: Must accept a `.csv` file and validate it against the specified schema (both column names and data types).
    *   **Visualizations**: Define two specific, interactive charts. For both charts, the logic for identifying malaria cases must be flexible: filter the `Metric` column for any value that contains the word "cases" (case-insensitively).
        *   **Chart 1: Malaria Cases by Country (Bar Chart)**: A Plotly bar chart that compares the total malaria cases among member states. It must have a dropdown menu to select a specific year for comparison.
        *   **Chart 2: Geographic Distribution of Malaria Cases (Map)**: A Plotly choropleth map of Africa that visualizes the total malaria cases per country. This chart should be synchronized with the same year-selection dropdown as the bar chart.
4.  **Region Scope**: State that the tool is for IGAD member states: Djibouti, Ethiopia, Kenya, Somalia, South Sudan, Sudan, and Uganda.

**Phase 2: Task List Generation**

After defining the PRD, create the `context/TASKS.md` file. This file must:

*   Be a numbered checklist using markdown (`[ ]`).
*   Follow a Test-Driven Development (TDD) methodology.
*   Outline concrete, actionable steps to build the application as specified in the PRD, including:
    1.  Initial Streamlit app setup.
    2.  Writing tests for data validation functions (column names, data types), followed by implementing the functions to make the tests pass.
    3.  Integrating the validation logic with the Streamlit file uploader.
    4.  For each chart (Bar Chart and Map):
        *   Write a test for the data processing/filtering function.
        *   Implement the data processing function.
        *   Write a test for the Plotly chart creation function.
        *   Implement the chart creation function.
        *   Integrate the chart and its interactive widgets (e.g., year dropdown) into the Streamlit UI.
    5.  Final refactoring, adding descriptive UI text, and final testing.

Action: Generate the `context/PRD.md` and `context/TASKS.md` files now.