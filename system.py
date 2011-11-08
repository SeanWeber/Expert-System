from BeautifulSoup import BeautifulSoup
from difflib import *
import zipfile, io, re

def main():
    country = raw_input("Enter a Country:")
    keyWord = getQuery() #raw_input("What would you like to know?")
    countrySearch(country, keyWord)

def countrySearch(country, key):
    file = open("countryList.txt", "r")
    for line in file:
        if country in line: 
            page = line[:2] + ".html" #finds name of the country's file
            break
    
    print page
      
    archive = zipfile.ZipFile("countries.zip", "r") #access a zip archive
    file2 = archive.open(page, "r")
    soup = BeautifulSoup(file2)
    
    possibilities = dict()
    
    
    
    for attr in soup.findAll("div", "category"):
    	aTag = attr.find("a")
    	if aTag: 
    		dataTag = attr.parent.parent.findNextSibling("tr").find("div", "category_data")
    		if dataTag:
    			#alot of the titles contain extra info after a " - " which is throwing off the search
    			title = formatKey(aTag.string)
    			data = dataTag.string
    			possibilities[title] = data
    	
    if key == ";lst":
    	for key in possibilities.keys():
    		print key + "," + possibilities[key]
    	return		
    	
    if key == ";keys":
    	for key in possibilities.keys():
    		print key
    	return
    
    results = get_close_matches(key, possibilities.keys())
    
    if key == ";matches":
    	for result in results:
    		print result
    	return

    
    if(len(results) == 0): print "I'm afraid I can't do that Dave."
    else:
    	for result in results:
    		print result + ": " 
    		print "\t" + possibilities[result]
    
def formatKey(key):
	words = key.split()
	
	temp = []
	for word in words:
		if word == "-":
			break
		else:
			temp.append(word)
	
	return " ".join(temp)
			

def getQuery():
	userInput = raw_input("What would you like to know?")
	wordsToRemove = ["how", "what", "the", "a", "an", "which", "of", "in", ",", ":", ".", "?", "is"]
	for word in wordsToRemove:
		userInput = userInput.replace(" " + word + " ", "")
		
	userInput = userInput.strip()	
		
	print userInput
	
	return userInput










if __name__ == '__main__':
    main()
    

