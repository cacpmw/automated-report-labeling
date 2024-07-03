from utils import parse_date


def debridement_relabel(text):
    procedure = "Debriedement";
    provider = text[10].split(":")[1];
    full_date = text[12].split(": ")[1]
    patient= text[14].split(":")[1]
    location=None;

    if "-" in patient:
        patient,location = patient.split("-");

    date=parse_date(full_date)

    return f'\n{date} [Signed] [REPORT]{f" [{location.strip()}] " if location else " [Home] "}{provider.strip()} - {patient.strip()} - {procedure}.pdf'
