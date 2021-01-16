"""
Project related configuration
"""

ENGLISH_COLUMN_NAMES = ['status', 'duration', 'credit_history', 'purpose', 'amount',
                        'savings', 'employment_duration', 'installment_rate',
                        'personal_status_sex', 'other_debtors',
                        'present_residence', 'property',
                        'age', 'other_installment_plans',
                        'housing', 'number_credits',
                        'job', 'people_liable', 'telephone', 'foreign_worker',
                        'credit_risk']

"""
hints for NORMALIZATION_MAPPING:

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

    'purpose': {
        'delete': True,
        'replace_with': 'new_purpose',
        'use_as_is': False,
        'value_mapping': {
            0: 0,
            1: 1,
            2: 1,
            3: 2,
            4: 2,
            5: 2,
            6: 2,
            7: 3,
            8: 4,
            9: 3,
            10: 5,
        },
    },

    'amount': {
        'delete': True,
        'replace_with': None,
        'use_as_is': False,
        'value_mapping': {

        },
    },

    'savings': {
        'delete': True,
        'replace_with': 'new_savings',
        'use_as_is': False,
        'value_mapping': {
            1: 1,
            2: 2,
            3: 3,
            4: 3,
            5: 4,
        },
    },

    'employment_duration': {
        'delete': True,
        'replace_with': 'new_employment_duration',
        'use_as_is': False,
        'value_mapping': {
            1: 1,
            2: 2,
            3: 3,
            4: 3,
            5: 3,
        },
    },

    'installment_rate': {
        'delete': False,
        'replace_with': None,
        'use_as_is': True,
        'value_mapping': {
            1: 1,
            2: 2,
            3: 3,
            4: 4,
        },
    },

    'personal_status_sex': {
        'delete': True,
        'replace_with': None,
        'use_as_is': False,
        'value_mapping': {

        },
    },

    'other_debtors': {
        'delete': True,
        'replace_with': 'new_othe_debtors',
        'use_as_is': False,
        'value_mapping': {
            1: 1,
            2: 2,
            3: 2,
        },
    },

    'present_residence': {
        'delete': True,
        'replace_with': 'new_present_residence',
        'use_as_is': False,
        'value_mapping': {
            1: 1,
            2: 2,
            3: 2,
            4: 2,
        },
    },

    'property': {
        'delete': True,
        'replace_with': 'new_property',
        'use_as_is': False,
        'value_mapping': {
            1: 1,
            2: 2,
            3: 2,
            4: 2,
        },
    },

    'age': {
        'delete': True,
        'replace_with': None,
        'use_as_is': False,
        'value_mapping': {

        },
    },

    'other_installment_plans': {
        'delete': False,
        'replace_with': None,
        'use_as_is': True,
        'value_mapping': {
            1: 1,
            2: 2,
            3: 3,
        },
    },

    'housing': {
        'delete': True,
        'replace_with': 'new_housing',
        'use_as_is': False,
        'value_mapping': {
            1: 1,
            2: 2,
            3: 1,
        },
    },

    'number_credit': {
        'delete': False,
        'replace_with': None,
        'use_as_is': True,
        'value_mapping': {
            1: 1,
            2: 2,
            3: 3,
            4: 4,
        },
    },

    'job': {
        'delete': True,
        'replace_with': 'new_job',
        'use_as_is': False,
        'value_mapping': {
            1: 1,
            2: 2,
            3: 3,
            4: 3,
        },
    },

    'people_liable': {
        'delete': False,
        'replace_with': None,
        'use_as_is': True,
        'value_mapping': {
            1: 1,
            2: 2,
        },
    },

    'telephone': {
        'delete': True,
        'replace_with': None,
        'use_as_is': False,
        'value_mapping': {

        },
    },

    'foreign_worker': {
        'delete': False,
        'replace_with': None,
        'use_as_is': True,
        'value_mapping': {
            1: 1,
            2: 2,
        },
    },

    'credit_risk': {
        'delete': False,
        'replace_with': None,
        'use_as_is': True,
        'value_mapping': {
            1: 1,
            2: 2,
        },
    },
}
