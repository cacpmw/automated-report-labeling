""" Amend Notes Module"""

from utils import parse_date
from utils import Errors, BASE_PATH
import os


def amend_note_relabel(text, should_add_signed_tag,index):
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
        finalFileName = f'{date} {"[Signed] " if should_add_signed_tag else "[Not Signed] "}[REPORT]{f" [{location.strip()}] " if location else " [Home] "}{provider.strip()} - {patient.strip()} - {procedure}.pdf'
        if os.path.exists(f"{BASE_PATH}/output/{finalFileName}"):
            return f'{date} {"[Signed] " if should_add_signed_tag else "[Not Signed] "}[REPORT]{f" [{location.strip()}] " if location else " [Home] "}{provider.strip()} - {patient.strip()} - {procedure}-{index}.pdf'
        return finalFileName
    except Exception as e:
        #print(Errors.EXCEPTION_MESSAGE.value)
        print(e)
        return ""
