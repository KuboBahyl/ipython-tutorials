
# coding: utf-8

# # Comp 3
# 
# Peter Vanya
# 
# Jarná škola FX, marec 2016
# 
# ## Program na dnes
# Práca so súbormi, tlačenie a načítanie dát.

# ## Za pomoci numpy
# 
# Najjednoduchší spôsob za pomoci dvoch príkazov: `np.loadtxt` a `np.savetxt`.

# In[1]:

# najjednoduchsi sposob
import numpy as np
import os

a = np.arange(10)
print(a)
fname = "subor.out"
np.savetxt(fname, a)   # vektor ulozeny v subor.out
os.listdir(".")        # je tam, ale pozor na formatovanie


# In[2]:

cat subor.out


# In[5]:

# opatovne nacitanie
b = np.loadtxt("subor.out")
b    # premena z int na float


# ## Štandardný Python

# In[10]:

veta = "toto je veta"
fname = "veta.out"

# spravny sposob
with open(fname, "w") as f:
    f.write(veta)
        
# alebo na jeden riadok
open(fname, "w").write(veta + "42" + veta)


# In[7]:

# nacitanie
veta = open(fname, "r").read()
print(veta)
print(len(veta))    # dlzka


# ## Operácie so stringom [Adv 1]
# Python má perfektné možnosti manipulácie stringov, stojí za to sa ich naučiť (napr. ak raz budete chcieť scrapovať internet alebo "čítať" emaily)

# In[12]:

print(veta)
print(veta.split())              # rozdel podla medzier
print(veta.split("t"))           # rozdel podla znaku t


# In[15]:

print("_333_".join(veta.split()))    # spoj naspat podla zelaneho znaku


# Realny text:

# In[2]:

fname = "eminem.out"
lyric = open(fname, "r").read()
print(len(lyric))                   # pocet znakov
print(len(lyric.split()))           # pocet slov


# In[3]:

# inak
lyric = open(fname, "r").readlines()
len(lyric)        # pocet riadkov


# In[4]:

print(lyric[:50])


# In[5]:

# najdime nejake slovo
word = "mother"
zoznam_riadkov = [l for l in lyric if word in l]
zoznam_riadkov


# In[6]:

[i**2 for i in range(10)]


# In[7]:

lyric = open("eminem.out", "r").readlines()
#print(lyric[:100])
hot_vety = [l for l in lyric if "hot" in l]
hot_slova = [slovo for slovo in " ".join(hot_vety).split() if "hot" in slovo]
print(hot_slova)
hot_slova = [s.rstrip(".") for s in hot_slova]
hot_slova = [s.rstrip(",") for s in hot_slova]
hot_slova



# ## Reálne dáta
# 
# Zoberme si xyz súbor `dump.xyz`.
# * Prvy riadok: počet atómov
# * Druhý riadok: komentár
# * Zvyšné riadky: typ atómu a súradnice

# In[9]:

cat dump.xyz


# In[10]:

fname = "dump.xyz"
A = open(fname).readlines()
A[:2]


# In[11]:

A[2:]


# In[12]:

B = A[2:]
B = [[float(i) for i in line.split()] for line in B]

# Pozor! V numpy maticiach nemozno spravit jeden stlpec typu int
# a iny typu float
#B[:, 0] = [int(B[i, 0]) for i in B[:, 0]]
#B[:, 0] = B[:, 0].astype(int)   # nejde
B


# ## Alternatívne...
# 
# ... vyrobme si objekt a uložme atómové typy a xyz maticu do rôznych atribútov.

# In[14]:

class xyzMatica():
    def __init__(self):
        self.types = []
        self.xyz = np.array([[]])
        self.pozdrav = "ahoj Fero"
    
    def read(self, fname):
        A = open(fname).readlines()
        A = [line.split() for line in A[2:]]
        A = np.array(A).astype(float)
        self.types = A[:, 0].astype(int)
        self.xyz = A[:, 1:4]
        


# In[15]:

moja_matica = xyzMatica()
moja_matica.types


# In[16]:

moja_matica.xyz


# In[17]:

# teraz do objektu nacitajme data
mat = xyzMatica()
mat.read("dump.xyz")
mat.types


# ***
# ## [Problem]
# 
# Načítajte *Lose yourself* a nájdite počet prázdnych riadkov.
# ***

# In[18]:

lyric = open("eminem.out", "r").readlines()
prazdne = [line for line in lyric if line == "\n"]
len(prazdne)


# In[ ]:



