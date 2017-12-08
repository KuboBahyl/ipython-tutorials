
# coding: utf-8

# # Comp 2
# 
# Peter Vanya
# 
# Jarná škola FX, marec 2016
# 
# ## Program na dnes
# 
# * Matematické operácie, vektory a matice. Hľadanie vlastných čísel. 
# * Prvé zoznámenie sa s knižnicami `numpy` a `matplotlib`.

# In[14]:

# najskor nacitame kniznice
# toto je vseobecne zauzivana konvencia, nemente ju!
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# ## Vektory

# In[3]:

a = np.array([1, 2, 3])
print(a)
print(type(a))

b = np.array([2, 3, 4])
print(a + b)    # spravne scitanie!


# In[4]:

np.dot(a, b)    # skalarny sucin
a.dot(b)


# In[5]:

np.cross(a, b)  # vektorovy sucin


# In[7]:

np.outer(a, b)  # outer product (jak sa to povie po slovensky?), premyslite si


# ## Matice

# In[6]:

A = np.array([[0, 1], [1, 0]])
print(A)
type(A)


# In[7]:

AA = np.matrix(A)   # premena na iny datovy typ
type(AA)


# In[8]:

B = np.array([[1, 0], [0, -1]])
print(B)


# In[11]:

np.dot(A, B)


# In[12]:

# pozor!
A*B


# In[14]:

# Vlastnosti numpy matic
len(A)   # pocet riadkov


# In[15]:

A.shape   # rozmery


# In[16]:

# uzitocne vektory/matice, konvencia z Matlabu
N = 3
np.ones(N)      # konstantny vektor


# In[29]:

np.ones((N, N))    # jednotky


# In[30]:

np.eye(N)       # identita


# In[20]:

np.zeros((N, N+1))      # nulova matica NxN


# In[24]:

# spajanie matic
A = np.ones((3, 3))
B = np.eye(3)
print(A, "\n")
print(B)
np.hstack((A, B))


# ### Prístup k prvkom

# In[34]:

A = np.arange(9).reshape((3, 3))
A


# In[35]:

A[1, 1]


# In[36]:

A[1][1]


# In[40]:

A[-1, -1] = 10
A


# In[41]:

A[0, 0]


# In[44]:

A[-3, -2]


# ## Slicing
# 
# Ako vyberať jednotlivé stĺpce a riadky matíc?

# In[4]:

A = np.arange(9)
A = A.reshape((3, 3))
A


# In[5]:

A[:, 0]


# In[6]:

A[1, :]


# In[7]:

A[[0, 2], :]


# In[8]:

# zmena riadku
A[:, 1] = 4
A


# In[9]:

# pripocitanie cisla k stlpcu
for i in range(len(A)):
    A[i, 2] += 100

A


# In[10]:

A = np.arange(25).reshape((5, 5))
A


# In[11]:

A[2:, 3]


# ## Generovanie (pseudo)náhodných čísel

# In[80]:

# cisla sa menie, pokial nefixneme seed!
np.random.seed(12)

N = 5
a = 2*np.random.rand(N)   # v intervale [0,1]
a


# In[81]:

A = np.random.rand(N, N)
A


# In[88]:

a = np.random.randn(5)
a


# In[107]:

mu, sigma = 1.0, 2.0
a = np.random.randn(1000)*sigma + mu
plt.hist(a, bins=20)
plt.show()


# In[131]:

a = np.random.randint(10, size=1000)   # cele cisla, pozor na size!
u = plt.hist(a)
#plt.plot(u[1][1:], u[0])


# ## Vlastné čísla
# 
# $$ A v = \lambda v$$
# Použijeme funkciu `eig`.
# 
# Okrem nej existujú ešte funkcie na vlastné čísla symetrických alebo hermitovských matíc `eigs` a `eigh`.

# In[95]:

from numpy.linalg import eig


# In[106]:

N = 20
A = np.random.rand(N, N)
vals, vecs = eig(A)
print(vals.real)


# ## Matematické funkcie

# In[12]:

import math
print(math.__dict__.keys())  # alebo dir(math)
len(dir(math))


# In[4]:

math.pi


# In[5]:

math.cos


# In[132]:

math.cos(math.pi/2)


# ## Grafy

# In[15]:

import matplotlib
matplotlib.rcParams.update({'font.size': 16})

x = np.linspace(0, 2*math.pi, 100)
y = np.sin(x)
plt.plot(x, y, "r*")     # cervene hviezdicky
plt.xlabel("$x$")
plt.ylabel("$\sin(x)$")
plt.xlim([0, 2*math.pi])
plt.show()


# In[148]:

np.linspace(0, 1, 11)


# ## Pár slov k štylistike
# Python má svoje štylistické štandardy PEP 8, ktoré odporúčam dodržiavať. Podľa miery dodržiavania sa určuje "krása" (a čitateľnost) kódu.
# 
# * odsadzovanie for cyklov a funkcií o štyri medzery
# * za čiarkou nasleduje medzera
# * medzi "=" je medzera, (napr. `a = 2`), ale nie vo funkcii (napr. `def func(a, b=5)`)
# * názvy funkcií malými písmenami, slová oddeľujeme podtržníkom (napr. `calc_evals(A)`), názvy objektov veľkými písmenami (pre expertov)

# In[149]:

import this


# ---
# ## [Problem]
# 
# Vygenerujte (100x100) maticu náhodných čísel, získajte jej vlastné čísla a spravte z nich histogram.
# 

# In[157]:

N = 100
A = np.random.rand(N, N)
vals, vecs = eig(A)
vals = np.real(vals)
#print(vals)
plt.hist(np.real(vals))
plt.show()


# ---
# ## [Problem]
# 
# Aké sú vlastné čísla matice
# $$ A = x x^T $$
# ?

# In[172]:

N = 10
x = np.matrix(np.random.rand(N)).T
A = np.dot(x, x.T)
vals, vecs = eig(A)
np.real(vals)


# In[166]:

np.dot(x.T, x)


# In[ ]:



