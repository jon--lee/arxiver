#
# @author jonathan_lee@berkeley.edu (Jonathan N Lee)
# 
# NewPubl implements parser class which is designed to handling
# parsing of new publications on arxiv given a specific topic
# new publications papge is only html (no xml api)
#

# system libraries
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


class NewPubl(Parser):
    
    # soupify method takes in a topic, generates the url
    # to request given a valid topic. generates the soup
    # version the data and returns it. also sets instance field
    # equal to the soup
    def soupify(self, topic):
        raise NotImplementedError

    # given valid soup from the arxiv new topic page,
    # function parses the soup extracting information
    # that will create a list of Paper objects
    def parse(self, soup):
        raise NotImplementedError
