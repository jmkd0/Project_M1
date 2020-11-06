import math
#Exercice 1
#La fonction isocele prend 3 valeurs double en arguments et retourne un boolean
#Elle determine si les valeurs a, b, c forment un triangle isocele
#

def isocele(a,b,c):
    u = (a+b+c)/2   
    if a > 0 and b > 0 and c > 0 and a < u and b < u and c < u: #test si a,b,c peut former un triangle 
        if a == b or a == c or b == c:
            return True
        else:
            return False
    else:
        return False

isisocele = isocele(4,4,4)
print("Exercice 1: Le triangle est isocele ?: ",isisocele)

#Exercice 2
#La fonction aire_ordonne prend en argument 3 valeurs et retourne l'aire du triangle
def aire_ordonne(a, b, c):
    u1 = min(a,b,c)
    u3 = max(a,b,c)
    u2 = sum([a,b,c]) - u1 - u3
    aire = (1/2)*math.sqrt(u1**2 * u3**2 - ((u1**2 - u2**2 + u3**2)/2)**2)
    return aire

aire = aire_ordonne(4,2,3)
print("Exercice 2: Le triangle a pour aire: ",aire)

#Exercice 3
#La fonction definit_triangle prend en argument 3 valeurs et retourne un boolean
#
def definit_triangle(a, b, c):
    u = (a+b+c)/2
    if a > 0 and b > 0 and c > 0 and a < u and b < u and c < u:
        return True
    else:
        return False

istriangle = definit_triangle(1,1,20)
print("Exercice 3: Le triangle est un triangle ?: ",istriangle)

#Exercice 4
#Cette fonction prend en argument deux valeurs entier n et p et qui retourne le nombre de triangle 
#dont les cotés sont des entiers compris entre n et p
#ELle affiche aussi les valeurs de chaque triangle
def nb_triangles_speciaux(n, p):
    cpt = 0
    tab = []
    for a in range(n, p+1):
        for b in range(n, p+1):
            for c in range(n, p+1):
                if definit_triangle(a, b, c):
                    if aire_ordonne(a,b,c) == a+b+c:
                        cpt += 1
                        t = [a,b,c]
                        t.sort()
                        if t not in tab:
                            tab.append(t)
    print("Exercice 4: Les triangles possible sont: ",tab)                        
    return len(tab)

triangles = nb_triangles_speciaux(1,20)
print(" On a : ",triangles, " triangles")





#EXEMPLE DE SORTIE

#Exercice 1: Le triangle est isocele ?:  True
#Exercice 2: Le triangle a pour aire:  2.9047375096555625
#Exercice 3: Le triangle est un triangle ?:  False
#Exercice 4: Les triangles possible sont:  [[5, 12, 13], [6, 8, 10], [7, 15, 20], [9, 10, 17]]
# On a :  4  triangles