#
# @author jonathan_lee@berkeley.edu (Jonathan N. Lee)
# 
# Parser interface module which abstract defines the structure
# of a general arxiv parser. Do not instantiate this abstract class.
# 

# system libraries
# internal libraries
# third party libraries


class Parser(object):
    

    # intializer sets instance field to the given
    # url for processing with other functions
    # @param url        provide the base url only (e.g. http://www.google.com/)
    #                   full urls will be constructed by implemented classes
    def __init__(url):
        self.url = url

    # soupify should make use of urllib in order to retrieve
    # data from the link and convert that raw data into a data
    # structure which can then be parsed
    def soupify(*args):

    # parse should parse the entire soup data structure
    # identify useful information and pack it into
    # a more useable and "interfaceable" data structure
    def parse(*args):
        raise NotImplementedError
