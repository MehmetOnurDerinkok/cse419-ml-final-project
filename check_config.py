try:
    from preprocessing_config import NORMALIZATION_MAPPING
    print('SUCCESS: CONFIG SYNTAX IS CORRECT')
except Exception:
    print('ERROR: CONFIG SYNTAX IS BROKEN!')
