import time #conda install -c anaconda ipython
#Exercice 1
def compte_mots(chaine):
    return len(chaine.split(" "))

#Exercice 2
def remplace_multiple(s1, s2, n):
    k = 0
    while k < len(s2):
        pos = (k+1)*n
        if pos < len(s1):
            s1 = s1[:pos]+s2[k]+s1[pos+1:]
            k += 1
        else:
            s1 += s2[k:]
            break
    return s1

#Exercice 3
#Enonce 1
def termeU(n):
    if n == 0:
        return 1
    else:
        return termeU(n-1)*pow(2,n) + n
#Enonce 2
def serie(p):
    ser = 0
    for i in range(p+1):
        a = termeU(i)
        ser += a
    return ser
##Enonce 3
def serie_v2(p):
    ser = 0
    precedent = 1
    for i in range(p+1):
        if i == 0:
            ser = 1
        else:
            precedent = precedent*pow(2, i) + i
            ser += precedent
    return ser

def mesureTimeSerie(p):
    begin_serie_1 = time.perf_counter()
    s1 = serie(p)
    end_serie_1 = time.perf_counter()

    begin_serie_2 = time.perf_counter()
    s2 = serie_v2(p)
    end_serie_2 = time.perf_counter()
    print("Le premier algorithme a fait ",str(end_serie_1-begin_serie_1)," secondes")
    print("Le deuxieme algorithme a fait ",str(end_serie_2-begin_serie_2)," secondes")

#####Exercie 4
def factoriel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factoriel(n-1)


###########Exercice 1
#count_word = compte_mots("il ingurgite impunément un iguane.")
#print("Your chain contain", count_word,"words")

##########Exercice 2
#chain1 = remplace_multiple("abacus", "oiseau",2)
#chain2 = remplace_multiple("hirondelles", "nid",3)
#print(chain1)
#print(chain2)

###########Exercice 3
##Enonce 1
#terme = termeU(1)
#print(terme)
##Enonce 2
#ser = serie(5)
#print(ser)
##Enonce 3
#ser_v = serie_v2(5)
#print(ser_v)

##Enonce 5
#mesureTimeSerie(100)  
                    #####Le premier algorithme a fait  0.003928021003957838  secondes
                    #####Le deuxieme algorithme a fait  0.00013218300591688603  secondes
#mesureTimeSerie(300)
                    #####Le premier algorithme a fait  0.19399257900658995  secondes
                    #####Le deuxieme algorithme a fait  0.0025211309985024855  secondes
#mesureTimeSerie(400)
                    #####Le premier algorithme a fait  0.8190473849972477  secondes
                    #####Le deuxieme algorithme a fait  0.009440625988645479  secondes

####Exercice 4
fac = factoriel(4)
print("La factoriel donne", fac)

