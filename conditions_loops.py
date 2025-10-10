###############################################
# KOŞULLAR (CONDITIONS) & DÖNGÜLER (LOOPS)
###############################################

# Koşullar bir program yazımı esnasında akış kontrolü sağlayan ve
# programların belirli kurallara göre ya da koşullara göre nasıl hareket etmesi gerektiğini
# biz kullanıcılar tarafından programlara bildirme imkanı sağlayan yapılardır.
# Eğer bu koşul sağlanıyorsa bunu yoksa şunu yap diyen akışlar tasarlamamızı sağlar.

# True-False'u hatırlayalım.
1 == 1
1 == 2

# if
if 1 == 1:
    print("something")

if 1 == 2:
    print("something")

number = 15

if number == 10: # false çıkarsa alttaki işlem çalışmaz.
    print("number is 10") # Yapılması istenen işlem yazılır.

number = 10
number = 22


def number_check(number):
    if number == 10:
        print("number is 10")


number_check(16)
number_check(85)
number_check(10)


#######################
# else
#######################
def number_check(number):
    if number == 10:
        print("number is 10")


number_check(32)


def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")


number_check(32)
number_check(10)


#######################
# elif
#######################

def number_check(number):
    if number > 10:
        print("greater than 10")
    elif number < 10:
        print("less than 10")
    else:
        print("equal to 10")


number_check(54)
number_check(6)
number_check(10)

###############################################
# DÖNGÜLER (LOOPS)
###############################################
# for loop

students = ["Neva", "Sumire", "Kerem", "Begüm"]

students[0]
students[1]
students[2]

for student in students:
    print(student)

for student in students:
    print(student.upper())

for student in students:
    print(student.lower())

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)

for salary in salaries:
    print(int(salary * 20 / 100 + salary))

for salary in salaries:
    print(int(salary * 30 / 100 + salary))

for salary in salaries:
    print(int(salary * 50 / 100 + salary))


# sürekli değişen zam değerleri için bir fonk yazalım

def new_salary(salary, rate):
    return int(salary * rate / 100 + salary)


new_salary(1000, 20)
new_salary(2000, 30)

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(new_salary(salary, 25))

for salary in salaries:
    print(new_salary(salary, 50))

salaries2 = [10700, 25000, 30400, 40300, 50200]

for salary in salaries2:
    print(new_salary(salary, 20))

for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 10))
    else:
        print(new_salary(salary, 20))

#######################
# Uygulama - Mülakat Sorusu
#######################

# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

len("Severa")
range(0, 6)
range(len("Sevara"))

for i in range(0, 6):
    print(i)

for i in range(len("Severa")):
    print(i)

m = "yasemin"
m[2]


def alternating(string):
    new_string = ""
    for string_index in range(len(string)):
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()
    print(new_string)


alternating("yasemin")


def alternating(string):
    new_string = ""
    # girilen string'in index'lerinde gez.
    for string_index in range(len(string)):
        # index çift ise büyük harfe çevir.
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        # index tek ise küçük harfe çevir.
        else:
            new_string += string[string_index].lower()
    print(new_string)


alternating("Sevara")
alternating("hi my name is john and i am learning python")

#######################
# break & continue & while
#######################

salaries = [1000, 2000, 3000, 4000, 5000]

# break: şart saglandiğinde kod calısmayi durdur.

for salary in salaries:
    if salary == 3000:
        break
    print(salary)

# continue sarti pas gec demektir.

for salary in salaries:
    if salary == 3000:
        continue
    print(salary)

# while

number = 1
while number < 5:
    print(number)
    number += 1

#######################
# Enumerate: Otomatik Counter/Indexer ile for loop
#######################

students = ["Severa", "Neva", "Kerem", "Sumire", "Mirza"]

for student in students:
    print(student)

for index, student in enumerate(students):
    print(index, student)

for index, student in enumerate(students, 1): # index in 1 ile başlamasını istersek
    print(index, student)

A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)

print(A, B)

######################
# Uygulama - Mülakat Sorusu
########################
# divide_students fonksiyonu yazınız.
# Çift indexte yer alan öğrencileri bir listeye alınız.
# Tek indexte yer alan öğrencileri başka bir listeye alınız.
# Fakat bu iki liste tek bir liste olarak return olsun.

students = ["John", "Mark", "Venessa", "Mariam"]

def divide_students(student):
    groups = [[], []]
    for index, student in enumerate(students):
        if index %2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups


divide_students(students)
st = divide_students(students)
st[0]
st[1]

#######################
# Uygulama - Mülakat Sorusu
#######################

# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

#######################
# alternating fonksiyonunun enumerate ile yazılması
#######################

def alternating(string):
    new_string = ""
    for index, letter in enumerate(string):
        if index %2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

alternating("Yasemin Nilüfer BABACAN")
alternating("hi my name is john and i am learning python")

#######################
# Zip : aynı indeksli elemanları eşleştirip tuple’lar halinde bir araya getirir.
#######################

# zip() fonksiyonu, Python’da birden fazla diziyi (list, tuple vb.)
# eleman bazında birleştirmek için kullanılır.

students = ["John", "Mark", "Venessa", "Mariam"]

departments = ["mathematics", "statistics", "physics", "astronomy"]

ages = [23, 30, 26, 22]

list(zip(students, departments, ages))

###############################################
# lambda, map, filter, reduce
###############################################
def summer(a, b):
    return a + b

summer(8,6) * 6

# lambda : atama işlemi olmaksızın fonksiyon tanımlama imkanı sunar.
# kullan-at fonksiyondur.

new_sum = lambda a,b: a + b
new_sum(8,3)

# map : seni döngü yazmaktan kurtarmak istiyorum der.
# Bana içerisinde gezebileceğim iterarif bir nesne ver.
# ve bu nesneye uygulamak istediğin fonksiyonu gir.
# Ben sana bu işlemi otomatik olarak yapayım der.

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x
new_salary(1000)

for salary in salaries:
    print(new_salary(salary))

list(map(new_salary, salaries))

#del new_sum

list(map(lambda x: x * 20 / 100 + x, salaries))
list(map(lambda x: x ** 2, salaries))

#FILTER : ilgili koşulu filtreler getirir.

list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 ==0, list_store))

#Reduce : listedeki elemanları soldan sağa doğru, verilen bir fonksiyona göre birleştirir.

from functools import reduce
list_store = [1, 2, 3, 4]
reduce(lambda a,b: a +b, list_store)

