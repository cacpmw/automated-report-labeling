"""Helper Module"""

import os
from utils import BColors
import time


def get_user_input():
    """Get user input"""
    should_add_signed_tag = input(
        "Do you want to label pdfs as signed? y/n: (PRESS ENTER TO SUBMIT)\n"
    )
    return should_add_signed_tag == "y"


def check_folders(base_path):
    """Check if folders exist and created them if they dont"""
    if not os.path.exists(f"{base_path}"):
        os.makedirs(f"{base_path}")
        os.makedirs(f"{base_path}/pdfs")

    if not os.path.exists(f"{base_path}/output"):
        os.makedirs(f"{base_path}/output")


def is_docusigned(data):
    """Check for docusign string"""
    for line in data:
        if "docusign"  in line.lower():
            return True
    return False

def print_general_exception(e):
    """Print general exception"""
    print(f"{BColors.FAIL.value}{e}{BColors.ENDC.value}")

def fileNameWithMilliseconds(date,should_add_signed_tag, location, provider, patient, procedure, index, report_or_superbill):
    seconds = time.time()
    # Convert to milliseconds
    milliseconds = int(seconds * 1000)
    return f'{date} {"[Signed] " if should_add_signed_tag else "[Not Signed] "}[{report_or_superbill}]{f" [{location.strip()}] " if location else " [Home] "}{provider.strip()} - {patient.strip()} - {procedure}-{index}{milliseconds}.pdf'

def check_for_ds_store_file(report_path):
    if os.path.exists(f"{report_path}/.DS_store"):
        try:
            os.remove(f"{report_path}/.DS_store") # This file causes headaches on macs
            print(f"{BColors.OKCYAN.value}.DS_Store removed{BColors.ENDC.value}") 
        except Exception:
            print(f"{BColors.OKCYAN.value}Couldn't delete .DS_Store file.{BColors.ENDC.value}") 
    else:
        print(f"{BColors.OKCYAN.value}No .DS_Store file{BColors.ENDC.value}") 

def shutdown_at_zero_files(number_of_files):
    if number_of_files == 0:
        print(
            f"{BColors.FAIL.value}No pdfs available to relabel.\nStopping execution...{BColors.ENDC.value}"
        )
        sys.exit(0)