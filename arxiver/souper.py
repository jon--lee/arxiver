# system libraries
import urllib2

# third party libaries
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


def soupify(url):
    data = urllib2.urlopen(url)
    soup = bs(''.join(data), "html.parser")
    soup.prettify()
    return soup

