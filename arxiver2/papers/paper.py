#
# @author jonathan_lee@berkeley.edu (Jonathan N Lee)
#
# Paper module that defines the characteristics of a paper
# class is designed as a psuedo data structure that involves
# functions associated with processing paper information
#
# No functions exist yet but the intent is that this module is
# extensible.
#

# system libraries
# internal libraries
# third party libraries

class Paper(object):
    def __init__(self, **kwargs):
        self.title = kwargs['title']
        self.abstract = kwargs['abstract']
        self.arxiv_id = kwargs['arxiv_id']
        self.pdf = kwargs['pdf']
        self.page = kwargs['page']
        self.authors = kwargs['authors']




paper = Paper(title='this is my title', abstract='this is my abstract')
print paper.abstract
