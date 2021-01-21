"""
Prediction related functionalities
"""
from typing import Any

import pandas as pd


def predict_credit_risk_for_query_inputs(
    model: Any, query_input_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Predicts credit_risk based on previously trained model and query inputs

    Args:
        model: Trained model function
        query_inputs
    """
    return model.predict(query_input_dataframe)
