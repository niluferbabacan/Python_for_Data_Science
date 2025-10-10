###############################################
# COMPREHENSIONS
###############################################

#######################
# List Comprehension
#######################
def new_salary(x):
    return x * 20 / 100 + x

for salary in salaries:
    print(new_salary(salary))

null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))

null_list = []

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))

[new_salary(salary*2) if salary < 3000 else new_salary(salary *0.2) for salary in salaries]

[salary * 2 for salary in salaries]
[salary * 2 for salary in salaries if salary < 3000]
[salary *2 if salary < 3000 else salary * 0 for salary in salaries]

[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries]


students = ["Sumire", "Neva", "Kerem", "Enes"]
students_no = ["Sumire", "Kerem"]

[student.lower() if student in students_no else student.upper() for student in students]
[student.upper() if student not in students_no else student.lower() for student in students]

#######################
# Dict Comprehension
#######################

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}

dictionary.keys()
dictionary.values()
dictionary.items()

{k: v ** 2 for (k,v) in dictionary.items()}

{k.upper(): v for (k,v) in dictionary.items()}

{k.upper(): v ** 3 for (k,v) in dictionary.items()}

# key ve value değerlerine özel bir şekilde müdahale edip bunlar üzerinde değişiklikler yaptık.

#######################
# Uygulama - Mülakat Sorusu
#######################

# Amaç: çift sayıların karesi alınarak bir sözlüğe eklenmek istemektedir
# Key'ler orjinal değerler value'lar ise değiştirilmiş değerler olacak.

# klasik döngü ile

numbers = range(12)
new_dict = {}

for n in numbers:
    if n %2 ==0:
        new_dict[n] = n ** 2


# list comprehensions ile

numbers = range(4,36)
{n: n ** 2 for n in numbers if n %2 ==0}

# pekişmesi açısından bir örnek daha

numbers = range(0, 24)
new_dict = {}
for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n**2 # bu kullanım önemli

# daha basit yolu:

numbers = range(30)
{n:n**2 for n in numbers if n%2 ==0}


#######################
# List & Dict Comprehension Uygulamalar
#######################

#######################
# Uygulama_1
# Bir Veri Setindeki Değişken İsimlerini Değiştirmek
#######################

# before:
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

import  seaborn as sns # kütüphane import edildi
df = sns.load_dataset("car_crashes") # dataset getirildi
df.columns  # değişken isimleri geldi.

# Klasik döngü ile

for col in df.columns:
    print(col)

for col in df.columns:
    print(col.upper())

# kalıcı hale getirmek için liste içinde saklayalım

A = []

for col in df.columns:
    A.append(col.upper())

df.columns = A   # atama işlemiyle değişiklik kalıcı hale geldi.

# List Comprehensions ile

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

df.columns = [col.upper() for col in df.columns]

#######################
# Uygulama_2
# İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.
#######################

# before:
# ['TOTAL',
# 'SPEEDING',
# 'ALCOHOL',
# 'NOT_DISTRACTED',
# 'NO_PREVIOUS',
# 'INS_PREMIUM',
# 'INS_LOSSES',
# 'ABBREV']

# after:
# ['NO_FLAG_TOTAL',
#  'NO_FLAG_SPEEDING',
#  'NO_FLAG_ALCOHOL',
#  'NO_FLAG_NOT_DISTRACTED',
#  'NO_FLAG_NO_PREVIOUS',
#  'FLAG_INS_PREMIUM',
#  'FLAG_INS_LOSSES',
#  'NO_FLAG_ABBREV']



[col for col in df.columns if "INS" in col]


["FLAG_" + col for col in df.columns if "INS" in col]

["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

# Kalıcı hale getirmek için atama işlemi;

df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

#######################
# Uygulama_3
# Amaç key'i string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak.
# Sadece sayısal değişkenler için yapmak istiyoruz.
#######################

# Output:
# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'],
#  'ins_losses': ['mean', 'min', 'max', 'var']}

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "O"]
soz = {}
agg_list = ["mean", "min", "max", "sum"]

for col in num_cols:
    soz[col] = agg_list


# kısa yol
num_cols = [col for col in df.columns if df[col] != "O"]

new_dict = {col: agg_list for col in num_cols}

df[num_cols].head()

df[num_cols].agg(new_dict)




#### Kodun Açıklaması
# sayısal değişkenleri seçmek için;
# veri setinin içinde object olmayan tipteki verileri seçecek df[col].dtype !="O"

num_cols = [col for col in df.columns if df[col].dtype != "O"]  # nümerik tipteki değişkenler geldi.

cat_col = [col for col in df.columns if df[col].dtype == "O"]  # kategorik olanları getirdi.

num_cols = [col for col in df.columns if df[col].dtype != "O"]

dict = {}
agg_list = ["mean", "min", "max", "sum"]  # bizden istenen sözlük formunun value tarafı

# birçok senaryoda kullanılabilecek bir yöntem şimdi bahsedeceğim
# öyle bir şey yapmalıyız ki bir sözlük oluşturup
# key değerine değişken ismimlerini
# value değerlerine ise agg_list basmalıyız

for col in num_cols: # num_cols larda gezdim nümerik kolonlarda
    dict[col] = agg_list

# yakaladığın sütunları key olarak ekledim
# bunlar değişken (col) num_cols dan geliyor
# sol taraf dinamik değişken bir şekilde  num_cols dan geliyor olsa da
# sağ tarafı bir şeyle doldurmak istiyorum.
# value bölümüne sabit bir liste giriyorum Orjinal kısmı burasıydı.

# kısa yol Açıklaması

new_dict = {col: agg_list for col in num_cols} # key deki col num_cols dan geldi

df[num_cols].head() # dataframe içerinde [ ] yardımıyla seçme işlemi yapıldı head ile gözlemledik.

df[num_cols].agg(new_dict) # agg aggregation fonksiyonun kısaltması

# Aggregation fonksiyonu ihtiyaçlarımızı anlayabilecek akıllı bir fonksiyon.
# eğer içerisine böyle bir sözlük girersek ve bu şekilde dataframe e uygularsanız
#gönderdiğiniz sözlüğün içerisindeki değişkenleri key bölümünde tutar
# value bölümüne girdiğiniz tüm fonksiyonları gidip bu değişkenlere(key) otomatik olarak uygular.
# Belirli bir dataframe deki belirli değişkenlere  isteyebileğiniz  bir fonksiyon setini de çok kolay bir hamlede
# (aynı şekilde dict yerine fonk girerek)
# list comprehension yapısı sayesinde biçimlendirmeler gerçekleştiririz.

