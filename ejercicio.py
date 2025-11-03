def son_anargamas(a: str, b: str) -> bool:
    a=a.lower()
    b=b.lower()
     
    temp_a=[]
    for ch in a:
        if not ch.isspace():
            temp_a.append(ch)
    a="".join(temp_a)
 
    temp_b=[]
    for ch in b:
        if not ch.isspace():
            temp_b.append(ch)
    b="".join(temp_b)
    if len(a)!=len(a):
        return False
    
    conteo=()
    for ch in a:
        conteo[ch]=conteo.get(ch,0)+1
    
    for ch in b:
        if ch not in conteo:
            return False
        conteo[ch]-=1
        if conteo[ch]<0:
            return False
        
    for ch in conteo.values():
        if ch!=0:
            return False
    return True
    
buleano=son_anargamas("Amor","Roma")

if buleano:
    print ("Son anargamas")
