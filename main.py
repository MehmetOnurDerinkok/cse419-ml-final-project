""" Main functionality including preprocessing, training and validation """
# builtin python module
import sys

# external 3rd party library
import pandas as pd

# project modules
from preprocessing import preprocess_train_data, preprocess_query_input_data
from training import train_model
from prediction import predict_credit_risk_for_query_inputs


def parse_csv(file_path: str, delimiter: str = ' ') -> pd.DataFrame:
    """
    Parses csv into a pd.DataFrame

    Args:
        file_path: str - file path to be parsed
        delimiter: str - csv delimiter

    Returns:
        pd.DataFrame
    """
    try:
        return pd.read_csv(file_path, delimiter=delimiter)
    except FileNotFoundError:
        return None


if __name__ == '__main__':
    TRAIN_DATA_FILE_PATH = 'data/south_german_credit.asc'
    QUERY_INPUT_FILE_PATH = 'data/query_input.asc'

    train_dataframe = parse_csv(TRAIN_DATA_FILE_PATH)
    query_input_dataframe = parse_csv(QUERY_INPUT_FILE_PATH)

    if any([
        train_dataframe is None,
        query_input_dataframe is None
    ]):
        sys.exit(
            'Did you already place raw and input files under `data/` directory? '
            'Please check README.md for more details.'
        )

    try:
        train_dataframe = preprocess_train_data(train_dataframe)
        query_input_dataframe = preprocess_query_input_data(query_input_dataframe)

        trained_model = train_model(train_dataframe)

        credit_risk_result_dataframe = predict_credit_risk_for_query_inputs(
            trained_model, query_input_dataframe
        )

        print('Credit Risk Result:')
        print(credit_risk_result_dataframe)
    except Exception as exc:
        sys.exit(f'Unpexpected Error! -> {exc}')
