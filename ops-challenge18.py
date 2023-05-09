# Demo Class 18
#
# The Python "zipfile" library at https://docs.python.org/3/library/zipfile.html allows us to interact with files using the ZIP archive and compression standard. 

from zipfile import ZipFile

zip_file = ### Your password protected zip file ###
password = ### Password to guess ###

with ZipFile(zip_file) as zf:
  zf.extractall(pwd=bytes(password,'utf-8'))