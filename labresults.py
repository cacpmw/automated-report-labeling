from utils import parse_date


def lab_results_relabel(text):
    procedure = "Lab Results";
    provider = text[6].split(":")[1];
    full_date = text[9].split(": ")[1]
    patient= text[8].split(":")[1]
    location=None;

    if "-" in patient:
        patient,location = patient.split("-");

    date=parse_date(full_date)

    return f'\n{date} [Signed] [REPORT]{f" [{location.strip()}] " if location else " [Home] "}{provider.strip()} - {patient.strip()} - {procedure}.pdf'
