from pypdf import PdfReader
import os;
from utils import parse_date


def superbill_relabel(text):
    procedure = "Superbill";
    provider = text[2].split(":")[1].strip();
    full_date = text[4].split(": ")[1].strip();
    patient = text[5].split(":")[1]

    date=parse_date(full_date)

    if "-" in patient:
        patient,location = patient.split("-");

    return f'{date} [Signed] [Superbill]{f" [{location.strip()}] " if location else " [Home] "}{provider.strip()} - {patient.strip()} - {procedure}.pdf'
