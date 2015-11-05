import string
from functionPackage import *

class OneClass(object):
    """docstring for OneClass"""
    def __init__(self, className, attributes, publicFunctions):
        super(OneClass, self).__init__()
        self.className = className
        self.attributes = attributes
        self.publicFunctions = publicFunctions


def main():
    print "Generation of c++ code : \n"
    className = raw_input("name of class you want to generate : ")
    print "Generation de la classe ", className
    attributes = fillingLists("attributes")
    print (attributes)
    publicFunctions = fillingLists("publicFunctions")
    print(publicFunctions)
    myClass = OneClass(className, attributes, publicFunctions)

    if(writeDotH(myClass) == 0):
        print "\n\n\n\n\n//End of printing H."
    if(writeDotCpp(myClass) == 0):
        print "\n\n\n\n\n//End of printing Cpp."

main()
