""" Lab Results Module"""

from utils import parse_date
from utils import Errors


def lab_results_relabel(text, should_add_signed_tag):
    """Lab Results relabel"""

    try:
        procedure = "Lab Results"
        provider = text[6].split(":")[1]
        full_date = text[9].split(": ")[1]
        patient = text[8].split(":")[1]
        location = None

        if "-" in patient:
            patient, location = patient.split(" - ")

        date = parse_date(full_date)

        return f'{date} {"[Signed] " if should_add_signed_tag else "[Not Signed] "}[REPORT]{f" [{location.strip()}] " if location else " [Home] "}{provider.strip()} - {patient.strip()} - {procedure}.pdf'
    except IndexError:
        print(Errors.INDEXERROR.value)
        return ""
