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
    
    
    possibilities = parseHtml(file2)
    
    	
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
    		print possibilities[result]
    		
def parseHtml(htmlFile):
	soup = BeautifulSoup(htmlFile)
    
	possibilities = dict()    
    
	for attr in soup.findAll("div", "category"):
		aTag = attr.find("a")
		if aTag: 
			trTag = attr.parent.parent.findNextSibling("tr")
    		
			if len(trTag) > 1:
				contents = []
				for div in trTag.findAll("div", "category"):
					if len(div.contents) > 0:
						contents.append(div.contents[0].strip())
						for span in div.find("span"):
							contents.append(span.string.strip())
    		
				for div in trTag.findAll("div", "category_data"):
					if div.string:
						contents.append(div.string)
    			
				data = "\r\n".join(contents)
			elif trTag.find("td"):
				data = trTag.find("td").find("div", "category_data").string
				print data
			else: 
				data = trTag.find("div", "category_data").string
    			
   		#alot of the titles contain extra info after a " - " which is throwing off the search
			title = formatKey(aTag.string)
   		
			if possibilities.has_key(title):
				data = possibilities[title] + "\r\n" + data
    			
			possibilities[title] = data
   		
	return possibilities
    
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
	userInput = raw_input("What would you like to know?").lower()
	wordsToRemove = ["how", "what", "the", "a", "an", "which", "of", "in", ",", ":", ".", "?", "is"]
	
	words = []
	for word in userInput.split():
		if word not in wordsToRemove:
			words.append(word)

	userInput = " ".join(words)
		
	print userInput
	
	return userInput










if __name__ == '__main__':
    main()
    

