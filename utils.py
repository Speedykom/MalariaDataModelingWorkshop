import pandas as pd
import plotly.express as px

def validate_columns(df: pd.DataFrame) -> bool:
    """
    Validates that the uploaded DataFrame has the required columns.

    Args:
        df: The DataFrame to validate.

    Returns:
        True if columns are valid.

    Raises:
        ValueError: If columns are missing or incorrect.
    """
    REQUIRED_COLUMNS = {
        "ISO3",
        "Name",
        "Admin Level",
        "Metric",
        "Units",
        "Year",
        "Value",
    }

    uploaded_cols = set(df.columns)
    if uploaded_cols != REQUIRED_COLUMNS:
        missing = sorted(list(REQUIRED_COLUMNS - uploaded_cols))
        extra = sorted(list(uploaded_cols - REQUIRED_COLUMNS))
        
        error_message = "Column validation failed."
        if missing:
            error_message += f" Missing columns: {missing}."
        if extra:
            error_message += f" Extra columns: {extra}."
        raise ValueError(error_message)

    return True

def validate_data_types(df: pd.DataFrame) -> bool:
    """
    Validates that numeric columns can be cast to numeric types.

    Args:
        df: The DataFrame to validate.

    Returns:
        True if data types are valid.

    Raises:
        ValueError: If any numeric column contains non-numeric data.
    """
    NUMERIC_COLS = [
        "Year", "Value"
    ]
    
    errors = []
    for col in NUMERIC_COLS:
        if not pd.to_numeric(df[col], errors='coerce').notna().all():
            errors.append(col)
            
    if errors:
        raise ValueError(f"Non-numeric data found in columns: {errors}")
        
    return True


def create_country_comparison_chart(df: pd.DataFrame, year: int):
    """
    Creates a Plotly bar chart comparing total malaria cases by country for a given year.

    Args:
        df: The source DataFrame.
        year: The year to filter by.

    Returns:
        A Plotly Figure object.
    """
    # Filter for metrics containing 'cases', case-insensitively.
    df_cases = df[df['Metric'].str.contains('cases', case=False, na=False)].copy()
    df_year = df_cases[df_cases['Year'] == year]
    
    comparison_df = df_year.groupby('Name')[['Value']].sum().reset_index()
    
    fig = px.bar(
        comparison_df,
        x='Name',
        y='Value',
        title=f"Total Malaria Cases by Country in {year}"
    )
    fig.update_layout(
        xaxis_title="Country",
        yaxis_title="Total Malaria Cases"
    )
    return fig


def create_choropleth_map(df: pd.DataFrame, year: int):
    """
    Creates a Plotly choropleth map showing total malaria cases by country for a given year.

    Args:
        df: The source DataFrame.
        year: The year to filter by.

    Returns:
        A Plotly Figure object.
    """
    # Filter for metrics containing 'cases', case-insensitively.
    df_cases = df[df['Metric'].str.contains('cases', case=False, na=False)].copy()
    df_year = df_cases[df_cases['Year'] == year]
    
    map_df = df_year.groupby(['ISO3', 'Name'])['Value'].sum().reset_index()
    
    fig = px.choropleth(
        map_df,
        locations="ISO3",
        color="Value",
        hover_name="Name",
        color_continuous_scale=px.colors.sequential.Plasma,
        scope="africa",
        title=f"Geographic Distribution of Malaria Cases in {year}"
    )
    fig.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='mercator'
        )
    )
    return fig
