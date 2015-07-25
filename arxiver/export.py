# system libraries
import urllib
import xml.etree.ElementTree as ET

namespace = "{http://www.w3.org/2005/Atom}"


def parse_query(data):
    """
    ElementTree doesn't read the search queries well, 
    so a lot of tricks must be used
    
    # set the parameters for query
    params = {
            "search_query": query,
            "max_results": max_results
    }
    
    # construct query with constant base url and parameters
    url = API_URL + urllib.urlencode(params)
    data =  urllib.urlopen(url)
    tree = ET.parse(data)
    root = tree.getroot()
    """
    tree = ET.parse(data)
    root = tree.getroot()
    
    # index 7 is the starting point of the entries
    # for each paper
    papers = []
    for entry in root[7:]:
        page_link = entry.find(namespace + 'id').text.replace('\n', ' ').strip()
        title =     entry.find(namespace + 'title').text.replace('\n', ' ').strip()
        summary =   entry.find(namespace + 'summary').text.replace('\n', ' ').strip()
        
        # list of authors for each paper because there may be multiple
        authors = [  author[0].text.replace('\n', ' ').strip() for author in entry.findall(namespace + 'author')   ]
        
        papers.append( {
                "page_link": page_link,
                "title": title,
                "abstract": summary,
                "authors": authors
                }
        )
    
    # return read data as basic python data structure        
    return papers
