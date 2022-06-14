CHAR_LIMIT_SIZE = {
    "email_min": 8,
    "email_max": 20,
    "firstname_min": 1,
    "firstname_max": 20,
    "lastname_min": 1,
    "lastname_max": 20,
    "username_min": 1,
    "username_max": 20,
    "password_min": 8,
    "password_max": 16,


}

VALIDATION = {
    'email': {
        "blank": "EMAIL_BLANK",
        "invalid": "EMAIL_INVALID",
        "required": "EMAIL_REQUIRED",
        "min_length": "EMAIL_MIN_LENGTH",
        "max_length": "EMAIL_MAX_LENGTH"

    },
    'username': {
        "blank": "USERNAME_BLANK",
        "invalid": "USERNAME_INVALID",
        "required": "USERNAME_REQUIRED",
        "min_length": "EMAIL_MIN_LENGTH",
        "max_length": "EMAIL_MAX_LENGTH"
    },
    'firstname': {
        "blank": "NAME_BLANK",
        "invalid": "NAME_INVALID",
        "required": "USERNAME_REQUIRED",
        "min_length": "EMAIL_MIN_LENGTH",
        "max_length": "EMAIL_MAX_LENGTH"
    },
    'lastname': {
        "blank": "NAME_BLANK",
        "invalid": "NAME_INVALID",
        "required": "USERNAME_REQUIRED",
        "min_length": "EMAIL_MIN_LENGTH",
        "max_length": "EMAIL_MAX_LENGTH"
    },

    'password': {
        "blank": "PASSWORD_BLANK",
        "invalid": "PASSWORD_INVALID",
        "required": "PASSWORD_REQUIRED",
        "min_length": "PASSWORD_MIN_LENGTH",
        "max_length": "PASSWORD_MAX_LENGTH"
    },


}
