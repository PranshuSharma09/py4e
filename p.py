language = input("lang : ")
na = input("name : ")
def greet (language):
    if language == 'esp' :
        return 'hola'
    elif language == 'fr' :
        return 'bojour'
    elif language == 'hindi' :
        return 'namaste'
    else:
        return 'hello'
print (greet (language), na)
