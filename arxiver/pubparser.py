
ID_PREFIX = "arxiv:"

dt = None
dd = None


# find the number of the new publication
def num():
    global dt
    num_str = dt.a.string
    return int(num_str[1:-1])


# lots of information is stored in the Abstract element
# get the element
def arxiv():
    global dt
    return dt.find(title='Abstract')


# id is going to be two numbers separated by point with a prefix
def arxiv_id(arxiv): 
    arxiv_id = arxiv.string[len(ID_PREFIX):]
    return arxiv_id


# page link is given in Abstract element
def page_link(arxiv, url):
    page_link = url + arxiv['href']
    return page_link


# text that follows descriptor
def title():
    title = dd.find(class_="descriptor").next_sibling[1:].rstrip()       # trim the space before the title
    return title


# multiple authors
def authors():
    author_div = dd.find(class_='list-authors')
        authors = []
        for a in author_div.find_all('a'):
            author = { "name": a.string, "link": BASE_URL[:-1] + a['href'] }
            authors.append(author)                                           # adding list of authors of one paper ie "subauthors"  
        

