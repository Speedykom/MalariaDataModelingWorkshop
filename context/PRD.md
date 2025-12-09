# Product Requirements Document: IGAD Malaria Executive Dashboard

## 1. Executive Summary

This document outlines the requirements for the IGAD Malaria Executive Dashboard, a web-based tool designed for public health leadership and policymakers within IGAD member states. The primary objective is to provide a high-level, interactive interface for monitoring malaria trends, enabling data-driven decision-making for resource allocation, and strengthening regional public health interventions. The dashboard will be developed as a Streamlit application for ease of use and rapid deployment.

## 2. Data Specifications

The dashboard will process CSV files containing malaria surveillance data. Based on an analysis of the provided dataset (`dj_et_ke_so_ss_sd_ug_NationalUnit-data.csv`), all user-uploaded data must adhere to the following schema for validation and processing.

| Column Name      | Data Type | Description                                        |
|------------------|-----------|----------------------------------------------------|
| `Country`        | Text      | The full name of the country.                      |
| `ISO3`           | Text      | The 3-letter ISO code for the country (e.g., 'UGA'). |
| `Year`           | Integer   | The year of the record (e.g., 2023).               |
| `Month`          | Integer   | The month of the record (1-12).                    |
| `Malaria Cases`  | Integer   | The number of confirmed malaria cases reported.    |
| `Malaria Deaths` | Integer   | The number of deaths attributed to malaria.        |
| `Population`     | Integer   | The estimated population for the region.           |

## 3. Functional Requirements

### 3.1. File Uploader

- **Component**: The application must feature a file uploader widget.
- **Accepted Format**: CSV (`.csv`).
- **Validation**:
    - The application must validate that any uploaded file contains exactly the columns specified in the Data Specifications section.
    - Column data types must be validated (e.g., `Year`, `Month`, `Malaria Cases`, `Malaria Deaths`, and `Population` must be numeric).
    - If validation fails, a clear and descriptive error message must be displayed to the user, guiding them to correct the format.

### 3.2. Visualizations

The dashboard will feature the following interactive visualizations, built using Streamlit and Plotly, to provide actionable insights.

#### Chart 1: Malaria Cases Trend
- **Type**: Multi-line chart.
- **Description**: Displays the trend of reported malaria cases over time.
- **X-Axis**: Time, aggregated by `Year` and `Month`.
- **Y-Axis**: Total number of `Malaria Cases`.
- **Interactivity**: A multi-select dropdown to filter and compare trends for specific countries.

#### Chart 2: Geographic Distribution of Malaria Deaths
- **Type**: Choropleth map.
- **Description**: Visualizes the total number of malaria deaths across the IGAD region.
- **Data**: Aggregated `Malaria Deaths` per country.
- **Interactivity**:
    - A date-range slider to filter the data for a specific period.
    - Hover-over tooltips displaying the country name and the total death count for the selected period.

#### Chart 3: Malaria Incidence Rate by Country
- **Type**: Bar chart.
- **Description**: Compares the malaria incidence rate (cases per 1,000 population) among member states.
- **Calculation**: Incidence Rate = (`Total Malaria Cases` / `Total Population`) * 1000.
- **X-Axis**: Country.
- **Y-Axis**: Calculated Incidence Rate.
- **Interactivity**: A dropdown menu to select a specific year for comparison.

### 3.3. Region Scope

The tool is exclusively designed to support the public health informatics needs of the Intergovernmental Authority on Development (IGAD) member states:
- Djibouti
- Ethiopia
- Kenya
- Somalia
- South Sudan
- Sudan
- Uganda
