from pypdf import PdfReader
import os;
from utils import parse_date
import shutil;

from  woundassessment import wound_assessment_relabel
from superbill import superbill_relabel

reportPath = f"{os.path.expanduser('~')}/Reports/pdfs"
basePath = f"{os.path.expanduser('~')}/Reports"
print(reportPath);

PDFs = os.listdir(reportPath)
print(f"Reading {len(PDFs)} files")
print(PDFs,'\n\n')

if not os.path.exists(f"{basePath}/output"):
    os.makedirs(f"{basePath}/output")

for pdf in PDFs:
    print(pdf)
    reader = PdfReader(f'{reportPath}/{pdf}')

    page = reader.pages[0]
    text=page.extract_text().splitlines();
    print(text)
    procedure_type = text[1]
    
    match procedure_type :
        case 'Wound Assessment':
            label = wound_assessment_relabel(text);
            print(label);
            shutil.copy(f"{reportPath}/{pdf}",f"{basePath}/output/{label}")
        case 'SuperBill':
            label = superbill_relabel(text)
            print(label);
            shutil.copy(f"{reportPath}/{pdf}",f"{basePath}/output/{label}")











