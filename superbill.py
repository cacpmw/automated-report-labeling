from pypdf import PdfReader
import os;
from utils import parse_date


def superbill_relabel(text):
    procedure = text[1].strip();
    provider = text[2].split(":")[1].strip();
    full_date = text[4].split(": ")[1].strip();
    patient, location = text[5].split(":")[1].split("-")

    print(procedure, provider,full_date,patient, location);

    date=parse_date(full_date)

    return f'\n{date} [Signed] [Superbill] [{location.strip()}] {provider} - {patient.strip()} - {procedure}.pdf'
