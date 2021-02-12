"""
Training related functionalities
"""
from typing import Any

import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, ShuffleSplit

from utils import colored


ALGORITHMS = [
    LogisticRegression,
    # svc: support vector machine
    LinearSVC,
    RandomForestClassifier,
]


def train_model(dataframe: pd.DataFrame):
    """
    Trains previous credit risk inputs and creates a model

    Args:
        dataframe: Proper dataframe inputs that contain proper credit risk related columns
    """

    inputs, outputs = get_inputs_and_outputs(dataframe)

    accuracies_and_deviations = []

    for Algorithm in ALGORITHMS:
        model = Algorithm()

        accuracy, std_deviation = calculate_accuracy_and_deviation_with_kfold(
            model, inputs, outputs
        )

        accuracies_and_deviations.append((model, accuracy, std_deviation))

    # we will find the best accuracy with the less standard deviation after sorting accuracies
    # DESC order
    accuracies_and_deviations = sorted(
        accuracies_and_deviations, key=lambda item: item[1], reverse=True
    )
    # get biggest value
    model, accuracy, std_deviation = accuracies_and_deviations[0]

    model_colored = colored(Algorithm, 'red')
    accuracy_colored = colored(round(accuracy, 2), 'red')
    deviation_colored = colored(round(std_deviation, 2), 'red')

    print(colored('###################', 'green'))
    print(colored(f'ALGORITHMS are {ALGORITHMS}\n\n', 'blue'))
    print(f'Picked this algorithm: {model_colored}.\n'
          f'Accuracy is {accuracy_colored}\n'
          f'Std Deviation is {deviation_colored}')
    print(colored('###################', 'green'))

    # train selected model with the original inputs
    return model.fit(inputs, outputs)


def get_inputs_and_outputs(dataframe: pd.DataFrame):
    """
    Returns explanatory variables and regarding credit_risk column separated
    """
    # vector of the response: real result -> 0 or 1
    outputs = dataframe['credit_risk']

    # matrix of explanatory variables: inputs while predicting
    dataframe.drop('credit_risk', axis=1, inplace=True)
    inputs = dataframe

    return inputs, outputs


def calculate_accuracy_and_deviation_with_kfold(
        model: Any, inputs: pd.DataFrame, outputs: pd.Series
):
    """
    Applies k-fold into dataframe and calculates avg accuracy for model
    """
    # randomly splits data into 10 chunks
    # in each chunk, 70% is for training, 30% is for testing purposes
    cross_validation = ShuffleSplit(n_splits=10, test_size=0.3, random_state=0)

    accuracies = cross_val_score(model, inputs, outputs, cv=cross_validation)

    avg_accuracy = accuracies.mean()
    std_deviation = accuracies.std()

    accuracies_as_list = [round(accuracy, 2) for accuracy in accuracies.tolist()]
    print('\n')
    print(colored('###################', 'blue'))
    print(colored('Cross validation accuracy results for {}:'.format(str(model)), 'green'))
    print(colored(accuracies_as_list, 'green'))
    print(colored('Avg Accuracy for {} is {}'.format(str(model), round(avg_accuracy, 2))))
    print(colored('###################', 'blue'))
    print('\n')

    return avg_accuracy, std_deviation


# model.fit(inputs, outputs)
# accuracy = round(model.score(X, y), 3)
