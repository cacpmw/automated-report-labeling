from utils import parse_date


def graft_relabel(text, shouldAddSignedTag):
    procedure = "Graft";
    provider = text[5].split(":")[1];
    full_date = text[7].split(": ")[1]
    patient= text[9].split(":")[1]
    location=None;

    if patient.__contains__("-"):
        patient,location = patient.split("-");

    date=parse_date(full_date)

    return f'{date} {f"[Signed] " if shouldAddSignedTag else ""}[REPORT]{f" [{location.strip()}] " if location else " [Home] "}{provider.strip()} - {patient.strip()} - {procedure}.pdf'
