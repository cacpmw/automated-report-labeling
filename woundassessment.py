from pypdf import PdfReader
import os;
from utils import parse_date


def wound_assessment_relabel(text):
    procedure = text[1];
    provider = text[8].split(":")[1];
    full_date = text[10].split(": ")[1]
    patient= text[11].split(":")[1]
    location=None;

    if patient.__contains__("-"):
        location = patient.split("-")[1];

    date=parse_date(full_date)

    return f'\n{date} [Signed] [REPORT]{f" [{location.strip()}] " if location else " [Home] "} {provider} - {patient.strip()} - {procedure}.pdf'
