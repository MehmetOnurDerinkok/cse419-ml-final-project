""" Main functionality including preprocessing, training and validation """
# builtin python module
import sys
from typing import List
from copy import deepcopy

# external 3rd party library
import pandas as pd

# project modules
from preprocessing import preprocess_train_data, preprocess_user_input_data
from training import train_model
from prediction import predict_credit_risk_for_query_inputs
from utils import colored


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
        dataframe = pd.read_csv(file_path, delimiter=delimiter)
        dataframe.reset_index(drop=True, inplace=True)
        return dataframe
    except FileNotFoundError:
        return None


def prepare_input_dataframe():
    """
    get user inputs and returns a dataframe
    """
    inputs = {
        'laufkont': ([1, 2, 3, 4], "any integer between 1 - 4"),
        'laufzeit': (range(100), "any integer between 0 - 100"),
        'moral': ([0, 1, 2, 3, 4], "any integer between 0 - 4"),
        'verw': ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "any integer between 0 - 10"),
        'hoehe': (range(1000, 50000), "any integer between 1000 - 50000"),
        'sparkont': ([1, 2, 3, 4, 5], "any integer between 1 - 5"),
        'beszeit': ([1, 2, 3, 4, 5], "any integer between 1 - 5"),
        'rate': ([1, 2, 3, 4], "any integer between 1 - 4"),
        'famges': ([1, 2, 3, 4], "any integer between 1 - 4"),
        'buerge': ([1, 2, 3], "any integer between 1 - 3"),
        'wohnzeit': ([1, 2, 3, 4], "any integer between 1 - 4"),
        'verm': ([1, 2, 3, 4], "any integer between 1 - 4"),
        'alter': (range(100), "any integer between 0 - 100"),
        'weitkred': ([1, 2, 3], "any integer between 1 - 3"),
        'wohn': ([1, 2, 3], "any integer between 1 - 3"),
        'bishkred': ([1, 2, 3, 4], "any integer between 1 - 4"),
        'beruf': ([1, 2, 3, 4], "any integer between 1 - 4"),
        'pers': ([1, 2], "any integer between 1 - 2"),
        'telef': ([1, 2], "any integer between 1 - 2"),
        'gastarb': ([1, 2], "any integer between 1 - 2"),
    }

    frame = deepcopy(inputs)
    for column, infos in inputs.items():
        while True:
            valids, desc = infos
            text = f'Please provide "{column}" - {desc}\n'

            try:
                val = int(input(text))
            except:
                val = -1

            if val in valids:
                break
        frame[column] = val

    return pd.DataFrame([frame])


def print_inputs_and_predictions(dataframe: pd.DataFrame, prediction_results: List[int]):
    """
    Pretty prints inputs and predictions
    """
    for index, row in dataframe.iterrows():
        print(colored('## INPUTS:', 'blue'))
        print(row)
        prediction = prediction_results[index]
        r_color = 'green' if prediction == 1 else 'red'
        print(colored('## credit_risk PREDICTION:', 'blue'), colored(prediction, r_color))
        print('\n')


if __name__ == '__main__':
    TRAIN_DATA_FILE_PATH = 'data/south_german_credit.asc'
    train_dataframe = parse_csv(TRAIN_DATA_FILE_PATH)

    if train_dataframe is None:
        sys.exit(
            'Did you already place raw and input files under `data/` directory? '
            'Please check README.md for more details.'
        )

    try:
        train_dataframe = preprocess_train_data(train_dataframe)
        trained_model = train_model(train_dataframe)

        # get inputs here and create dataframe
        query_input_dataframe = prepare_input_dataframe()
        query_input_dataframe = preprocess_user_input_data(query_input_dataframe)
        predictions = predict_credit_risk_for_query_inputs(
            trained_model, query_input_dataframe
        )
        credit_risk = predictions[0]
        r_color = 'green' if credit_risk == 1 else 'red'
        credit_risk_colored = colored(credit_risk, r_color)

        print(f'PREDICTION for "credit_risk" is {credit_risk_colored}')
    except Exception as exc:
        sys.exit(f'Unpexpected Error! -> {exc}')
