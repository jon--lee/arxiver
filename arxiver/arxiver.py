# system libraries
import urllib2
import urllib
import sys
import time

# third party libraries

# internal libraries
import souper
import pubparser as pp
import export




API_URL = "http://export.arxiv.org/api/query?"
BASE_URL = "http://arxiv.org/"
ID_PREFIX = "arxiv:"

soups = {}

def new_publications(topic, request=False):
    """
    list of dictionaries of 30 newest publications
    of given topic.
    dictinoary contains: number, page link, pdf link, title, list of authors (including links), subjects, abstract, arxiv id
    @param topic    must be a valid topic. see: get_valid_topics()             
    """
    global soups
    

    # optimize so that multiple requests for the same html are not made
    # keeping a "history" of requests unless user specifies otherwise (ie to get
    # newest results
    url = BASE_URL + "list/" + topic + "/new"
    if url in soups and not request:
        soup = soups[url]
    else:
        soup = souper.soupify(url)
        soups[url] = soup
    
        
    # once we go through all elements, add to list
    papers = []
    
    # A note to the reader: it's very hard to understand this code. I recommend
    # looking at it side by side with the html source from arxiv.
    for dt in soup.find_all('dt'):
        
        pp.dt = dt
        
        num = pp.num()

        arxiv = pp.arxiv()
        arxiv_id = pp.arxiv_id(arxiv)
        page_link = pp.page_link(arxiv, BASE_URL)
        
        # pdf link can be deduced by using arxiv_id
        pdf_link = BASE_URL + "pdf/" + arxiv_id

        # paper information is actually a sibling    
        pp.dd = dt.next_sibling.next_sibling

        title = pp.title()
        abstract = pp.abstract()
        authors = pp.authors(BASE_URL)
        

        # put it all together in dictionary
        papers.append(
            {
                "num": num,
                "title": title,
                "arxiv_id": arxiv_id,
                "page_link": page_link,
                "pdf_link": pdf_link,
                "authors": authors,
                "abstract": abstract
            }
        )
    
    return papers



def search(query, max_results=30):
    """
    returns results of api search queries
    @param query
    """

    params = {
        "search_query": query,
        "max_results": max_results
    }
    url = API_URL + urllib.urlencode(params)
    data = urllib.urlopen(url)
    
    # returned parsed xml from page
    return export.parse_query(data) 


def get_valid_topics():
    """
    returns a list of valid topics from the homepage
    does not return valid subtopics.
    """
    

