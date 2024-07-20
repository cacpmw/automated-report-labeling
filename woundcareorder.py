from utils import parse_date
from utils import Errors


def wound_care_order_relabel(text, shoud_add_signed_tag):
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
        # print(date)

        return f'{date} {"[Signed] " if shoud_add_signed_tag else "[Not Signed] "}[REPORT]{f" [{location.strip()}] " if location else " [Home] "}{provider.strip()} - {patient.strip()} - {procedure}.pdf'
    except Exception:
        print(Errors.EXCEPTION_MESSAGE.value)
        return ""
