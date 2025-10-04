###############################################
# FONKSİYONLAR, KOŞULLAR, DÖNGÜLER, COMPREHENSIONS
###############################################
# - Fonksiyonlar (Functions)
# - Koşullar (Conditions)
# - Döngüler (Loops)
# - Comprehesions

# Bahsedilecek tüm konu başlıklarıdır.
# Ancak bu dökümanda yalnızca fonksiyonlardan bahsedilecek.

###############################################
# FONKSİYONLAR (FUNCTIONS)
###############################################

#######################
# Fonksiyon Okuryazarlığı
#######################

print("a", "b")
print("a", "b", sep="**")

help(print)  # fonfsiyonun docstring ekranına ulaşılır.


#######################
# Fonksiyon Tanımlama
#######################

def calculate(x):
    print(x * 4)


calculate(6)


# İki argümanlı/parametreli bir fonksiyon tanımlayalım.

def summer(arg1, arg2):
    print(arg1 + arg2)


summer(3, 7)

summer(7, 3)

summer(arg2=7, arg1=3)


#######################
# Docstring
#######################

def summer(arg1, arg2):
    """
    Sum of two numbers

    Args:
        arg1: int, float
        arg2: int, float

    Returns:
        int, float

    Examples:

    Notes:

    """
    print(arg1 + arg2)


help(summer)

summer(4, 5)


#######################
# Fonksiyonların Statement/Body Bölümü
#######################

# def function_name(parameters/arguments):
#     statements (function body)

def say_hi():
    print("Merhaba")
    print("Hi")
    print("Hello")


say_hi()


def say_hi(string):
    print(string)
    print("Hello")
    print("Hi")


say_hi("Miuul")


def multiplication(x, y):
    z = x * y
    print(z)


multiplication(6, 7)

# girilen değerleri bir liste içinde saklayacak fonksiyon.

list_store = []


def add_element(x, y):
    z = x * y
    list_store.append(z)
    print(list_store)


add_element(4, 8)
add_element(5, 6)
add_element(18, 10)


#######################
# Ön Tanımlı Argümanlar/Parametreler (Default Parameters/Arguments)
#######################

def divide(a, b):
    print(a / b)


divide(1, 2)


def divide(a, b=1):
    print(a / b)


divide(12)


def say_hi(string="Merhaba"):
    print(string)
    print("Hi")
    print("Hello")


say_hi()
say_hi("Selam")

#######################
# Ne Zaman Fonksiyon Yazma İhtiyacımız Olur?
#######################

# varm, moisture, charge

(56 + 15) / 80
(17 + 45) / 70
(52 + 45) / 80


# DRY: don't repeat yourself
# birbirini tekrar eden görevler söz konusu olduğunda
# fonksiyon yazma ihtiyacı kendini hissettirir.

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


calculate(98, 12, 78)


#######################
# Return: Fonksiyon Çıktılarını Girdi Olarak Kullanmak
######################

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


# calculate(98, 12, 78) * 10

def calculate(varm, moisture, charge):
    return (varm + moisture) / charge


calculate(98, 12, 78) * 10

a = calculate(98, 12, 78) * 10


def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge
    return varm, moisture, charge, output


calculate(98, 12, 78)

type(calculate(98, 12, 78))

varma, moisturea, chargea, outputa = calculate(98, 12, 78)


#######################
# Fonksiyon İçerisinden Fonksiyon Çağırmak
######################

def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)


calculate(90, 12, 12) * 10


def standardization(a, p):
    return a * 10 / 100 + p * p


standardization(45, 1)


def all_calculation(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)


all_calculation(1, 4, 8, 21)


def all_calculation(varm, moisture, charge, a, p):
    print(calculate(varm, moisture, charge))
    b = standardization(a, p)
    print(b * 10)


all_calculation(1, 3, 5, 19, 12)

#######################
# Lokal & Global Değişkenler (Local & Global Variables)
#######################

list_store = [1, 2]


def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)


add_element(12, 4)
add_element(2, 7)
add_element(6, 3)





