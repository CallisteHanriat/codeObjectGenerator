def fillingLists(componant) :
    attributes= []
    i = 1
    typeEntry = "oneThing"
    while typeEntry != "":
        print "name of ", componant, i, " : "
        typeEntry = raw_input()
        i = i+1
        if (typeEntry  != "") :
            attributes.append(typeEntry)
    return attributes



def writeDotH(oneObject) :
    print "\n generation du code du fichier .h\n\n\n"
    i = 0
    print "class ", oneObject.className, " :  { \n"
    print "public : \n"
    while i<len(oneObject.attributes):
        if ' ' not in oneObject.attributes[i]:
            print "error for function : ", oneObject.attributes[i], "no specified type.\n"
            return 1
        typeDeDonnee =  oneObject.attributes[i].rsplit(' ', 1)[0]
        att =  oneObject.attributes[i].rsplit(' ', 1)[1]
        print "\t"+ "get"+ att+ "() const;\n"
        print "\t"+ "set"+ att+ "("+ typeDeDonnee +" " + att +");\n"
        i = i+1
    print "\n};"
    return 0
