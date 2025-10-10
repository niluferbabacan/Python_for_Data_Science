# Python Interview Questions with Bonus Solutions
# Topics: Data Structures, Functions, Conditions, Loops, and Comprehensions

# Python Mülakat Soruları ve Ek (Bonus) Çözümler
# Konular: Veri yapıları, fonksiyonlar, koşullar, döngüler, comprehensions

#######################
# Uygulama - Mülakat Sorusu -Interview Question_1
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

########
#Solution Explanation
########
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


### Solution 2:

def alternating(string):
    new_string = ""
    for letter in range(len(string)):
        if letter %2 == 0:
            new_string += string[letter].upper()
        else:
            new_string += string[letter].lower()
    print(new_string)

alternating("hi my name is john and i am learning python")

######################
# Uygulama - Mülakat Sorusu -Interview Question_2
########################
# divide_students fonksiyonu yazınız.
# Çift indexte yer alan öğrencileri bir listeye alınız.
# Tek indexte yer alan öğrencileri başka bir listeye alınız.
# Fakat bu iki liste tek bir liste olarak return olsun.

students = ["John", "Mark", "Venessa", "Mariam"]

# Solution 1:
def divide_students(students):
    A = []
    B = []
    for index, student in enumerate(students):
        if index %2 == 0:
            A.append(student)
        else:
            B.append(student)
    return A, B


divide_students(students)

# Solution 2:
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



# Solution 3:

def divide_students(students):
    groups = [[],[]]
    for index, student in enumerate (students):
        if index %2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)

    print(groups)

divide_students(students)




#######################
# Uygulama - Mülakat Sorusu -Interview Question_3
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
# Uygulama - Mülakat Sorusu --Interview Question_4
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


