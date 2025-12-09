# IGAD Malaria Dashboard: Development Tasks

**Note:** Always run the application using `uv run streamlit run app.py` to ensure you are in the correct virtual environment.

## Phase 1: Project Setup & Data Loading

1.  `[x]` Set up the basic Streamlit application structure with a title and placeholder sections for the dashboard components.
2.  `[x]` Write a test for a data validation function that checks for the required columns (`Country`, `ISO3`, `Year`, `Month`, `Malaria Cases`, `Malaria Deaths`, `Population`).
3.  `[x]` Implement the data validation function to pass the test with a valid CSV.
4.  `[x]` Write a test for the data validation function to handle incorrect column names and ensure it raises a specific error.
5.  `[x]` Update the validation function to handle incorrect column names.
6.  `[x]` Write a test for the data validation function to handle non-numeric data in numeric columns (`Year`, `Month`, `Malaria Cases`, `Malaria Deaths`, `Population`).
7.  `[x]` Update the validation function to handle data type errors.
8.  `[x]` Implement the Streamlit file uploader component, accepting only `.csv` files.
9.  `[x]` Integrate the data validation logic with the file uploader. Display a clear error message to the user if validation fails.

## Phase 2: Visualizations

### Chart 1: Malaria Cases Trend (Multi-Line Chart)

10. `[x]` Write a test for a data processing function that aggregates `Malaria Cases` by `Year` and `Month` for selected countries.
11. `[x]` Implement the data processing function.
12. `[x]` Write a function to generate a Plotly multi-line chart from the processed data.
13. `[x]` Write a test to verify that the chart function returns a valid Plotly Figure object with the correct axes.
14. `[x]` Implement the multi-select country filter and display the "Malaria Cases Trend" chart in the Streamlit app.

### Chart 2: Geographic Distribution of Malaria Deaths (Choropleth Map) - (Removed due to schema change)

15. `[ ]` ~~Write a test for a data processing function that filters data by a date range and aggregates total `Malaria Deaths` by country (`ISO3`).~~
16. `[ ]` ~~Implement the data filtering and aggregation function.~~
17. `[ ]` ~~Write a function to generate a Plotly choropleth map from the aggregated death data.~~
18. `[ ]` ~~Write a test to verify the map function returns a valid Plotly Figure object.~~
19. `[ ]` ~~Implement the date-range slider and display the choropleth map in the Streamlit app.~~

### Chart 3: Malaria Incidence Rate (Bar Chart) - (Removed due to schema change)

20. `[ ]` ~~Write a test for a function that calculates the malaria incidence rate per 1,000 population for a selected year. The test should cover the formula: (`Total Malaria Cases` / `Total Population`) * 1000.~~
21. `[ ]` ~~Implement the incidence rate calculation function.~~
22. `[ ]` ~~Write a function to generate a Plotly bar chart comparing incidence rates by country.~~
23. `[ ]` ~~Write a test to verify the bar chart function returns a valid Plotly Figure object with correct axes.~~
24. `[ ]` ~~Implement the year selection dropdown and display the "Malaria Incidence Rate" bar chart in the Streamlit app.~~

## Phase 3: Finalization

25. `[x]` Review and refactor code for clarity, performance, and adherence to best practices.
26. `[x]` Add descriptive titles, labels, and instructional text to all UI components to enhance usability.
27. `[x]` Final testing of the complete application workflow.
