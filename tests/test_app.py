import pandas as pd
import pytest
import plotly.graph_objects as go
from utils import (
    validate_columns,
    validate_data_types,
    create_country_comparison_chart,
    create_choropleth_map,
)

def test_validate_columns_with_valid_data():
    """
    Tests that the validation function returns True for a DataFrame with the correct columns.
    """
    valid_data = pd.DataFrame({
        'ISO3': ['TST'],
        'Name': ['Testland'],
        'Admin Level': [0],
        'Metric': ['Malaria Cases'],
        'Units': ['cases'],
        'Year': [2023],
        'Value': [100]
    })
    
    assert validate_columns(valid_data) is True


def test_validate_columns_with_invalid_columns():
    """
    Tests that a ValueError is raised for a DataFrame with incorrect columns.
    """
    invalid_data = pd.DataFrame({
        'ISO3': ['TST'],
        'Name': ['Testland'],
        'Admin Level': [0],
        'Metric': ['Malaria Cases'],
        'Units': ['cases'],
        'Year': [2023],
        'Wrong Value Column': [100]  # Incorrect column name
    })

    with pytest.raises(ValueError):
        validate_columns(invalid_data)


def test_validate_data_types_with_invalid_data():
    """
    Tests that a ValueError is raised for a DataFrame with non-numeric data in numeric columns.
    """
    invalid_type_data = pd.DataFrame({
        'ISO3': ['TST'],
        'Name': ['Testland'],
        'Admin Level': [0],
        'Metric': ['Malaria Cases'],
        'Units': ['cases'],
        'Year': [2023],
        'Value': ['one hundred']  # Invalid string data
    })

    with pytest.raises(ValueError):
        validate_data_types(invalid_type_data)


def test_validate_data_types_with_valid_data():
    """
    Tests that the validation function returns True for a DataFrame with correct data types.
    """
    valid_data = pd.DataFrame({
        'ISO3': ['TST'],
        'Name': ['Testland'],
        'Admin Level': [0],
        'Metric': ['Malaria Cases'],
        'Units': ['cases'],
        'Year': [2023],
        'Value': [100]
    })
    assert validate_data_types(valid_data) is True




def test_create_country_comparison_chart():
    """
    Tests that the country comparison chart function returns a valid Plotly Figure.
    """
    source_data = pd.DataFrame({
        'Name': ['Uganda', 'Kenya'],
        'Metric': ['Malaria Cases', 'Malaria Cases'],
        'Year': [2023, 2023],
        'Value': [100, 150]
    })
    
    fig = create_country_comparison_chart(source_data, 2023)
    
    assert isinstance(fig, go.Figure)
    assert fig.layout.title.text == 'Total Malaria Cases by Country in 2023'
    assert fig.layout.xaxis.title.text == 'Country'
    assert fig.layout.yaxis.title.text == 'Total Malaria Cases'



def test_create_choropleth_map():
    """
    Tests that the choropleth map function returns a valid Plotly Figure.
    """
    source_data = pd.DataFrame({
        'ISO3': ['UGA', 'KEN'],
        'Name': ['Uganda', 'Kenya'],
        'Admin Level': [0, 0],
        'Metric': ['Malaria Cases', 'Clinical cases'],
        'Units': ['cases', 'cases'],
        'Year': [2023, 2023],
        'Value': [100, 150]
    })
    
    fig = create_choropleth_map(source_data, 2023)
    
    assert isinstance(fig, go.Figure)
    assert fig.layout.title.text == 'Geographic Distribution of Malaria Cases in 2023'
