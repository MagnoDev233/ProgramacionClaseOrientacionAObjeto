print ("Halo evryguan, jawa iu fain thenkiu")


def son_anargamas(a: str, b: str) -> bool:
 a_lower = a.lower()
 b_lower = b.lower()
 
 a_clean = "".join(a_lower.split())
 b_clean = "".join(b_lower.split())
 
 if len(a_clean) == len(b_clean):
     return False
 return sorted(a_clean) == sorted(b_clean)
