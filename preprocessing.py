""" Preprocessing functionalities for csv files  """
from typing import Dict

import pandas as pd

from config import NORMALIZATION_MAPPING, ENGLISH_COLUMN_NAMES, ENGLISH_COLUMN_NAMES_USER_INPUTS


def translate_columns_into_english(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    replaces original `german` column names with their counterparts based on documentation.
    Documentation file is ./data/code_table.txt

    Args:
        dataframe: raw dateframe that their columns will be translated into english

    Returns:
        pd.DataFrame
    """
    try:
        dataframe.columns = ENGLISH_COLUMN_NAMES
        return dataframe
    except Exception as ex:
        raise Exception(
            'Columns could not be translated to english ones. Data is inconsistent.'
        ) from ex


def drop_column(column_name: str, dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Drops regarding column from dataframe

    Args:
        column_name: regarding column name to be dropped
        dataframe: pd.DataFrame - dataframe to be dropped from

    Returns:
        pd.DataFrame
    """
    try:
        dataframe.drop(column_name, axis=1, inplace=True)
        return dataframe
    except NameError as ex:
        raise Exception(
            f'Column[{column_name}] could not be found. Data is inconsistent.'
        ) from ex


def replace_column_based_on_value_mapping(
    dataframe: pd.DataFrame, column: str, replace_with: bool, value_mapping: Dict
) -> pd.DataFrame:
    """
    Adds new column based on value_mapping. It basically checks value_mapping to find counterpart
    of of an original value and put new value under new column

    Args:
        dataframe: original dataframe
        column: original column
        replace_with: new column based on `column` and value_mapping
        value_mapping: original-new value mapping

    Returns:
        Updated dataframe.
    """
    dataframe[replace_with] = dataframe[column].map(value_mapping)
    return dataframe


def preprocess_train_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    preprocess dataframe for all sort of dataframes related to this project

    Args:
        dataframe: pd.DataFrame

    Returns:
        preprocessed pd.DataFrame
    """

    # normally, dataframe columns are in german, we need to translate it into english ones
    dataframe = translate_columns_into_english(dataframe)

    # Scale new attributes and delete redundant columns based on NORMALIZATION_MAPPING
    for column, config in NORMALIZATION_MAPPING.items():
        use_as_is = config['use_as_is']
        if use_as_is:
            continue

        delete = config['delete']
        replace_with = config['replace_with']

        value_mapping = config['value_mapping']

        if replace_with:
            dataframe = replace_column_based_on_value_mapping(
                dataframe, column, replace_with, value_mapping
            )

        if delete:
            dataframe = drop_column(column, dataframe)

    return dataframe


def preprocess_user_input_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    replaces original `german` column names with their counterparts based on documentation.
    Documentation file is ./data/code_table.txt

    Args:
        dataframe: raw dateframe that their columns will be translated into english

    Returns:
        pd.DataFrame
    """
    try:
        dataframe.columns = ENGLISH_COLUMN_NAMES_USER_INPUTS

        # Scale new attributes and delete redundant columns based on NORMALIZATION_MAPPING
        for column, config in NORMALIZATION_MAPPING.items():
            use_as_is = config['use_as_is']
            if use_as_is:
                continue

            delete = config['delete']
            replace_with = config['replace_with']

            value_mapping = config['value_mapping']

            if replace_with:
                dataframe = replace_column_based_on_value_mapping(
                    dataframe, column, replace_with, value_mapping
                )

            if delete:
                dataframe = drop_column(column, dataframe)

        return dataframe
    except Exception as ex:
        raise Exception(
            'Columns could not be translated to english ones. Data is inconsistent.'
        ) from ex

    return dataframe
