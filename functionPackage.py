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


def majFirstLetter(oneString) :
    j = 0
    output = ""
    for i in oneString:
        if j==0 :
            output += i.upper()
        else :
            output += i
        j = j + 1
    return output

def writeGetterAndSetter(oneObject) :
    i = 0
    while i<len(oneObject.attributes):
        if ' ' not in oneObject.attributes[i]:
            print "error for : ", oneObject.attributes[i], "no specified type.\n"
            return 1
        typeDeDonnee =  oneObject.attributes[i].rsplit(' ', 1)[0]
        att =  oneObject.attributes[i].rsplit(' ', 1)[1]
        print "\t"+ typeDeDonnee + " " + "get"+ majFirstLetter(att)+ "() const;\n"
        print "\t"+ "void set"+ majFirstLetter(att)+ "("+ typeDeDonnee +" " + att +");\n"
        i = i+1
    return 0

def writeFunctions(oneObject) :
        i = 0
        while i<len(oneObject.publicFunctions):
            if ' ' not in oneObject.publicFunctions[i]:
                print "error for : ", oneObject.publicFunctions[i], "no specified type.\n"
                return 1
            typeDeDonnee =  oneObject.publicFunctions[i].rsplit(' ', 1)[0]
            functionName = oneObject.publicFunctions[i].rsplit(' ', 1)[1]
            print "\t"+ typeDeDonnee + " " + functionName + "();\n"
            i = i+1
        return 0


def writeDotH(oneObject) :
    print "\n generation du code du fichier .h\n\n\n"
    print "class ", oneObject.className, " :  { \n"
    print "public : \n"
    rtn = writeGetterAndSetter(oneObject)
    print "\n"
    rtn += writeFunctions(oneObject)
    print "\n};"
    return rtn
