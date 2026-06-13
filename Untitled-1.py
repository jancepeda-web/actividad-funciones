def dividir (a,b):
    if b == 0:
        return "error:no se puede dividir por cero." 
    return a / b

print ("probando division normal:" , dividir (10,2))
print (" probando validacion de cero:" ,dividir (10,0))
