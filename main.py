""" Main functionality including preprocessing, training and validation """

import os

from preprocessing import preprocess_file


if __name__ == '__main__':
    RAW_FILE_PATH = os.getenv('RAW_FILE_PATH', 'data/south_german_credit.asc')
    main_df = preprocess_file(RAW_FILE_PATH)
    item = main_df.iloc[0]
    assert item is not None
    print(main_df)
