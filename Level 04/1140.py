while True :
    
    frase = input()
    if frase == "*":
        break
    primeiras_letras = [palavra[0] for palavra in frase.split()]
    primeiras_letras = [letra.upper() for letra in primeiras_letras]
    boleano = True
    for i in range(len(primeiras_letras)-1):
        if primeiras_letras[i] != primeiras_letras[i+1]:
            boleano = False
            break
    
    if boleano == True:
        print("Y")
    else:
        print("N")  
        
        
    
        
    