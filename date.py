def dat(fichier):
    for el in fichier:
        if el == "-":
            barre = el.replace("-","/")
        barre1= barre.split("/") 
        for elem in barre1[1] :  
            if elem == "janvier" or elem=="Janvier" or elem == "JANVIER" or elem == "j" \
                or elem == "jan" or elem == "janv":
                elem=elem.replace (elem,"01")
            if elem == "fevrier" or elem == "FEVRIER" or elem == "fev" or elem == "Fev" \
                or elem =="fevr" :
                elem = elem.replace(elem,"02")
            if elem == "mars" or elem == "MARS" or elem == "Mars" or elem == "mar":
                elem == elem.replace(elem,"03") 
            if elem == "avril" or elem == "AVRIL" or elem == "Avril" or elem =="avr":
                elem = elem.replace(elem,"04")
            if elem == "mai" or elem == "MAI" or elem == "Mai" :
                elem = elem.replace(elem,"05")
            if elem == "juin" or elem == "JUIN"or elem == "Juin":
                elem =elem.replace(elem,"06")
            if elem == "juillet" or elem == "Juillet" or elem == "JUILLET" or elem == "juill":
                elem = elem.replace(elem,"07")
            if elem == "aout" or elem == "AOUT" or elem == "Aout":
                elem = elem.replace(elem,"08")
            if elem == "septembre" or elem == "SEPTEMBRE" or elem == "Septembre" or elem == "sept":
                elem = elem.replace(elem,"09")
            if elem == "octobre" or elem == "OCTOBRE" or elem == "Oct" or elem == "oct":
                elem = elem.replace(elem,"10")
            if elem == "NOVEMBRE" or elem == "novembre" or elem == "Nov" or elem == "nov":
                elem = elem.replace(elem,"11")
            if elem == "decembre" or elem == "DECEMBRE" or elem == "DEC" or elem == "Dec" or elem == "dec":
                elem = elem.replace(elem,"12")
        barre = "/".join(barre1)                                               
