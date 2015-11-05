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
        print "\t"+ "void set"+ majFirstLetter(att)+ "("+ typeDeDonnee +" &" + att +");\n"
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

def writePrivateAttrs(oneObject):
    i=0
    while i<len(oneObject.attributes):
        if ' ' not in oneObject.attributes[i]:
            print "error for : ", oneObject.attributes[i], "no specified type.\n"
            return 1
        typeDeDonnee =  oneObject.attributes[i].rsplit(' ', 1)[0]
        att = oneObject.attributes[i].rsplit(' ', 1)[1]
        print "\t"+ typeDeDonnee + " " + att + ";\n"
        i = i+1
    return 0

def writeOperatorCinAndCoutBody(oneObject):
    car = oneObject.className[0].lower()
    print "std::ostream& operator<<(std::ostream& flux, " + oneObject.className + " & " + car + ") {"
    print  "\t" + car + ".afficher(flux);"
    print "\treturn flux;"
    print "}\n"
    print "std::istream& operator>>(std::istream& flux, " + oneObject.className + " & " + car + ") {"
    print  "\t" + car + ".saisir(flux);"
    print "\treturn flux;"
    print "}"

def writeDotH(oneObject) :
    print "\n generation du code du fichier .h\n\n\n"
    print "class ", oneObject.className, "  { \n"
    print "public : \n"
    print "\t" + oneObject.className + "();\n"
    rtn = writeGetterAndSetter(oneObject)
    print "\n"
    rtn += writeFunctions(oneObject)
    print "private :\n"
    rtn+=writePrivateAttrs(oneObject)
    car = oneObject.className[0].lower()
    print "\n};\n"
    print "std::ostream& operator<<(std::ostream& flux, " + oneObject.className + " & " + car + ");"
    print "std::istream& operator>>(std::istream& flux, " + oneObject.className + " & " + car + ");"
    return rtn

def writeGetterAndSetterBody(oneObject) :
    i = 0
    while i<len(oneObject.attributes):
        if ' ' not in oneObject.attributes[i]:
            print "error for : ", oneObject.attributes[i], "no specified type.\n"
            return 1
        typeDeDonnee =  oneObject.attributes[i].rsplit(' ', 1)[0]
        att =  oneObject.attributes[i].rsplit(' ', 1)[1]
        print typeDeDonnee + " " + oneObject.className + "::get" + majFirstLetter(att)+ "() const {\n"
        print "\treturn this->" + att + ";\n"
        print "}\n"
        print "void " + oneObject.className + "::set"+ majFirstLetter(att)+ "("+ typeDeDonnee +" &" + att +") {\n"
        print "\t"+ "this->" + att + "=" + att + ";\n"
        print "}\n"
        i = i+1
    return 0

def writeFunctionsCpp(oneObject):
    i = 0
    while i<len(oneObject.publicFunctions):
        if ' ' not in oneObject.publicFunctions[i]:
            print "error for : ", oneObject.publicFunctions[i], "no specified type.\n"
            return 1
        typeDeDonnee =  oneObject.publicFunctions[i].rsplit(' ', 1)[0]
        functionName = oneObject.publicFunctions[i].rsplit(' ', 1)[1]
        print typeDeDonnee + " " + oneObject.className + "::" + functionName + "() {}\n"
        i = i+1
    return 0

def writeDotCpp(oneObject):
    print "\n generation du code du .cpp\n\n\n"
    print '#include "' + oneObject.className + '.h"\n\n\n'
    print "//constructor\n"
    print oneObject.className + "::" + oneObject.className + "() \n{}\n"
    rtn = writeGetterAndSetterBody(oneObject)
    rtn+= writeFunctionsCpp(oneObject)
    writeOperatorCinAndCoutBody(oneObject)
    return rtn
