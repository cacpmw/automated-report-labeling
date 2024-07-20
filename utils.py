""" Utility functions and classes """
from enum import Enum

def parse_date(string_date):
    """Parse dates from a string"""
    date = ""
    splitted = string_date.split(" ")
    date += splitted[3] + "."
    day = splitted[2].split(",")[0]
    if splitted[1] == "January":
        date += "01." + day
    elif splitted[1] == "February":
        date += "02.0" + day if int(day) < 10 else "02." + day
    elif splitted[1] == "March":
        date += "03.0" + day if int(day) < 10 else "03." + day
    elif splitted[1] == "April":
        date += "04.0" + day if int(day) < 10 else "04." + day
    elif splitted[1] == "May":
        date += "05.0" + day if int(day) < 10 else "05." + day
    elif splitted[1] == "June":
        date += "06.0" + day if int(day) < 10 else "06." + day
    elif splitted[1] == "July":
        date += "07.0" + day if int(day) < 10 else "07." + day
    elif splitted[1] == "August":
        date += "08.0" + day if int(day) < 10 else "08." + day
    elif splitted[1] == "September":
        date += "09.0" + day if int(day) < 10 else "09." + day
    elif splitted[1] == "October":
        date += "10.0" + day if int(day) < 10 else "10." + day
    elif splitted[1] == "November":
        date += "11.0" + day if int(day) < 10 else "11." + day
    elif splitted[1] == "December":
        date += "12.0" + day if int(day) < 10 else "12." + day
    return date


class BColors(Enum):
    """Terminal colors"""

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class Errors(Enum):
    """Exception messages"""

    EXCEPTION_MESSAGE = f"{BColors.FAIL.value}ERROR: The current file isn't in the correct format. Can't relabel this one.\nPlease replace it or remove it and relabel manually{BColors.ENDC.value}"
