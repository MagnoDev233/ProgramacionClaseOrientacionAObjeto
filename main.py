print ("Halo evryguan, jawa iu fain thenkiu")


def son_anargamas(a: str, b: str) -> bool:
    a_min=a.lower()
    b_min=b.lower()
    
    temp_a=[]
    for ch in a_min:
        if not ch.isspace():
            temp_a.append(ch)
    a="".join(temp_a)
 
    temp_b=[]
    for ch in b_min:
        if not ch.isspace():
            temp_b.append(ch)
    b="".join(temp_b)
 
son_anargamas("Amor","Roma")
