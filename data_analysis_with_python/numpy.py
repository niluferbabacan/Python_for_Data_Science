###############################################
# PYTHON İLE VERİ ANALİZİ (DATA ANALYSIS WITH PYTHON)
###############################################
# - NumPy
# - Pandas
# - Veri Görselleştirme: Matplotlib & Seaborn
# - Gelişmiş Fonksiyonel Keşifçi Veri Analizi (Advanced Functional Exploratory Data Analysis)

# Bu klasör içerisinde işlenecek tüm konulardır.
# Ancak bu dosyada sadece Numpy dan bahsedilecek.

#############################################
# NUMPY
#############################################

# Neden NumPy? (Why Numpy?)
# NumPy Array'i Oluşturmak (Creating Numpy Arrays)
# NumPy Array Özellikleri (Attibutes of Numpy Arrays)
# Yeniden Şekillendirme (Reshaping)
# Index Seçimi (Index Selection)
# Slicing
# Fancy Index
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
# Matematiksel İşlemler (Mathematical Operations)

#############################################
# Neden NumPy?
#############################################

# Numpy; nümerik hesaplamalı işlemler için geliştirilmiş bir kütüphanedir.
# Sabit tipte (fix type) veri tutar. Verimli veri saklar.
# Listelere kıyasla çok daha hızlı şekilde işlem yapma imkanı sağlar.
# Yüksek seviyeden işlemler yapma imkanı
# daha az çabayla daha fazla işlem vektör seviyesinden işlem


import numpy as np  # numpy library import ettim

# iki listeyi çarpmak istediğimizde klasik python yolu ile:

a = [1,2,3,4]
b = [2,3,4,5]

ab = []
for i in range(0,len(a)):
    ab.append(a[i] * b[i])


# Numpy ile:
import numpy as np
a = np.array([1,2,3,4]) # 2 listeyi de numpy array'ine çevirdi.
b = np.array([2,3,4,5])

a * b

#############################################
# NumPy Array'i Oluşturmak (Creating Numpy Arrays)
#############################################
# Numpy array diğer bir ifadesiyle nd.array nesneleri
# pythonda kullanılan diğer bazı veri yapıları gibi bir veri yapısıdır.

import numpy as np

np.array([1,2,3,4])
type(np.array([1,2,3,4])) # numpy.ndarrray

# Normalde sıfırdan array oluşturulmaz ama örnek olması için;

np.zeros(10, dtype=int) # girdiğin sayı adedince sıfır oluşturur.

np.random.randint(0,15,size=4)

np.random.normal(10,4, (3,4))
# belirli bir istatiksel değere göre sayı üretmek için normal kullan
# normal fonk der ki; ortalaması, standart sapması ve boyut bilgisi gir

#############################################
# NumPy Array Özellikleri (Attibutes of Numpy Arrays)
#############################################
import numpy as np

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size=8)

a.shape
a.ndim
a.size
a.dtype

#############################################
# Yeniden Şekillendirme (Reshaping)
#############################################
# elimizdeki array in boyutunu değiştirmek için kullanılır.

import numpy as np

np.random.randint(1,12, size=9)   # tek boyutlu bir array'dir. 2 boyutluya çevirelim

np.random.randint(1,12, size=9).reshape(3,3) # 3x3 matrise çevrildi. burada (size) boyut bilgisi dikkate alınır.

np.random.randint(1,12, size=7).reshape(3,3) #hata alırsın


# atama ile de boyut değiştirme işlemi yapabiriz
ar= np.random.randint(2,48,size=15)
ar.reshape(3,5) # 3 satır 5 sütun matrise dönüştü.

#############################################
# Index Seçimi (Index Selection)
#############################################
import numpy as np
a = np.random.randint(10,size=10)

a[0]
a[:6]

a[1] = 999


# 2 boyutlu array içinde:

m = np.random.randint(10, size=(3,6))

m[0,0] # hem satır hem sütun bilgisini vermeniz gerekmektedir.

m[1,1]

m[1,3] = 888

m[0,2] = 4.9 # 4 olarak dahil eder çünkü fix type özelliği sabit veri saklar

m[:,3]
m[1,:]
m[:2, 1:5]  # hem satır hem sutün için aralık girerek sciling işlemi

#############################################
# Fancy Index
#############################################

# fancy index; bir numpy array'ine bir liste girdiğinizde
# (ki bu liste index numarası ya da true/false ifadeleri de tutuyor olabilir.
# bize kolay bir şekilde seçim işlemi sağlar.


import numpy as np

v = np.arange(0,30,3) # başlangıç, bitiş, artış miktarı
#arange belirli bir adım boyunca array oluşturmak için kullanılır.

v = np.arange(0,30,3)
v[1]
v[4]

catch =[1,2,3]
v[catch]
# v numpy array'indeki bu indexlere karşılık gelen değerleri
# bu array içerisinden getirmiş olacak


#############################################
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
#############################################
import numpy as np
v = np.array([1, 2, 3, 4, 5])

#######################
# Klasik döngü ile
#######################

ab = []

for i in v:
    print(i)

for i in v:
    if i < 3:
        ab.append(i)

#######################
# Numpy ile
#######################

v[v < 3] # köşeli parantez içerisine koşulu yazdık

v[v > 3]
v[v != 3]
v[v == 3]
v[v >=3 ]

# mantıklsal operatörler burada kullanılabilir.

#############################################
# Matematiksel İşlemler (Mathematical Operations)
#############################################
import numpy as np

v = np.array([1,2,3,4,5])

v / 5
v * 5 / 10
v ** 2
v - 1

# bu işlemleri metodlar aracılığı ile de gerçekleştirebiliriz.

np.subtract(v,1)
np.add(v,4)
np.mean(v)
np.sum(v)
np.min(v)
np.max(v)
np.var(v)

# bu yapılan işlemlerin kalıcı olması isteniyorsa atama yap

v = np.subtract(v, 2)

#######################
# NumPy ile İki Bilinmeyenli Denklem Çözümü
#######################

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

x = np.array([[5, 1],[1, 3]]) # denklemin katsayıları bir array'de
y = np.array([12,10]) # sonuçlar bir array'de

np.linalg.solve(x,y) # numpy array içerisinde yer alan solve metodu ile işlem sonucu geldi