import zipfile

source = 'photos.zip'
destination = 'photos/'

with zipfile.ZipFile(source, 'r') as zipfile:
    zipfile.extractall(destination)