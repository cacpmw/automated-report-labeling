from utils import parse_date
from utils import Errors


def wound_assessment_relabel(text, should_add_signed_tag):
    """Wound assessment relabel function"""
    try:
        procedure = "Wound Assessment"
        provider = text[8].split(":")[1]
        full_date = text[10].split(": ")[1]
        patient = text[11].split(":")[1]
        location = None

        if "-" in patient:
            patient, location = patient.split(" - ")

        date = parse_date(full_date)

        return f'{date} {"[Signed] " if should_add_signed_tag else "[Not Signed] "}[REPORT]{f" [{location.strip()}] " if location else " [Home] "}{provider.strip()} - {patient.strip()} - {procedure}.pdf'
    except IndexError:
        print(Errors.INDEXERROR.value)
        return ""
