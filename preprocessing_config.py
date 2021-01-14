"""
hints:

delete: True/False
replace_with: string/None
use_as_is: True/False
value_mapping: Dict

"""

NORMALIZATION_MAPPING = {
    'status': {
        'delete': True,
        'replace_with': 'new_status',
        'use_as_is': False,
        'value_mapping': {
            1: 1,
            2: 2,
            3: 3,
            4: 3,
        },
    },

    'duration': {
        'delete': True,
        'replace_with': None,
        'use_as_is': False,
        'value_mapping': {

        },
    },

    'credit_history': {
        'delete': True,
        'replace_with': 'new_credit_history',
        'use_as_is': False,
        'value_mapping': {
            0: 0,
            1: 1,
            2: 2,
            3: 2,
            4: 2,
        },
    },

}

# EXAMPLE DICTIONARY
# key - value mapping

# {
#    'key1': 'value1',
#    'key2': 'value2',
#    'key3': {
#        'key3.key1': 'value3.value1',
#        'key3.key2': 'value3.value2',
#    },
#    'key4': 'value4',
# }
