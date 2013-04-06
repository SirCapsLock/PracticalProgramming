'''
Created on Mar 28, 2013

@author: Kiks
'''

import urllib2
import json


#https://api.instagram.com/v1/tags/{tag-name}/media/recent
puppURL = "https://api.instagram.com/v1/tags/cockerspaniel/media/recent?client_id=f297ecbb75d3410fb19ae2e013698ca5"

def printPuppies(puppyURL):
    
    #Get the response from the API
    puppyResponse = urllib2.urlopen(puppyURL)
    
    '''
    *Want to read the contents of a regular file?*
    myFile = open('myFile.txt') <-- path relative to python file
    stringOfMyFilesContents = myFile.read()
    listOfLinesInMyFile = myFile.readLines()
    Easy, eh?
    '''
    
    #convert to JSON
    puppyJSON = json.loads(puppyResponse.read())
    
    #navigate to the primary "data" dictionary which containts all the pic info
    puppyData = puppyJSON["data"] #list of instagram photos
    
    for puppy in puppyData:
        thisPuppyLink = puppy["link"] #the instagram link to this photo (NOT the source image!)
        
        #v Good example of traversing your response - Easy, eh?
        #this is the source image
        thisPuppy = puppy["images"]["standard_resolution"]["url"]
        #Build that string!
        imgTag = "<img src='" + thisPuppy + "'>"
        print( imgTag )
    
    #return the next URL of data from the API
    return puppyJSON["pagination"]["next_url"]

numPages = 10   #number of pages of photos (I believe we get 20 each page)
                #10 = 200 KITTENS! (or dogs, or cocker spaniels...)
                
count = 0       #count just to keep track of which page we're printing
nextURL = puppURL   #initialize to original URL
while count <= numPages:
    print( "**New Page:" + str(count) + "**")
    nextURL = printPuppies(nextURL)    
    count += 1




