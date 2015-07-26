#
# @author jonathan_lee@berkeley.edu (Jonathan N Lee)
# 
# NewPubl implements parser class which is designed to handling
# parsing of new publications on arxiv given a specific topic
# new publications papge is only html (no xml api)
#

# system libraries
import urllib2
# internal libraries
from papers import Paper
from parser import Parser

# third party libraries
try:
    from BeautifulSoup import BeautifulSoup as bs
except ImportError:
    try:
        from bs4 import BeautifulSoup as bs
    except ImportError:
        sys.stderr.write("Could not import BeautifulSoup or bs4.\n")
        raise


# constants
ID_PREFIX = 'arxiv:'


class NewPubl(Parser):
    
    # soupify method takes in a topic, generates the url
    # to request given a valid topic. generates the soup
    # version the data and returns it. also sets instance field
    # equal to the soup
    def soupify(self, topic):
        url = self.url + "list/" + topic + "/new"
        data = urllib2.urlopen(url)
        soup = bs(''.join(data), "html.parser")
        soup.prettify()
        return soup





    # given valid soup from the arxiv new topic page,
    # function parses the soup extracting information
    # that will create a list of Paper objects
    def parse(self, soup):
        papers = []
        
        for dt in soup.find_all('dt'):
            
            # dt element contains location/link information
            arxiv = dt.find(title='Abstract')
            arxiv_id = arxiv.string[len(ID_PREFIX):]
            
            # links to page and pdf
            page = self.url + arxiv['href'][1:]
            pdf = self.url + "pdf/" + arxiv_id

            # dd element that contains content information
            dd = dt.next_sibling.next_sibling

            title = dd.find(class_='descriptor').next_sibling[1:].rstrip()

            # abstract may be absent
            abstract = None
            p = dd.div.p
            if p is not None and p.string is not None:
                abstract = p.string.replace('\n', ' ')
            
            # must account for multiple authors (with name and link to page)
            author_div = dd.find(class_='list-authors')
            authors = []
            for a in author_div.find_all('a'):
                author = { "name":a.string, "link": self.url + a['href'][1:] }
                authors.append(author)

            paper = Paper(
                    title=title,
                    abstract=abstract,
                    arxiv_id=arxiv_id,
                    pdf=pdf,
                    page=page,
                    authors=authors
                    )

            papers.append(paper)
            

        return papers
