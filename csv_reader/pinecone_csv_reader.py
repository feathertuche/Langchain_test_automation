from langchain_community.document_loaders import CSVLoader
from helper_functions import api_log


def read_test_csv_file(filename):
    api_log(msg="***************READ CSV FILE BLOC*****************")
    api_log(msg='12')
    if not filename.lower().endswith(".csv"):
        api_log(msg='13')
        raise ValueError(
            f"'Invalid file format: {filename}, please check the file name and try again..'"
        )

    api_log(
        msg=f"Reading and fetching data from  CSV file: {filename}, please wait a while..."
    )
    lang_csv_data = CSVLoader(
        file_path=filename,
        autodetect_encoding=True,
        csv_args={
            "delimiter": ",",
            "quotechar": '"',
            #"fieldnames": ["Index", "Height", "Weight"],
        },
    )
    api_log(msg='14')
    docs = lang_csv_data.load()
    api_log(msg=f'THIS IS A DOCCCCCC: {docs}')
    return docs
