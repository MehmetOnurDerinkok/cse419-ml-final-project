""" Preprocessing for raw file  """

import pandas as pd


CONSECUTIVE_COLUMNS = ('status', 'duration', 'credit_history', 'purpose', 'amount',
                       'savings', 'employment_duration', 'installment_rate',
                       'personal_status_sex', 'other_debtors',
                       'present_residence', 'property',
                       'age', 'other_installment_plans',
                       'housing', 'number_credits',
                       'job', 'people_liable', 'telephone', 'foreign_worker',
                       'credit_risk')


def parse_csv(file_path: str, delimiter: str = ' ') -> pd.DataFrame:
    """
    Parses csv into a pd.DataFrame

    Args:
        file_path: str - file path to be parsed

    Returns:
        pd.DataFrame
    """
    try:
        raw_df = pd.read_csv(file_path, delimiter=delimiter)
        raw_df.columns = CONSECUTIVE_COLUMNS
        return raw_df
    except FileNotFoundError:
        return None


def normalize_df(raw_df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalizes df based on given conditions

    Args:
        raw_df: pd.DataFrame - raw dataframe to be normalized

    Returns:
        pd.DataFrame
    """
    return raw_df


def preprocess_file(file_path: str) -> pd.DataFrame:
    """
    Parses and normalizes csv content at file_path

    Args:
        file_path: str - file path to be processed

    Returns:
        Parsed and normalized pd.DataFrame
    """

    raw_df = parse_csv(file_path)
    if raw_df is not None:
        normalized_df = normalize_df(raw_df)
        return normalized_df

    return raw_df
