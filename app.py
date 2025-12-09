import streamlit as st
import pandas as pd

from utils import (
    validate_columns,
    validate_data_types,
    create_country_comparison_chart,
    create_choropleth_map,
)

def handle_uploaded_file(uploaded_file):
    """
    Handles the uploaded file by validating and displaying visualizations.
    
    Args:
        uploaded_file: The uploaded file object from Streamlit.
    """
    try:
        df = pd.read_csv(uploaded_file)
        validate_columns(df)
        validate_data_types(df)

        st.success("File uploaded and validated successfully!")
        
        # Chart 1: Country Comparison
        st.subheader("Chart 1: Malaria Cases by Country for a Specific Year")
        year_list = sorted(df['Year'].unique(), reverse=True)
        if year_list:
            selected_year = st.selectbox(
                "Select a year for comparison:",
                year_list
            )
            if selected_year:
                comparison_chart = create_country_comparison_chart(df, selected_year)
                st.plotly_chart(comparison_chart, use_container_width=True)
        else:
            st.warning("No years available in the data for comparison.")

        st.divider()

        # Chart 2: Geographic Distribution Map
        st.subheader("Chart 2: Geographic Distribution of Malaria Cases")
        if year_list:
            if selected_year:
                map_chart = create_choropleth_map(df, selected_year)
                st.plotly_chart(map_chart, use_container_width=True)
        else:
            st.warning("No years available in the data for map.")

    except ValueError as e:
        st.error(f"Data validation failed: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")


def main():
    """
    Main function to run the Streamlit application.
    """
    st.set_page_config(
        page_title="IGAD Malaria Executive Dashboard",
        page_icon="📊",
        layout="wide"
    )

    st.title("IGAD Malaria Executive Dashboard")
    st.subheader("Monitor malaria trends across IGAD member states")

    st.sidebar.header("Data Upload")
    uploaded_file = st.sidebar.file_uploader(
        "Upload your data in CSV format.",
        type=['csv'],
        help="The CSV file must contain the following columns: ISO3, Name, Admin Level, Metric, Units, Year, Value."
    )
    
    st.header("Dashboard Visualizations")

    if uploaded_file is not None:
        handle_uploaded_file(uploaded_file)
    else:
        st.info("Please upload a CSV file through the sidebar to view the dashboard.")


if __name__ == "__main__":
    main()
