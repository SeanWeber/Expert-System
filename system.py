import zipfile, io, re

def main():
  country = raw_input("Enter a Country:")
  file = open("countryList.txt", "r")
  for line in file:
    if country in line: 
      countryPage = line[:2] + ".html"
  countrySearch(countryPage)

def countrySearch(page):
  archive = zipfile.ZipFile("countries.zip", "r") #access a zip archive
  file = archive.open(page, "r")
  for line in file:  #searches the file containing a string and outputs it
    if "Background" in line: 
      print line

if __name__ == '__main__':
  main()
