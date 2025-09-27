from langchain_community.document_loaders import CSVLoader

from helper_functions import api_log


def read_test_csv_file(filename):
    api_log(msg="***************READ CSV FILE BLOC*****************")
    if not filename.lower().endswith(".csv"):
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
            "fieldnames": ["Index", "Height", "Weight"],
        },
    )
    docs = lang_csv_data.load()
    return docs
