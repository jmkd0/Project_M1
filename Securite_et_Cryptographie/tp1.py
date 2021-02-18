import unicodedata

#Exercice 1
primes = [1,2,3]
def prime_number(N):
 for n in range(5,N):
  isTrue = True
  k = 1
  while k < len(primes):
   if n % primes[k] == 0:
    isTrue = False
    break
   else:
    k += 1
  if isTrue == True:
   primes.append(n)

#Exercice 2

def cesar(n, texte):
 chiff = ""
 alph_clair = [chr(i+65) for i in range(26)]
 alph_chiff = [chr((i+n)%26+65) for i in range(26)]
 texte = unicodedata.normalize('NFD', texte).encode('ascii','ignore').decode('ascii')
 texte = texte.upper()
 
 for letter in texte:
  if letter in alph_clair:
   chiff += alph_chiff[alph_clair.index(letter)]
  else:
   chiff += letter
 
 return chiff


def casser_cesar(n, texte):
 dechiff = ""
 alph_clair = [chr(i+65) for i in range(26)]
 alph_chiff = [chr((i+n)%26+65) for i in range(26)]
 texte = unicodedata.normalize('NFD', texte).encode('ascii','ignore').decode('ascii')
 texte = texte.upper()
 
 for letter in texte:
  if letter in alph_clair:
   dechiff += alph_clair[alph_chiff.index(letter)]
  else:
   dechiff += letter
 
 return dechiff

prime_number(50)
print(primes)

chiff = cesar(3, "l'ecole ça va bien")
print(chiff)
dechiff = casser_cesar(3, "O'HFROH FD YD ELHQ")
print( dechiff)
