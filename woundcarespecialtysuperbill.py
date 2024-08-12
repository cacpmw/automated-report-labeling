from utils import parse_date
from utils import BASE_PATH
import os
from helpers import print_general_exception, fileNameWithMilliseconds


def wound_care_specialty_superbill_relabel(text, should_add_signed_tag,index):
    """Wound care specialty superbill relabel function"""
    # print(text)
    try:
        procedure = "Superbill"
        provider = text[4].split(":")[1]
        full_date = text[6].split(": ")[1]
        patient = text[7].split(":")[1]
        location = None

        if "-" in patient:
            patient, location = patient.split(" - ")
        
        date = parse_date(full_date) 
        finalFileName = f'{date} {"[Signed] " if should_add_signed_tag else "[Not Signed] "}[Superbill]{f" [{location.strip()}] " if location else " [Home] "}{provider.strip()} - {patient.strip()} - {procedure}.pdf'
        
        if os.path.exists(f"{BASE_PATH}/output/{finalFileName}"):
            return fileNameWithMilliseconds(date,should_add_signed_tag,location, provider,patient,procedure,index,"Superbill")

        return finalFileName

    except Exception as e:
        print_general_exception(e)
        return ""
