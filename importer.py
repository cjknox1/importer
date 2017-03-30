#!/usr/bin/env python

""" Importer.py, by Chris Knox 2017_03_28
This program will find the image directory, change the name, and save to another directory"""
"""Variable allocation
    ans= answer to MRN query
    mrn_count= MEEI MRN number
    mrn= length of the ans"""

print("IO Image Importer")


def mrn_check():

    ans = input("Enter MRN:")

    mrn_count = 14

    mrn = len(ans)

    if mrn == mrn_count:
        print("ok")
    else:
        print("Check MRN and Re-enter, please")
        mrn_check()


if __name__ == "__main__":
    mrn_check()



