from utils import parse_date


def wound_care_order_relabel(text, shouldAddSignedTag):
    procedure = "Wound Care Order";
    provider = text[8].split(":")[1];
    full_date = text[0];
    patient= text[10].split(":")[1]
    location=None;

    if "-" in patient:
        patient,location = patient.split(" - ");

    date=parse_date(full_date)

    return f'{date} {f"[Signed] " if shouldAddSignedTag else "[Not Signed] "}[REPORT]{f" [{location.strip()}] " if location else " [Home] "}{provider.strip()} - {patient.strip()} - {procedure}.pdf'
