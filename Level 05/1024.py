casos = int(input())

for i in range(1, casos + 1):
    s= input()
        
    #important
    listString = [chr(ord(c) + 3) if c.isalpha() else c for c in s]
            
            
    listString.reverse()
    
    #important
    for i in range(len(listString) // 2, len(listString)):
        listString[i] = chr(ord(listString[i]) - 1) 
    listString = "".join(listString)
    print(listString)