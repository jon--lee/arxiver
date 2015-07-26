#
# @author jonathan_lee@berkeley.edu (Jonathan N. Lee)
# 
# arxiver module which acts as the main interface for access
# to the scaping and compilation functions within the package.
# several comprehensive functions complete the tasks of accessing
# new publications and searching for publications.
#

# system libraries
# internal libraries
import papers
from parsers import NewPubl
from parsers import Search
# third party libraries


def get_new_publ(topic):
    parser = NewPubl('http://arxiv.org/')
    soup = parser.soupify('cs')
    return parser.parse(soup)

def search(search_query, max_results=30):
    parser = Search('http://export.arxiv.org/')
    soup = parser.soupify('electron', max_results)
    return parser.parse(soup)


