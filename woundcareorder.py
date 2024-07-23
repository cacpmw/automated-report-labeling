from utils import parse_date
from utils import Errors, BASE_PATH
import os
from helpers import print_general_exception, fileNameWithMilliseconds


def wound_care_order_relabel(text, should_add_signed_tag,index):
    """Wound care order relabel function"""
    # print(text)
    try:
        procedure = "Wound Care Order"
        provider = text[8].split(":")[1]
        full_date = text[11].split(": ")[1]
        patient = text[10].split(":")[1]
        location = None

        if "-" in patient:
            patient, location = patient.split(" - ")
        
        date = parse_date(full_date) 
        finalFileName = f'{date} {"[Signed] " if should_add_signed_tag else "[Not Signed] "}[REPORT]{f" [{location.strip()}] " if location else " [Home] "}{provider.strip()} - {patient.strip()} - {procedure}.pdf'
        
        if os.path.exists(f"{BASE_PATH}/output/{finalFileName}"):
            return fileNameWithMilliseconds(date,should_add_signed_tag,location, provider,patient,procedure,index)

        return finalFileName

    except Exception as e:
        print_general_exception(e)
        return ""
