def revertir (string):
    if len (string)==0:
        return string
    else:
        return revertir(string[1:])+ string[0]

string='hola que tal'

print ('el string revertido es: ', (revertir(string)))