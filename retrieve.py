def save_data():
    pass



def retrieve_data(uri: str, res_to_json=lambda r: r, store_json=save_data, filename="test.pt"):
    pass
def download(url, file_name):
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
