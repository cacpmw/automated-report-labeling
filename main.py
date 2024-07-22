"""Automation for relabeling pdf files."""

import shutil
import time
import sys
import os
from pypdf import PdfReader
from utils import BColors
from sys import platform

from helpers import check_folders, is_docusigned

from woundassessment import wound_assessment_relabel
from superbill import superbill_relabel
from graft import graft_relabel
from debridement import debridement_relabel
from labresults import lab_results_relabel
from amendnote import amend_note_relabel
from woundcareorder import wound_care_order_relabel


report_path = f"{os.path.expanduser('~')}/Reports/pdfs"
base_path = f"{os.path.expanduser('~')}/Reports"

print(f"{BColors.BOLD.value}{BColors.HEADER.value}Accessing files in {report_path}{BColors.ENDC.value}")

check_folders(base_path)

if os.path.exists(f"{report_path}/.DS_store"):
    try:
        os.remove(f"{report_path}/.DS_store") # This file causes headaches on macs
        print(f"{BColors.OKCYAN.value}.DS_Store removed{BColors.ENDC.value}") 
    except Exception:
        print(f"{BColors.OKCYAN.value}Couldn't delete .DS_Store file.{BColors.ENDC.value}") 


else:
  print(f"{BColors.OKCYAN.value}No .DS_Store file{BColors.ENDC.value}") 

PDFs = os.listdir(report_path)
number_of_files = len(PDFs)
if number_of_files == 0:
    print(
        f"{BColors.FAIL.value}No pdfs available to relabel.\nStopping execution...{BColors.ENDC.value}"
    )
    sys.exit(0)

print(f"{BColors.HEADER.value}Reading {number_of_files} files")
print(f"{PDFs}{BColors.ENDC.value}", "\n")


print(
    f"{BColors.BOLD.value}{BColors.OKGREEN.value}Starting to relabel files...{BColors.ENDC.value}"
)

start_time = time.time()

for index, pdf in enumerate(PDFs):
    try:
        reader = PdfReader(f"{report_path}/{pdf}")
    except Exception:
        print(Exception)

    page = reader.pages[0]
    text = page.extract_text().splitlines()
    procedure_type = text[1]
    SHOULD_ADD_SIGNED_TAG = is_docusigned(text)
    print(f"{pdf} {BColors.WARNING.value}| Original file name{BColors.ENDC.value}") #prints the pdf filename

    match procedure_type:
        case "Wound Assessment":
            label = wound_assessment_relabel(text, SHOULD_ADD_SIGNED_TAG, index)
            print(f"{BColors.OKBLUE.value}{label}{BColors.ENDC.value} {BColors.WARNING.value}| New file name{BColors.ENDC.value}")
            shutil.copy(f"{report_path}/{pdf}", f"{base_path}/output/{label}")
        case "SuperBill":
            label = superbill_relabel(text, SHOULD_ADD_SIGNED_TAG, index)
            print(f"{BColors.OKBLUE.value}{label}{BColors.ENDC.value} {BColors.WARNING.value}| New file name{BColors.ENDC.value}")
            shutil.copy(f"{report_path}/{pdf}", f"{base_path}/output/{label}")
        case "Graft Pr ocedur e":
            label = graft_relabel(text, SHOULD_ADD_SIGNED_TAG,index)
            print(f"{BColors.OKBLUE.value}{label}{BColors.ENDC.value} {BColors.WARNING.value}| New file name{BColors.ENDC.value}")
            shutil.copy(f"{report_path}/{pdf}", f"{base_path}/output/{label}")
        case "Non-Selectiv e Sharp Debridement":
            label = debridement_relabel(text, SHOULD_ADD_SIGNED_TAG,index)
            print(f"{BColors.OKBLUE.value}{label}{BColors.ENDC.value} {BColors.WARNING.value}| New file name{BColors.ENDC.value}")
            shutil.copy(f"{report_path}/{pdf}", f"{base_path}/output/{label}")
        case "Lab W ork Results":
            label = lab_results_relabel(text, SHOULD_ADD_SIGNED_TAG,index)
            print(f"{BColors.OKBLUE.value}{label}{BColors.ENDC.value} {BColors.WARNING.value}| New file name{BColors.ENDC.value}")
            shutil.copy(f"{report_path}/{pdf}", f"{base_path}/output/{label}")
        case "Amend Repor ts":
            label = amend_note_relabel(text, SHOULD_ADD_SIGNED_TAG,index)
            print(f"{BColors.OKBLUE.value}{label}{BColors.ENDC.value} {BColors.WARNING.value}| New file name{BColors.ENDC.value}")
            shutil.copy(f"{report_path}/{pdf}", f"{base_path}/output/{label}")
        case "Wound Car e Order":
            label = wound_care_order_relabel(text, SHOULD_ADD_SIGNED_TAG,index)
            print(f"{BColors.OKBLUE.value}{label}{BColors.ENDC.value} {BColors.WARNING.value}| New file name{BColors.ENDC.value}")
            shutil.copy(f"{report_path}/{pdf}", f"{base_path}/output/{label}")
    print("\n")

print(
    f"{BColors.OKGREEN.value}--- {number_of_files} files relabeled in %s seconds ---{BColors.ENDC.value}"
    % (time.time() - start_time)
)
