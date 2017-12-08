
# coding: utf-8

# # Comp 1
# 
# Peter Vanya
# 
# Jarná škola FX, marec 2016
# 
# Programovanie posúva teóriu bližšie k experimentom tam, kde teória nestačí (skoro všade, analyticky riešiteľných problémov je minimum). V škole (na strednej alebo vysokej) sa programovanie moc neučí, tak vám ho v plnej kráse prinášame my.
# 
# ## Ideme sa učiť Python
# V tomto kurze sa naučíme komunikovať v jazyku Python (názov odvodený od *Monty Python*, nie toho hada), konkrétne verzie 3 (inak sa ešte používa verzia 2.7). 
# 
# ### Výhody
# Na rozdiel od prastarých jazykov ako Pascal a C, a modernejších ako C++:
# 
# * general-purpose, použiva sa na weby ako aj *high-performance computing* (= vo vede)
# * netreba ho kompilovať, stačí len písať kód a stláčať Enter (v tomto prípade Shift+Enter)
# * ľahko v ňom možno zadefinovať pre vedu užitočné koncepty ako vektory a matice (príp. tenzory vyššieho rádu; obsahuje obrovské množsvo algoritmov na diferenciálne rovnice, Fourierove transformácie, alebo prakticky hocičo dôležité
# * je príjemný na čítanie a písanie
# * vynikajúca dokumentácia ([docs.python.org](http://docs.python.org) alebo Stack Overflow)
# 
# ### Nevýhody
# V porovnaní s C++ a Fortranom je pomalý. To sa dá občas napraviť rôznymi spôsobmi zlepšiť, napr.:
# * integrovaním kód Fortranu pre časovo náročné výpočty (v prípade záujmu sa ma spýtajte osobne)
# * použitím knižinice [Numba](http://numba.pydata.org) Ako? (*Numba works by generating optimized machine code using the LLVM compiler infrastructure at import time, runtime, or statically (using the included pycc tool). Numba supports compilation of Python to run on either CPU or GPU hardware, and is designed to integrate with the Python scientific software stack.*)
# 
# ## Čo ešte sa naučíme
# V obmedzenej miere, ale predsa budete mať šancu zoznámiť sa s nasledovnými konceptami:
# * *git*, version control system
# * *IPython notebook*, po novom Jupyter (Julia, Python, R, tri programovacie jazyky budúcnosti). To, na čo sa práve pozeráte, i.e. písaný text a kód pomedzi to v prehliadači
# 
# ## Osnova
# 1. Základy: premenné, for cyklus, užitočné koncepty v Pythone
# 2. Matematické operácie: vektory, matice, skalárne a vektorové súčiny
# 3. Input/output: načítavanie zo a písanie do súborov
# 4. Fyzika! Derivovanie, integrovanie, riešenie difiek
# 
# ## Ako sa efektívne učiť
# * *Practice makes perfect*. Kvantita (snahy) produkuje kvalitu. Čím viac toho poskúšate, tým hlbšie do pamäti sa vám to zaryje
# * Ak niečomu nerozumiete, formulujte otázku, čomu presne, a niekde si ju zapíšte. Potom sa nad ňou zamyslite alebo sa ju niekoho (kamaráta alebo prednášajúceho) spýtajte
# 
# Poďme na to!

# ## Premenné

# In[4]:

# toto je komentar, pre istotu nepiseme s diakritikou
# pre vyhodnotenie bunky stlacte Shift+Enter
a = 5
type(a)


# In[5]:

float


# In[6]:

# typ premennej je automaticky uhadnuty
b = 0.2
type(b)


# In[7]:

print(a)    # vsimnite si zatvorky okolo! Novinka v Python3
a=1
print(a/2)
print(a//2) # celociselne delenie
print(a%2)  # zvysok po deleni


# In[6]:

a+b    # scitanie


# In[9]:

b=3
b**2   # umocnenie


# ## Strings

# In[15]:

c = "abc"
type(c)


# Jednotlivé stringy možno meniť na čísla, *float* alebo *int*.

# In[17]:

s = "123"
si = int(s)
print(si)
sf = float(s)
print(sf)


# ... a naopak, z čísel do stringu

# In[22]:

d = 123
ds = str(d)
print(ds + "_" + "s")


# O stringoch viac pozajtra (3. deň). Dnes spomeňme, že ich možno ľahko premeniť na pole:

# In[18]:

s = "123"
print(len(s))
list(s)


# ## Lists
# *List* je usporiadaný zoznam prvkov, ktorý možno meniť, napr. `a = [1,2,3]`
# 
# Okrem toho existuje *tuple*, ktorý sú nemenný, napr. `a = (1, 2, 3)`
# 

# In[20]:

a = [1, 2, 3]
print(a)
b = [2, 5]
c = a + b        # pozor na scitanie listov!
print(a + b)
#print(a-b)      # Error, vyskusajte


# Prístup k prvkom:

# In[22]:

print(a[0])   # prvy element, cislovanie zacina nulou!
print(a[-1])  # posledny element
#a[3]   # Error: list index out of range
a[0] = 5
print(a)      # prvy element zmeneny
print(a[10])


# Rôzne operácie:

# In[26]:

# dlzka listov
print(len(a))
# suma clenov
sum(a)
print(sum(a))
# pripoj dalsie cislo
a.append(10)
print(a)


# Listy možno usporiadať.

# In[33]:

v = [5, 3, 8, 1]
print(v)
v.sort()
for i in reversed(v):
    print(i)
print(v)


# In[35]:

# specificke listy
r = range(10)
print(r)
r = list(r)
print(r)
print(len(r), sum(r))

# rozne ine moznosti, vseobecna struktura
# range(first, last, increment)
print(list(range(1,10,2)))
print(list(range(10,1)))    # prazdny list
print(list(range(10,1,-1)))


# In[39]:

a=range(5)
print(a)
a[2]
print(type(a))


# Krátko o tuploch.

# In[51]:

t = (1, 2)
print(t)
print(sum(t))    # podobne operacie ako na listoch
t[1] = 3         # error! Tuple nemozno menit


# ## For cyklus

# In[62]:

for i in range(10):
    print(i**2)


# In[45]:

for i in "abc":   # tlacit mozno aj stringy
    print(i)


# In[ ]:




# ## List comprehension
# Zjednodušený for cyklus v Pythone na jeden riadok, veľmi užitočná vec.

# In[43]:

a = [print(i**2) for i in range(10)]
print(a)
b = [i*i for i in range(10)]
print(b)
A = [[i+j for i in range(5)] for j in range(5)]   # matica (list listov), len nie pekne zapisana
print(A)
print(np.array(A))
A[1][3]   # pristup k jednotlivym prvkom matice


# ## Funkcie
# Základný stavebný prvok programovacieho jazyka.
# 
# Funkcie v Pythone môžu vracať viacero premenných (na rozdiel C/C++ a Fortranu).

# In[9]:

def plus(a, b):
    return a + b


# In[10]:

print(plus(1, 2))
print(plus(3.2, -1))


# In[48]:

# vo funkcii mozu byt defautlne premenne
def plus2(a, b=2):
    return a + b

print(plus2(7))
print(plus2(7,4))


# In[15]:

# ciferny sucet, elegantne
def cif_sucet(a):
    return sum([int(i) for i in str(a)])


# In[20]:

cif_sucet(123)


# In[21]:

# co sme spravili?
b = 234
[int(i) for i in str(b)]


# ***
# ## [Problem]
# V Prima Banke ponúkajú vklad s 5% ročným úrokom. Ak budete počas jedného roka každý mesiac vkladať 50 eur, na konci mesiaca vám pribudne 5% per annum z celkovej sumy, ktorú v tom čase máte na účte. Koľko eur na konci roka zarobíte?
# ***

# ## Komplexné čísla

# In[49]:

z = 1 + 2j
print(z)
print(type(z))


# In[54]:

z*z


# In[55]:

z.conjugate()


# In[50]:

print(z.real)
print(z.imag)


# In[69]:

from math import sqrt
sqrt((z*z.conjugate()).real)
abs(z)
np.angle(z)


# ## Podmienky

# In[71]:

a = 5
if a == 2:
    print("a sa rovna dva")
elif a == 3 or a == 4:
    print("a sa rovna tri")
else:
    print("a sa nerovna dva ani tri")


# ---
# ## [Problem]
# Zoberte číslo (napr. 1987) a spočítajte jeho ciferný súčet.
# 
# ---
# ## [Problem]
# Nájdite súčet všetkých čísel deliteľných 3 alebo 5 menších ako 100.
# 
# ---
# ## [Problem] [Adv]
# Napíšte funkciu, ktorá mi rozhodne, či je dané číslo prvočíslo.
# 
# Nájdite súčet všetkých prvočísel do 100.

# In[76]:

# Problem 1
a = 1987
print([i for i in str(a)])
print(sum([int(i) for i in str(a)]))


# In[77]:

# Problem 2
sum([i for i in range(101) if i%3 == 0 or i%5 == 0])


# In[2]:

# Problem 3
def isprime(n):
    for i in range(2, n//2+1):
        if n%i == 0:
            return False
    return True


# In[4]:

print([i for i in range(2, 101) if isprime(i)])
sum([i for i in range(2, 101) if isprime(i)])


# In[ ]:



