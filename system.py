import zipfile, io

archive = zipfile.ZipFile("countries.zip", "r") #access a zip archive

file = archive.open("aa.html", "r")

for line in file:  #searches the file containing a string and outputs it
  if "People and Society" in line: 
    print line
