import zipfile, io, re

def main():
    country = raw_input("Enter a Country:")
    keyWord = raw_input("What would you like to know?")
    countrySearch(country, keyWord)

def countrySearch(country, key):
    file = open("countryList.txt", "r")
    for line in file:
        if country in line: 
            page = line[:2] + ".html" #finds name of the countrie's file
      
    archive = zipfile.ZipFile("countries.zip", "r") #access a zip archive
    file2 = archive.open(page, "r")
    for line in file2:  #searches the file containing a string and outputs it
        if key in line: 
            print line

if __name__ == '__main__':
    main()
