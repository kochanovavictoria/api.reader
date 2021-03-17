# coding: utf-8

""" Load data from comtrade.un.org/data
"""

import os
import logging
import json
import requests
import tempfile

from rbs_series.hdf5tables import Hdf5Table

log = logging.getLogger()


def download(url, file_name):
    get_response = requests.get(url, stream=True)
    # file_name  = url.split("/")[-1]
    log.info("file_name = %s", file_name)
    with open(file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)


def convert_json_to_pytable(src_file_name, dst_file_name, url):
    with open(src_file_name, "r") as f:
        data = json.load(f)
    data = data.get("dataset")
    first_row = data[0]
    table_config = gen_table_config(first_row, url)

    log.info("table_config = %s", table_config)

    with  Hdf5Table.create_new_file(
            file_path=dst_file_name,
            table_path="/table",
            table_config=table_config) as h5file:
        h5file.add_rows(data)
        h5file.close()


def gen_table_config(first_row, url):
    table_config = {
        "fields": {},
        "description": "data loaded from url: %s" % url
    }
    fields = table_config["fields"]
    n = 0
    for k in sorted(first_row.keys()):
        v = first_row[k]
        if v == None:
            fields[k] = "StringCol(100, pos = %s)" % n
        elif isinstance(v, int):
            fields[k] = "Int64Col(pos = %s)" % n
        elif isinstance(v, float):
            fields[k] = "Float64Col(pos = %s)" % n
        else:
            fields[k] = "StringCol(100, pos = %s)" % n
    return table_config


def load_data_from_comtrade(url, dest_file):
    """ Load data by given url, and save them to dest_file pytable.
    """

    tfile = tempfile.NamedTemporaryFile(delete=False)
    download(url, tfile.name)
    log.info("file_name = %s", tfile.name)
    convert_json_to_pytable(tfile.name, dest_file, url)
    os.unlink(tfile.name)


def example_tester():
    logging.basicConfig(level=logging.DEBUG)
    url = """https://comtrade.un.org/api/get/plus?max=100000&type=C&freq=A&px=HS&ps=2019&r=643&p=0&rg=all%2C2&cc=TOTAL&uitoken=51f8d57316ef76afd66c0074d5b53774&fmt=json
    """
    big_url = """https://comtrade.un.org/api/get/plus?max=100000&type=C&freq=A&px=HS&ps=2019&r=all&p=0&rg=all&cc=TOTAL&uitoken=51f8d57316ef76afd66c0074d5b53774&fmt=json"""
    from rbs_path.path_functions import get_bm_data_path
    file_path = os.path.join(get_bm_data_path(), "series", "test_test_comtrade.h5")
    if os.path.exists(file_path):
        os.unlink(file_path)
    load_data_from_comtrade(url, file_path)
