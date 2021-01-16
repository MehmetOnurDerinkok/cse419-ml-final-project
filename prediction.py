"""
Prediction related functionalities
"""
from typing import Callable

import pandas as pd


def predict_credit_risk_for_query_inputs(
    model: Callable, query_input_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Predicts credit_risk based on previously trained model and query inputs

    Args:
        model: Trained model function
        query_inputs
    """
    query_input_dataframe['credit_risk'] = query_input_dataframe.apply(model)
    return query_input_dataframe
