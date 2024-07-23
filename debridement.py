""" Debridement Module"""

from utils import parse_date
from utils import Errors, BASE_PATH
import os
from helpers import print_general_exception,fileNameWithMilliseconds


def debridement_relabel(text, should_add_signed_tag,index):
    """Debridement relabel function"""
    # print(text)
    try:
        procedure = "Debriedement"
        provider = text[10].split(":")[1]
        full_date = text[12].split(": ")[1]
        patient = text[14].split(":")[1]
        location = None

        if "-" in patient:
            patient, location = patient.split(" - ")
       
        date = parse_date(full_date)
        finalFileName = f'{date} {"[Signed] " if should_add_signed_tag else "[Not Signed] "}[REPORT]{f" [{location.strip()}] " if location else " [Home] "}{provider.strip()} - {patient.strip()} - {procedure}.pdf'
        
        if os.path.exists(f"{BASE_PATH}/output/{finalFileName}"):
            return fileNameWithMilliseconds(date,should_add_signed_tag,location, provider,patient,procedure,index)

        return finalFileName 

    except Exception as e:
        print_general_exception
        return ""
