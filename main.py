# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


""" Load data from comtrade.un.org/data
"""
import requests
import os
import logging
import tempfile
import convert_json_to_pytable

def load_data_from_comtrade(url, dest_file):
    """ Load data by given url, and save them to dest_file pytable.
    """
    tfile = tempfile.NamedTemporaryFile(delete=False)
    url = """https://comtrade.un.org/api/get/plus?max=100000&type=C&freq=A&px=HS&ps=2019&r=643&p=
    0&rg=all%2C2&cc=TOTAL&uitoken=51f8d57316ef76afd66c0074d5b53774&fmt=json
    """
    logging.info("file_name = %s", tfile.name)
    convert_json_to_pytable(tfile.name, dest_file, url)
    os.unlink(tfile.name)
    requests.get(url).json()
