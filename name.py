
from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP
 

def main(emotion):
 

    if(emotion == "Sad"):
        urlhere = 'http://www.imdb.com/search/title?genres=drama&amp;title_type=feature&amp;sort=moviemeter, asc'
 
    
    elif(emotion == "Disgust"):
        urlhere = 'http://www.imdb.com/search/title?genres=musical&amp;title_type=feature&amp;sort=moviemeter, asc'
 
    
    elif(emotion == "Anger"):
        urlhere = 'http://www.imdb.com/search/title?genres=family&amp;title_type=feature&amp;sort=moviemeter, asc'
 
    
    elif(emotion == "Anticipation"):
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&amp;title_type=feature&amp;sort=moviemeter, asc'
 
    
    elif(emotion == "Fear"):
        urlhere = 'http://www.imdb.com/search/title?genres=sport&amp;title_type=feature&amp;sort=moviemeter, asc'
 
    
    elif(emotion == "Enjoyment"):
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&amp;title_type=feature&amp;sort=moviemeter, asc'
 
    
    elif(emotion == "Trust"):
        urlhere = 'http://www.imdb.com/search/title?genres=western&amp;title_type=feature&amp;sort=moviemeter, asc'
 
    
    elif(emotion == "Surprise"):
        urlhere = 'http://www.imdb.com/search/title?genres=film_noir&amp;title_type=feature&amp;sort=moviemeter, asc'
 
    
    response = HTTP.get(urlhere)
    data = response.text
 
    # Parsing the data using
    # BeautifulSoup
    soup = SOUP(data, "lxml")
 
    # Extract movie titles from the
    # data using regex
    title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
    return title
 

