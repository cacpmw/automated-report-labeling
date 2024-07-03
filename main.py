from pypdf import PdfReader;
import os;
from utils import parse_date;
from utils import bcolors;
import shutil;
import time


from woundassessment import wound_assessment_relabel;
from superbill import superbill_relabel;
from graft import graft_relabel;
from debridement import debridement_relabel;
from labresults import lab_results_relabel;
from amendnote import amend_note_relabel;
from woundcareorder import wound_care_order_relabel;

start_time = time.time();
reportPath = f"{os.path.expanduser('~')}/Reports/pdfs";
basePath = f"{os.path.expanduser('~')}/Reports";
print(f"{bcolors.BOLD}{bcolors.HEADER}Accessing files in {reportPath}");
PDFs = os.listdir(reportPath);
number_of_files = len(PDFs);
print(f"Reading {number_of_files} files");
print(f"{PDFs}{bcolors.ENDC}",'\n');

if not os.path.exists(f"{basePath}/output"):
    os.makedirs(f"{basePath}/output");
print(f"{bcolors.BOLD}{bcolors.OKGREEN}Starting to relabel files...{bcolors.ENDC}")
for pdf in PDFs:
    reader = PdfReader(f'{reportPath}/{pdf}')

    page = reader.pages[0]
    text=page.extract_text().splitlines();
    procedure_type = text[1]
    
    match procedure_type :
        case 'Wound Assessment':
            label = wound_assessment_relabel(text);
            print(f"{bcolors.OKBLUE}{label}{bcolors.ENDC}");
            shutil.copy(f"{reportPath}/{pdf}",f"{basePath}/output/{label}")
        case 'SuperBill':
            label = superbill_relabel(text)
            print(f"{bcolors.OKBLUE}{label}{bcolors.ENDC}");            
            shutil.copy(f"{reportPath}/{pdf}",f"{basePath}/output/{label}")
        case "Graft Pr ocedur e":
            label = graft_relabel(text)
            print(f"{bcolors.OKBLUE}{label}{bcolors.ENDC}");            
            shutil.copy(f"{reportPath}/{pdf}",f"{basePath}/output/{label}")
        case "Non-Selectiv e Sharp Debridement":
            label = debridement_relabel(text);
            print(f"{bcolors.OKBLUE}{label}{bcolors.ENDC}");            
            shutil.copy(f"{reportPath}/{pdf}",f"{basePath}/output/{label}")
        case "Lab W ork Results":
            label = lab_results_relabel(text);
            print(f"{bcolors.OKBLUE}{label}{bcolors.ENDC}");            
            shutil.copy(f"{reportPath}/{pdf}",f"{basePath}/output/{label}")
        case "Amend Repor ts":
            label = amend_note_relabel(text);
            print(f"{bcolors.OKBLUE}{label}{bcolors.ENDC}");            
            shutil.copy(f"{reportPath}/{pdf}",f"{basePath}/output/{label}")
        case "Wound Car e Order":
            label = wound_care_order_relabel(text);
            print(f"{bcolors.OKBLUE}{label}{bcolors.ENDC}");            
            shutil.copy(f"{reportPath}/{pdf}",f"{basePath}/output/{label}")

print(f"{bcolors.OKGREEN}--- {number_of_files} files relabeled in %s seconds ---{bcolors.ENDC}" % (time.time() - start_time));











