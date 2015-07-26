#
# @author jonathan_lee@berkeley.edu (Jonathan N Lee)
#
# Search implements parser class which is designed to handle
# parsing of publications returned from searh query. Not all the
# fields of the paper object will be filled in as arxiv witholds some
# information.
#

# system libraries
import urllib
import xml.etree.ElementTree as ET

# internal libraries
from parser import Parser
from papers import Paper
# third party libraries


namespace = "{http://www.w3.org/2005/Atom}"

class Search(Parser):
    
    # returns the results of encoding the parameters
    # urlopen-ing the final url. data is converted to an etree
    def soupify(self, search_query, max_results):
        params = {
                "search_query": search_query,
                "max_results": max_results
                }
        url = self.url + "api/query?" + urllib.urlencode(params)
        data =urllib.urlopen(url)
        tree = ET.parse(data)
        return tree




    # given the eTree, parse the remaining elements
    # in order to extract information about documents
    # returned from the arxiv api search query in xml
    # element identifications are preceded by a namespace
    def parse(self, tree):
        
        papers = []
        root = tree.getroot()

        # index 7 is starting point of entries
        for entry in root[7:]:
            page = entry.find(namespace + 'id').text.replace('\n', ' ').strip()
            title = entry.find(namespace + 'title').text.replace('\n', ' ').strip()
            summary = entry.find(namespace + 'summary').text.replace('\n', ' ').strip()

            authors = [ author[0].text.replace('\n', ' ').strip() for author in entry.findall(namespace + 'author') ]

            paper = Paper(
                    title = title,
                    abstract = summary,
                    page = page,
                    authors = authors
                    )

            papers.append(paper)

        return papers
