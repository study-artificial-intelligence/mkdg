"""
Implement load file: csv, text
"""
import pandas as pd


def read_csv_file(sheet_name):
    data = pd.read_excel("data/misspell.xlsx", sheet_name=sheet_name)
    return data


def read_text_file(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        text = f.readlines()

    return text


if __name__ == "__main__":
    """ txt file """
    # filename = "./data/20200404060046918.txt"
    # raw_text = read_text_file(filename)
    # print(raw_text)

    """ csv file """
    raw_text = read_csv_file("adjective")
    print(raw_text)
