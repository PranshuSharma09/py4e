while True:
    age = input ("age : ")
    x = int (18) - int(age)
    if int(age) < int(18) :
        print ("wait for", x,"years and try again")
        continue
    else :
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
        break
