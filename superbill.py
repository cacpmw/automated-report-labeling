""" Superbill Module """

from utils import parse_date
from utils import Errors, BASE_PATH
import os


def superbill_relabel(text, should_add_signed_tag,index):
    """Superbill relabel"""
    try:
        procedure = "Superbill"
        provider = text[2].split(":")[1].strip()
        full_date = text[4].split(": ")[1].strip()
        patient = text[5].split(":")[1]
        date = parse_date(full_date)

        if " - " in patient:
            patient, location = patient.split(" - ")
        finalFileName = f'{date} {"[Signed] " if should_add_signed_tag else "[Not Signed] "}[Superbill]{f" [{location.strip()}] " if location else " [Home] "}{provider.strip()} - {patient.strip()} - {procedure}.pdf'
        if os.path.exists(f"{BASE_PATH}/output/{finalFileName}"):
            return f'{date} {"[Signed] " if should_add_signed_tag else "[Not Signed] "}[Superbill]{f" [{location.strip()}] " if location else " [Home] "}{provider.strip()} - {patient.strip()} - {procedure}-{index}.pdf'
        return finalFileName
    except Exception as e:
        #print(Errors.EXCEPTION_MESSAGE.value)
        print(e)
        return ""
