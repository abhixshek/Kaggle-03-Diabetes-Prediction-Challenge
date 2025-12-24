import zipfile


def extract_from_zip(zip_file):
    with zipfile.ZipFile(zip_file) as zip_file_object:
        zip_file_object.extractall(path=zip_file.split('.')[0])
