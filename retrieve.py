def save_data():
    pass
def download(url, file_name):
    url = """https://comtrade.un.org/api/get/plus?max=100000&type=C&freq=A&px=HS&ps=2019&r=643&p=0&rg=all%2C2&cc=TOTAL&uitoken=51f8d57316ef76afd66c0074d5b53774&fmt=json
    """
    get_r = requests.get(url)
    r.text
    r.encoding = 'utf-8'
    r.json()
    res_to_json= lambda r: r
    type(r)
    # file_name  = url.split("/")[-1]
    log.info("file_name = %s", file_name)
    with open(file_name, 'wb') as fd:
        for chunk in get_r.iter_content(chunk_size=1024):
                fd.write(chunk)

def retrieve_data(uri: str, res_to_json=lambda r: r, store_json=save_data, filename="test.pt"):
    pass

def convert_json_to_pytable(src_file_name, dst_file_name, url):
    with open(src_file_name, "wb") as fd:
        for chunk in get_r.iter_content(chunk_size=1024):
    data = json.load(fd)
    data = data.get("dataset")
    first_row = data[0]
    table_config = gen_table_config(first_row, url)

    log.info("table_config = %s", table_config)

    with  Hdf5Table.create_new_file(
            file_path = os.path.join(get_bm_data_path(), "series", "test_test_comtrade.h5")
    if os.path.exists(file_path):
        os.unlink(file_path),
            table_path="/table",
            table_config=table_config) as h5file:
        h5file.add_rows(data)
        h5file.write(data)
        h5file.close()



