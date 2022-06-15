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

    "house_max": 50,
    "landmark_max": 100,
    "country_max": 50,
    "state_max": 50,
    "city_max": 50,

    "corres_house_max": 50,
    "corres_landmark_max": 100,

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

ADDRESS = {
    'house_number': {
        "blank": "HOUSE NUMBER FIELD BLANK",
        "required": "HOUSE_NUMBER_REQUIRED",
        "max_length": "HOUSE-NUMBER_MAX_LENGTH"
    },

    'landmark': {
        "blank": "LANDMARK FIELD BLANK",
        "required": "LANDMARK_REQUIRED",
        "max_length": "LANDMARK_MAX_LENGTH"
    },

    'country': {
        "blank": "COUNTRY FIELD BLANK",
        "required": "COUNTRY_REQUIRED",
        "max_length": "COUNTRY_MAX_LENGTH"
    },

    'state': {
        "blank": "STATE FIELD BLANK",
        "required": "STATE_REQUIRED",
        "max_length": "STATE_MAX_LENGTH"
    },

    'city': {
        "blank": "CITY FIELD BLANK",
        "required": "CITY_REQUIRED",
        "max_length": "CITY_MAX_LENGTH"
    },
    'pincode': {
        "blank": "PINCODE FIELD BLANK",
        "required": "PINCODE_REQUIRED",

    },
}

CORRESPONDENCE_ADDRESS = {
    'house_number': {
        "blank": "HOUSE NUMBER FIELD BLANK",
        "required": "HOUSE_NUMBER_REQUIRED",
        "max_length": "HOUSE-NUMBER_MAX_LENGTH"
    },
    'corres_landmark': {
        "blank": "LANDMARK FIELD BLANK",
        "required": "LANDMARK_REQUIRED",
        "max_length": "LANDMARK_MAX_LENGTH"
    },

}
