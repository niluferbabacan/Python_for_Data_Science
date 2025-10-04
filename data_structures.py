###############################################
# VERİ YAPILARI (DATA STRUCTURES)
###############################################
# - Veri Yapılarına Giriş ve Hızlı Özet
# - Sayılar (Numbers): int, float, complex
# - Karakter Dizileri (Strings): str
# - Boolean (TRUE-FALSE): bool
# - Liste (List)
# - Sözlük (Dictionary)
# - Demet (Tuple)
# - Set

###############################################
# Veri Yapılarına Giriş ve Hızlı Özet
##############################################

# Sayılar: integer
x = 24
type(x)

# Sayılar: float
x = 10.3
type(x)

# Sayılar: complex
x = 2j + 1
type(x)

# String
x = "Hello AI Era"
type(x)

# Boolean
True
False
type(True)
8 == 4
7 == 2
1 == 1
type(7 == 2)

# Liste
x = ["btc", "eth", "xrp"]
type(x)

# Sözlük (dictionary)
x = {"name": "Peter", "Age": 36}
type(x)

# Tuple
x = ("python", "ml", "ds")
type(x)

# Set
x = {"python", "ml", "ds"}
type(x)

# Not: Liste, tuple, set ve dictionary veri yapıları
# aynı zamanda Python Collections (Arrays) olarak geçmektedir.


###############################################
# Sayılar (Numbers): int, float, complex
###############################################

a = 5
b = 10.5

a * 3
a / 7
a * b / 10
a ** 2

#######################
# Tipleri değiştirmek
#######################

int(b)
float(a)

int(a * b / 10)

c = a * b / 10

int(c)


###############################################
# Karakter Dizileri (Strings)
###############################################

print("Nilüfer")
print('Nilüfer')

"Nilüfer"

name = "Nilüfer"
name = 'Nilüfer'

# Tek tırnak veya çift tırnak ile ifade edilir. Fark etmez.

#######################
# Çok Satırlı Karakter Dizileri
#######################

"""Veri Yapıları: Hızlı Özet, 
Sayılar (Numbers): int, float, complex, 
Karakter Dizileri (Strings): str, 
List, Dictionary, Tuple, Set, 
Boolean (TRUE-FALSE): bool"""

long_str = """Veri Yapıları: Hızlı Özet, 
Sayılar (Numbers): int, float, complex, 
Karakter Dizileri (Strings): str, 
List, Dictionary, Tuple, Set, 
Boolean (TRUE-FALSE): bool"""

#######################
# Karakter Dizilerinin Elemanlarına Erişmek
#######################

name = "Yasemin Nilüfer"
name
name[0]
name[4]
name[8]

#######################
# Karakter Dizilerinde Slice İşlemi
#######################

name[0:2]
long_str[0:10]

#######################
# String İçerisinde Karakter Sorgulamak
#######################

long_str

"veri" in long_str

"Veri" in long_str

# python case sensetive olduğundan 'v' harfinin küçük yazılması false döndürdü.
# \n bir alt satıra geçildiğini ifade eder.

"bool" in long_str

###############################################
# String (Karakter Dizisi) Metodları
###############################################

dir(str) #string ile kullanabilecek tüm metodlar listelendi.
dir(int)

#######################
# len --> fonksiyonu stringlerde boyut bigisini verir.
#######################

name = "nilüfer"
type(name)
len(name)

# Peki len bir fonksiyon mu metod mu? ctrl+len tıkla açılan sayfada şunlara bak:
# eğer bir fonksiyon class yapısı içerisinde tanımlandıysa buna metod denir.
# eğer bir class yapısı içinde değilse fonksiyondur.
# len python içindeki gömülü fonksiyonlardan biridir.

type(len)

len(name)
len("yasemin_nilüfer")
len("PYTHON")

#######################
# upper() & lower(): küçük-büyük dönüşümleri
#######################

"python".upper()
"PYTHON".lower()

# type(upper)
# type(upper())
# upper bir metoddur. class yapısı içinde tanımlanmıştır.

#######################
# replace: karakter değiştirir
#######################

hi = "Hello AI Era"
hi.replace("l","p")

#######################
# split: böler
#######################

"Hello AI Era".split()

#######################
# strip: kırpar
#######################

" ofofo ".strip()
"ofofo".strip("o")


#######################
# capitalize: ilk harfi büyütür
#######################

"fetih".capitalize()

dir("fetih") # kullanabileceğim tüm metodlar listelendi.

"fetih".startswith("f")

###############################################
# Liste (List)
###############################################

# - Değiştirilebilir
# - Sıralıdır. Index işlemleri yapılabilir.
# - Kapsayıcıdır.

notes = [1, 2, 3, 4]
type(notes)
names = ["a", "b", "v", "d"]
not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]

not_nam[0]
not_nam[5]
not_nam[6]
not_nam[6][1]
type(not_nam[6])
type(not_nam[6][1])

notes[0] = 99
notes
not_nam[0:4]


###############################################
# Liste Metodları (List Methods)
###############################################

dir(notes)
dir(list)

#######################
# len: builtin python fonksiyonu, boyut bilgisi.
#######################

len(notes)
len(not_nam)

#######################
# append: eleman ekler
#######################

notes.append(100)
notes

#######################
# pop: indexe göre siler
#######################

notes.pop(0)
notes

#######################
# insert: indexe ekler
#######################

notes.insert(2, 99)
notes

###############################################
# Sözlük (Dictonary)
###############################################

# Değiştirilebilir.
# Sırasız. (3.7 sonra sıralı.)
# Kapsayıcı.
# key değerleri farklı olacak.

# key-value

dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Reg"}

dictionary["REG"]
dictionary["LOG"]

dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}

dictionary["CART"]
dictionary["CART"][1]

dictionary = {"REG": 10,
              "LOG": 20,
              "CART": 30}

#######################
# Key Sorgulama
#######################

"YSA" in dictionary

#######################
# Key'e Göre Value'ya Erişmek
#######################

dictionary["REG"]
dictionary.get("REG")

#######################
# Value Değiştirmek
#######################

dictionary["REG"] = ["YSA", 10]

#######################
# Tüm Key'lere Erişmek
#######################

dictionary.keys()

#######################
# Tüm Value'lara Erişmek
#######################

dictionary.values()

#######################
# Tüm Çiftleri Tuple Halinde Listeye Çevirme
#######################

dictionary.items()

#######################
# Key-Value Değerini Güncellemek
#######################

dictionary.update({"REG": 11})

#######################
# Yeni Key-Value Eklemek
#######################

dictionary.update({"RF": 10})

###############################################
# Demet (Tuple)
###############################################

# - Değiştirilemez.
# - Sıralıdır.
# - Kapsayıcıdır.

t = ("severa","aysu", 12, 5)
type(t)

t[0]
t[:3]

t[1] = 4  # tuple lar değiştirilemez. diyelim değiştirmek istedik.

t = list(t)
t[1] = 4
t = tuple(t)
t

###############################################
# Set
###############################################

# - Değiştirilebilir.
# - Sırasız + Eşsizdir.
# - Kapsayıcıdır.

#######################
# difference(): İki kümenin farkı
#######################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

# set1'de olup set2'de olmayanlar.
set1.difference(set2)
set1 - set2

# set2'de olup set1'de olmayanlar.
set2.difference(set1)
set2 - set1

#######################
# symmetric_difference(): İki kümede de birbirlerine göre olmayanlar
#######################

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

#######################
# intersection(): İki kümenin kesişimi
#######################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

set1.intersection(set2)
set2.intersection(set1)

set1 & set2


#######################
# union(): İki kümenin birleşimi
#######################

set1.union(set2)
set2.union(set1)


#######################
# isdisjoint(): İki kümenin kesişimi boş mu?
#######################

set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])

set1.isdisjoint(set2)
set2.isdisjoint(set1)


#######################
# issubset(): Bir küme diğer kümenin alt kümesi mi?
#######################

set1.issubset(set2)
set2.issubset(set1)

#######################
# issuperset(): Bir küme diğer kümeyi kapsıyor mu?
#######################

set2.issuperset(set1)
set1.issuperset(set2)
