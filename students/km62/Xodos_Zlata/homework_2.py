#task1--------------------------------------------------------------------------------------------------------------------------------
“””Дано два цілих числа. Вивести найменше з них.  “””

print("Please, enter two numbers")

first_number=int(input("First number: "))
second_number=int(input("Second number: "))

if (first_number<second_number):
    print("The first number ",first_number," is less than second")
elif (second_number<first_number):
    print("The second number ",second_number," is less than first")
else: print("The first number is equal to the second")
#----------------------------------------------------------------------------------------------------------------------------------------


#task2--------------------------------------------------------------------------------------------------------------------------------
“””Вивести результат функції sign(x), що визначається наступним чином:  “””

"""sign(x)=1, коли x>0 
sign(x)=-1, коли x<0
sign(x)=0, коли x=0"""

x=float(input("Enter x: "))

if (x>0):
    print("sign(",x,") is 1")
elif (x<0):
    print("sign(",x,") is -1")
else: print("sign(",x,") is 0")
#----------------------------------------------------------------------------------------------------------------------------------------


#task3--------------------------------------------------------------------------------------------------------------------------------
“””Дано три цілих числа. Вивести найменше з них.  “””
print("Please, enter three numbers")

first=int(input("First number: "))
second=int(input("Second number: "))
third=int(input("Third number: "))

if (first<second) and (first<third):
    print("The smallest number is ",first)
elif (second<first) and (second<third):
    print("The smallest number is ",second)
else:
    print("The smallest number is ",third)
#----------------------------------------------------------------------------------------------------------------------------------------


#task4--------------------------------------------------------------------------------------------------------------------------------
“””Дано ціле число, що визначає рік. Визначити, чи є вказаний рік високосним. 
Якщо так, то вивести користувачу "LEAP", в іншому випадку – "СOMMON".“””

print("Please, enter a year in format XXXX")

year=int(input("Year: "))

if ((year%4==0) and (year%100!=0)) or (year%400==0):
    print ("LEAP")
else: print("COMMON")
#----------------------------------------------------------------------------------------------------------------------------------------


#task5--------------------------------------------------------------------------------------------------------------------------------
“””Дано три цілих числа. Визначте, скільки з них дорівнюють один одному. 
Програма повинна виводити одне з чисел: 3 (якщо всі числа однакові), 
2 (якщо два з них дорівнюють один одному, а третє відрізняється) або 0 (якщо всі числа різні).“””

print("Please, enter three numbers")

first=int(input("First number: "))
second=int(input("Second number: "))
third=int(input("Third number: "))

if first==second:
    if second==third:
        print("3")
    else: print("2")
else:
    if second==third or first==third:
        print("2")
    else: print("0")
#----------------------------------------------------------------------------------------------------------------------------------------

#task6--------------------------------------------------------------------------------------------------------------------------------
“””Шахова тура переміщається по горизонталі або по вертикалі. Дано координати двох клітин шахової дошки. 
Визначити, чи може тура перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає 
номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої.
Програма має вивести "YES", якщо тура може виконати переміщення, або "NO" в іншому випадку. “””

print("Please, enter four coordinates from 1 to 8 in format X")

x1=int(input("X1 is: "))
y1=int(input("Y1 is: "))
x2=int(input("X2 is: "))
y2=int(input("Y2 is: "))

if y1==y2 or x1==x2:
    print("YES")
else: print("NO")
#----------------------------------------------------------------------------------------------------------------------------------------


#task7--------------------------------------------------------------------------------------------------------------------------------
“””Дано координати двох клітин шахової дошки. Визначити, чи однакового вони кольору. 
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика 
клітини. Перші два числа - для першої клітини, останні два числа – для другої. 
Програма має вивести "YES", якщо колір однаковий, або "NO" в іншому випадку. """

"""
black - x парні, у парні
        х непарні, у непарні
white - х парні, у непарні
        х непарні, у парні

"""

print("Please, enter four coordinates from 1 to 8 in format X")

x1=int(input("X1 is: "))
y1=int(input("Y1 is: "))
x2=int(input("X2 is: "))
y2=int(input("Y2 is: "))

if (x1%2==1 and y1%2==1) or (x1%2==0 and y1%2==0): #for first - black 
    if (x2%2==1 and y2%2==1) or (x2%2==0 and y2%2==0): #for second - black 
        print("YES") 
    else: #for second - white 
        print("NO") 
else: #for first - white 
    if (x2%2==1 and y2%2==0) or (x2%2==0 and y2%2==1): #for second - white 
        print("YES") 
    else: #for second - black 
        print("NO")
#----------------------------------------------------------------------------------------------------------------------------------------

#task8--------------------------------------------------------------------------------------------------------------------------------
“”” Шаховий король переміщується по горизонталі, по вертикалі або по діагоналі на будь-яку сусідню клітинку. 
Дано координати двох клітин шахової дошки. Визначити, чи може король перейти з першої клітини у другу за один хід. 
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. 
Перші два числа - для першої клітини, останні два числа – для другої. 
Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку."""

print("Please, enter four coordinates from 1 to 8 in format X")

x1=int(input("X1 is: "))
y1=int(input("Y1 is: "))
x2=int(input("X2 is: "))
y2=int(input("Y2 is: "))

if (x2==x1+1 and y2==y1-1) or (x2==x1+1 and y2==y1+1):
    print("YES")
elif (x2==x1-1 and y2==y1-1) or (x2==x1-1 and y2==y1+1):
    print("YES")
elif (x2==x1+1 and y1==y2) or (x2==x1-1 and y1==y2):
    print("YES")
elif (x1==x2 and y2==y1+1) or (x1==x2 and y2==y1-1):
    print("YES")
else: 
    print("NO")
#----------------------------------------------------------------------------------------------------------------------------------------


#task9--------------------------------------------------------------------------------------------------------------------------------
“””Шаховий слон рухається по діагоналі на будь-яку кількість клітин. Дано координати двох клітин шахової дошки. 
Визначити, чи може слон перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та 
стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. 
Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку. """

"""
black - x парні, у парні
х непарні, у непарні
white - х парні, у непарні
х непарні, у парні
"""

print("Please, enter four coordinates from 1 to 8 in format X")

x1=int(input("X1 is: "))
y1=int(input("Y1 is: "))
x2=int(input("X2 is: "))
y2=int(input("Y2 is: "))

if (x1%2 == 1 and y1%2 == 1) or (x1%2 == 0 and y1%2 == 0): 
	if (x2%2 == 1 and y2%2 == 1) or (x2%2 == 0 and y2%2 == 0): 
		if (x2-x1 == y1-y2) or (x2-x1 == y2-y1):
			print("YES")
		elif (x1-x2 == y1-y2) or (x1-x2 == y2-y1):
			print("YES")
		else:
			print("NO")   
	else:
		print("NO") 
else: 
	if (x2%2 == 1 and y2%2 == 0) or (x2%2 == 0 and y2%2 == 1): 
		if (x2-x1 == y1-y2) or (x2-x1 == y2-y1):
			print("YES")
		elif (x1-x2 == y1-y2) or (x1-x2 == y2-y1):
			print("YES")
		else:
			print("NO") 
	else: 
		print("NO")
#----------------------------------------------------------------------------------------------------------------------------------------


#task10--------------------------------------------------------------------------------------------------------------------------------
“”” Шахова королева рухається по горизонталі, по вертикалі або по діагоналі на будь-яку кількість клітин. 
Дано координати двох клітин шахової дошки. Визначити, чи може королева перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа 
від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. 
Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку. """

print("Please, enter four coordinates from 1 to 8 in format X")

x1=int(input("X1 is: "))
y1=int(input("Y1 is: "))
x2=int(input("X2 is: "))
y2=int(input("Y2 is: "))

if ((x1==x2) or  (y1==y2)) or ( abs(x2-x1)==abs(y2-y1)):
    print('YES')
else:
    print('NO')
#----------------------------------------------------------------------------------------------------------------------------------------


#task11--------------------------------------------------------------------------------------------------------------------------------
“”” Шаховий кінь рухається як літера L. Він може переміщатись на дві клітинки по горизонталі і одну клітинку по вертикалі або на дві клітинки по вертикалі і 
одну по горизонталі. Дано координати двох клітин шахової дошки. Визначити, чи може кінь перейти з першої клітини у другу за один хід. Користувач вводить чотири 
цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. 
Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку."""

print("Please, enter four coordinates from 1 to 8 in format X")

x1=int(input("X1 is: "))
y1=int(input("Y1 is: "))
x2=int(input("X2 is: "))
y2=int(input("Y2 is: "))

if (x1+1==x2) and (y1+2==y2):
    print('YES')
elif (x1+2==x2) and (y1+1==y2):
    print('YES')
elif (x1+2==x2) and (y1-1==y2):
    print('YES')
elif (x1+1==x2) and (y1-2==y2):
    print('YES')
elif (x1-1==x2) and (y1-2==y2):
    print('YES')
elif (x1-2==x2) and (y1-1==y2):
    print('YES')
elif (x1-2==x2) and (y1+1==y2):
    print('YES')
elif (x1-1==x2) and (y1+2==y2):
    print('YES')
else:
    print('NO')
#----------------------------------------------------------------------------------------------------------------------------------------


#task12--------------------------------------------------------------------------------------------------------------------------------
“””Шоколад має форму прямокутника, розділеного на n×m клітин. Шоколад може бути розділений на дві частини тільки по горизонталі або по вертикалі, 
при цьому клітини мають бути цілими. Визначити, чи можна розділити шоколад за один крок таким чином, щоб одна з частин матиме точно k клітин. 
Програма має вивести "YES", якщо шоколад можна поділити, або "NO" в іншому випадку. """

print("Please, enter sizes of chocolate in order n,m,k")

n=int(input("n is: "))
m=int(input("m is: "))
k=int(input("k is: "))
i=0

if (k%n==0) and ((k//n)<m):
    i=1
if (k%m==0) and ((k//m)<n):
    i=1
if i==1:
    print('YES')
else:
    print('NO')