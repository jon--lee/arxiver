import urllib2
import sys
import time
try:
    from BeautifulSoup import BeautifulSoup as bs
except ImportError:
    try:
        from bs4 import BeautifulSoup as bs
    except ImportError:
        sys.stderr.write(
                "Could not import BeautifulSoup or bs4.\n"
        )
        raise

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
        data = urllib2.urlopen(url)
        soup = bs(''.join(data), "html.parser")
        soup.prettify()
        soups[url] = soup
    
        
    # once we go through all elements, add to list
    papers = []
    
    # A note to the reader: it's very hard to understand this code. I recommend
    # looking at it side by side with the html source from arxiv.
    for dt in soup.find_all('dt'):
        
        # find the number of the new publication
        num_str = dt.a.string
        num = int(num_str[1:-1])
        
        # lots of information is stored in the Abstract element
        # get the element
        arxiv = dt.find(title='Abstract')
        
        # id is going to be two numbers separated by point with a prefix
        arxiv_id = arxiv.string[len(ID_PREFIX):]

        # page link is given in Abstract element
        page_link = BASE_URL[:-1] + arxiv['href']
        
        # pdf link can be deduced by using arxiv_id
        pdf_link = BASE_URL[:-1] + "pdf/" + arxiv_id

        # paper information is actually a sibling
        dd = dt.next_sibling.next_sibling
        title = dd.find(class_="descriptor").next_sibling[1:].rstrip()       # trim the space before the title

        # There may not be an abstract, there may not be any text in it
        abstract = None
        p = dd.div.p
        if p is not None and p.string is not None:
            abstract = p.string.replace('\n', ' ')
        
        # Multiple authors
        author_div = dd.find(class_='list-authors')
        authors = []
        for a in author_div.find_all('a'):
            author = { "name": a.string, "link": BASE_URL[:-1] + a['href'] }
            authors.append(author)                                           # adding list of authors of one paper ie "subauthors"  
        
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

def search(query):
    """
    returns results of api search queries
    @param query
    """


def get_valid_topics():
    """
    returns a list of valid topics from the homepage
    does not return valid subtopics.
    """
    


pubs = new_publications("math")
pub = pubs[30]
for key in pub:
    print ""
    print key + ": " + str(pub[key])
