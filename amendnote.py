""" Amend Notes Module"""

from utils import parse_date
from utils import Errors


def amend_note_relabel(text, should_add_signed_tag):
    """Amend Notes relabel"""
    try:
        procedure = "Amend Note"
        provider = text[9].split(":")[1]
        full_date = text[12].split(": ")[1]
        patient = text[11].split(":")[1]
        location = None

        if "-" in patient:
            patient, location = patient.split(" - ")

        date = parse_date(full_date)

        return f'{date} {"[Signed] " if should_add_signed_tag else "[Not Signed] "}[REPORT]{f" [{location.strip()}] " if location else " [Home] "}{provider.strip()} - {patient.strip()} - {procedure}.pdf'
    except Exception:
        print(Errors.EXCEPTION_MESSAGE.value)
        return ""
