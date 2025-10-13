#############################################
# PANDAS
#############################################

# Veri manipülasyonu ya da veri analizi dendiğinde akla ilk gelen library'dir.


# Pandas Series
# Veri Okuma (Reading Data)
# Veriye Hızlı Bakış (Quick Look at Data)
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
# Apply ve Lambda
# Birleştirme (Join) İşlemleri

#  Dosya içinde bu konu başlıklarına değinilecek.

#############################################
# Pandas Series
#############################################
# pandas series; tek boyutlu index bilgisi barındıran bir veri tipidir.
# pandas dataframe ise çok boyutlu ve index bilgisi barındıran veri tipidir.

import pandas as pd
s =pd.Series([10,25,54,6,8])
type(s)

s.index
s.dtype
s.size
s.ndim  # pandas Serileri tek boyutludur.
s.values  # içindeki değerlere erişmek için

type(s.values) # nd.array geldi.

s.head()  # ilk 5 değeri getirir.
s.head(3)
s.tail()  # son 5 değeri getirir.
s.tail(3)

# Asıl üzerinde çalışacak olduğumuz yapı pandas dataframe'dir.

#############################################
# Veri Okuma (Reading Data)
#############################################

import pandas as pd

df= pd.read_csv("data_analysis_with_python/datasets/adversiting.csv")
df.head()

# pandas cheatsheet
# internette bulunan bir kaynaktır. kullanılabilecek diğer
# dosya formatları ile ilgili tüm bilgiler
# derli toplu bir şekilde elinin altında tutulur.


#############################################
# Veriye Hızlı Bakış (Quick Look at Data)
#############################################

# elimize bir dataframe geldiğinde buna hızlı bir şekilde
# hangi metodları uygulayabileceğimizi değerlendireceğiz.

import pandas as pd
import seaborn as sns


df = sns.load_dataset("titanic") # seaborn library'de yer alan bir veri setini çalışmamıza dahil ettik.

df.head()  # veriye hızlı bir göz atmayı sağlar
df.tail()
df.shape
df.info()  # veri setinin genel özet bilgilerini görüntüler
df.columns  # dataframe'in değişkenlerinin isimlerine erişmek için
df.index
df.describe()  # elimizdeki bir dataframe'in eğer hızlı bir şekilde özet istatistiklerine erişmek istersek.
df.describe().T # Çıktının daha okunabilir formatta gelmesi için

df.isnull().values.any() # veri setinde en az bir tane dahi olsa bir eksik değer var mı? sorusu içindir
df.isnull().sum() # herbir değişkende kaç tane eksik değer olduğu bilgisi hesaplanmış oldu

#bir dataframe'den değişken seçmek istediğinde df["sex"]

df["sex"].head()
df["sex"].value_counts()  # bu sex değişkeninde kaç tane sınıf olduğu ve herbir sınıfın kaçar tane olduğu bilgisi geldi

#########################################
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
#############################################

import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()

df.index
df[0:13]
df.drop(0, axis=0).head() # drop belirli indexe göre silme işlemi için kullanılır. axis = 0 satırda sil. axis = 1 sütunda sil.

delete_indexes =[1,3,5,7]
df.drop(delete_indexes, axis=0).head()  # gözlemlemek adına head atarım

# df.drop(delete_indexes, axis=0) işlemi kalıcı hale getirmek için:
df = df.drop(delete_indexes, axis=0) #1.yol
df.drop(delete_indexes, axis = 0, inplace=True) # inplace argümanı ile değişiklik kalıcı hale geldi atama işlemine gerek duymadan


#######################
# Değişkeni Indexe Çevirmek
#######################

df["age"].head()
df.age.head()  # buda bir değişken seçme yöntemi

df.index

# age değişkenini indexe atmak istersek:
df.index = df["age"]

df.drop("age", axis=1).head()  # sütundan age değişkeni uçtu

df.drop("age", axis=1, inplace=True)
df.head()

#######################
# Indexi Değişkene Çevirmek
#######################
# 1.yol:
df.index
df["age"] = df.index

df.head()

# 2.yol

df.drop("age", axis=1, inplace=True)  #önce bir silelim eski haline gelsin

df.reset_index().head()
df = df.reset_index()
df.head()

#######################
# Değişkenler Üzerinde İşlemler
#######################
import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None) # çıktıdaki 3 nokta gözükmesin tüm sütunları göster ayar yaptık
df = sns.load_dataset("titanic")
df.head()

"age" in df      # değişkenin datasette olup olmadığı sorgusu

df["age"].head()
df.age.head()

df["age"].head()
type(df["age"].head())  # pandas.Series

# Seçim sonucunda veri tipinin dataframe olarak kalmasını istiyorsan çift köşeli parantez kullan

df[["age"]].head()
type(df[["age"]].head())  # pandas.Dataframe  veri yapısı bozulmadı. dataframe olmaya devam etti.

# Bir dataframe'in içeriisnden birden fazla değişken seçmek istersek.
df[["age", "alive"]]   # seçmek istediğin değişkenleri liste içinde yaz.

col_names = ["age", "embarked", "alive"]
df[col_names]

# dataframe'e yeni bir değişken eklemek istendiğinde:

df["age2"] = df["age"] * 3

df["age3"] = df["age"] / df["age2"]

# silmek istendiğinde;
df.drop("age3", axis =1).head()

# birden fala değişken silmek istendiğinde;

df.drop(["age2", "age3"], axis=1)
df.head()

df.drop(col_names, axis=1).head()

# dataframe'de belirli bir string ifade barındıranlara belirli bir işlem yapılmak istendiğinde:

df.loc[:, df.columns.str.contains("age")].head()  # contains ile içinde age bulunanlar geldi.

# bunları silmek istedğimde değildir demenin yolu ~ dır  bunun dışındakileri seç demektir.

df.loc[:, ~df.columns.str.contains("age")].head()

#######################
# iloc & loc
#######################

import pandas as pd
import seaborn as sns
df.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

# iloc: integer based selection index bilgisine göre seçim yapar.

df.iloc[:3]
df.iloc[0,0]

df.iloc[:3, "age"]  # hata aldık age str olduğundan index bekliyor benden

# loc: label based selection

df.loc[0:3]
df.loc[:3, "age"]


col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]

#######################
# Koşullu Seçim (Conditional Selection)
#######################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df[df["age"] > 50].head()
df[df["age"] > 50].count()
df[df["age"] > 50]["age"].count() # sonuna ilgilendiğin değişkeni yazarsan onu getirir.

# yaşı 50 den büyük olanların class bilgisine erişmek için:

df.loc[df["age"] > 50, "class"].head()

# Bir koşul + 2 sütun seçelim;

df.loc[df["age"] > 50, ["class", "age"]].head()

# birden fazla koşul girildiği durumda  koşul ifadeleri paranteze alınmalıdır.

df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head()

df.loc[(df["age"] > 50) & (df["sex"] == "male") & (df["embark_town"] == "Cherbourg"),
["class", "age","embark_town"]].head()

df.loc[(df["age"] > 50)
       & (df["sex"] == "male")
       & (df["embark_town"] == "Cherbourg"),
       ["class", "age","embark_town"]].head()

df["embark_town"].value_counts()  # her bir class kişi sayısı geldi.

df.loc[(df["age"] > 50)
       & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
 ["class","age", "embark_town"]].head()

# count bilgisini gözlemlemek için değişikliği kalıcı hale getirmeli;

df_new = df.loc[(df["age"] > 50)
       & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
 ["class","age", "embark_town"]]

df["embark_town"].value_counts()

############################################
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
#############################################

# Toplulaştırma bir veri yapısı içinde barınan değerleri toplu bir şekilde temsil etmek demektir.
# özet istatistikler bunun için güzel bir örnektir.
# Aşağıdakiler toplulaştırma fonksiyonlarıdır. Tek başına da kullanılır.
# Fakat gruplama kavramı ile  beraber düşünüldüğünde toplulaştırma ve gruplama hep bir arada olur.

# - count()
# - first()
# - last()
# - mean()
# - median()
# - min()
# - max()
# - std()
# - var()
# - sum()


import pandas as pd
import seaborn as sns
pd.set_option("display.max_colums", None)
df = sns.load_dataset("titanic")
df.head()

# yaşın ortalaması:

df["age"].mean()

# cinsiyete göre yaşın ortalamasını öğrenmek istendiğinde:

df.groupby("sex")["age"].mean()

# birden fazla toplulaştırma işlemi yapılcağı durumda aggregation fonk kullanılır.
# agg kısaltılmışı içine dict yapısı yer alıyor.

df.groupby("sex").agg({"age": "mean"})

df.groupby("sex").agg({"age": ["mean", "sum"]})  # cinsiyet kırılımında yaşım mean + sum geldi.

df.groupby("sex").agg({"age": ["mean", "sum"],
                       "survived": "mean"})

# birden fazla kategorik değişkene göre kırılım yapmayı istendiğinde:

df.groupby(["sex", "embark_town"]).agg({"age": "mean",
                                       "survived": "mean"})

# cinsiyete göre veri seti kırıldı ardından embark_towna göre tekrar kırıldı 2 seviyeden groupby yapıldı

# 3 kırılım yapalım:

df.groupby(["sex", "embark_town", "class"]).agg({"age": "mean",
                                                "survived": "mean"})

# birde bunun frekans bilgisine erişmek istediğimizde ;


df.groupby(["sex", "embark_town", "class"]).agg({"age": "mean",
                                                "survived": "mean",
                                                 "sex": "count" })

#######################
# Pivot table
# Groupby işlemlerine benzer şekilde veri setini kırılımlar açısından
# değerlendirmek ve ilgilendiğimiz özet istatistiği bu kırılımlar açısından görme imkanı sağlar.
#######################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# pivot table: kesişimlerde neyi görmek istiyorsan(values), satırda hangi değişken görmek istiyorsan (index), sütunda hangi değişken görmek istiyorsan (columns)

df.pivot_table("survived","sex","embarked")  # pivot_table ön tanımlı değeri mean dir.
# biçimlendirmek için;
df.pivot_table("survived", "sex","embarked", aggfunc = "std")

df.pivot_table("survived","sex",["embarked", "class"])

# Yaş değişkeni hayatta kalma açısından nasıl değerlendirilebilir?

# Bunu yapmanın yolu yaş değişkenini kategorik değişkene çevirmektir.
# cut ve qcut funk ile mümkün.

# cut func der ki ; neyi böleceğimi ver. hangi aralıktan böleceğimi ver aralığı list formunda gir

df["new_age"] = pd.cut(df["age"], [0,10,18,25,40,90])
df.head()
df.pivot_table("survived", "sex", "new_age")

df.pivot_table("survived","sex",["new_age", "class"])

# kod yan yana gelsin çıktının okunabilirliği olsun:
pd.set_option("display.width",500)
"""
dikkat : cut ve qcut fonksiyonları elinizdeki sayısal değişkenleri kategorik değişkenlere çevirmek için en yaygın kullanılan iki ayrı fonksiyondur.
Eğer sayısal değişkeni hangi kategorilere bölmek istediğinizi biliyorsanız cut func.
Eğer elinizdeki sayısal değişkeni tanımıyorsanız dolayısıyla çeyreklik değerlerine bölsün istiyorsan qcut func.
qcut ; otomatik olarak değerleri küçükten büyüğe sıralar. yüzdelik, çeyreklik değerlerine göre bunları gruplara böler çok yaygın kullanılır.

"""


""" 
Temel sözdizimi;

pd.qcut(x, q, labels=False)
 
Parametreler:

x: Bölünecek veri (örneğin bir pandas Series)

q: Kaç dilime bölüneceği (ör. 4 = dört çeyrek)

labels: Etiket kullanılsın mı (varsayılan True).
labels=False dersen, sadece aralık numarası döner. """

# Örnek 1 – Basit kullanım
import pandas as pd

ages = pd.Series([10, 22, 25, 30, 40, 45, 50, 60, 70, 80])

# 4 eşit frekanslı gruba böl
groups = pd.qcut(ages, 4, labels=False)
print(groups)

# Örnek 2 – Etiketli gruplar

labels = ['young', 'mid-age', 'senior', 'elder']
age_groups = pd.qcut(ages, 4, labels=labels)
print(age_groups)

# Örnek 3 – DataFrame içinde kullanım
import pandas as pd

df = pd.DataFrame({
    'income': [2500, 3200, 4000, 5000, 6000, 7500, 9000, 12000]
})

df['income_group'] = pd.qcut(df['income'], 3, labels=['low', 'medium', 'high'])
print(df)

# Örnek4 titanic veri setinde

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df["new_fare"] = pd.qcut(df["fare"], 4, labels=False)
df.head()

#############################################
# Apply ve Lambda
# apply satır veya sütunlarda otomatik olarak fonksiyon çalıştırma imkanı sağlar.
# yani bir dataframe'in satır ya da sütunda apply ile istediğimiz func. uygulayabiliriz.
# lambda bir func tanımlama şeklidir.  kullan-at funct.
#############################################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["age2"] = df["age"] * 2
df["age3"] = df["age"] * 5
df.head()

(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()

# klasik yol:

for col in df.columns:
    if "age" in col:
        print(col)

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())

for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10
df.head()
# apply ve lambda ile:

df[["age", "age2", "age3"]].apply(lambda x: x/10).head()

# yaş değişkenini daha programatik seçelim:

df.loc[:,df.columns.str.contains("age")].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()

# lambda yerine dışarıda tanımlanan bir func da kullanılabilir.

def standart_scaler(col_name):
    return(col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

# kalıcı hale getirmek için:

df.loc[:, ["age","age2", "age3"]]= df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)
df.head()

#############################################
# Birleştirme (Join) İşlemleri
#############################################
import numpy as np
import pandas as pd
m = np.random.randint(1,30, size=(5,3)) #numpy array oluşturduk.
df1 = pd.DataFrame(m, columns=["var1","var2","var3"]) # sıfırdan dataframe oluşturduk
df2 = df1 + 88

pd.concat([df1,df2]) # index bilgisini olduğu gibi tuttu.


pd.concat([df1,df2], ignore_index = True) # index problemi çözüldü.

# concat'a argüman vererek sütun bazında da birleştirme yapılabilir. concat + ctrl tıkla tüm yöntemleri gör.

#######################
# Merge ile Birleştirme İşlemleri
#######################
df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

pd.merge(df1, df2)
pd.merge(df1, df2, on = "employees")

# Amaç: Her çalışanın müdürünün bilgisine erişmek istiyoruz.

df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})


pd.merge(df3,df4)
