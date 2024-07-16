from utils import parse_date
from utils import errors


def amend_note_relabel(text, shouldAddSignedTag):
    try:
        procedure = "Amend Note"
        provider = text[9].split(":")[1]
        full_date = text[12].split(": ")[1]
        patient = text[11].split(":")[1]
        location = None

        if "-" in patient:
            patient, location = patient.split(" - ")

        date = parse_date(full_date)

        return f'{date} {f"[Signed] " if shouldAddSignedTag else "[Not Signed] "}[REPORT]{f" [{location.strip()}] " if location else " [Home] "}{provider.strip()} - {patient.strip()} - {procedure}.pdf'
    except IndexError:
        print(errors.INDEXERROR)
        return ""
