Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
#Task 1_________________________________________________________________________

"""По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания. """

N= int(input())
i=1
while i**2<N:
	print(i**2, end=" ")
	i+=1   
#Task2______________________________________________________________________________
"""
 Дано целое число, не меньше 2. Выведите его наименьший натуральный делитель отличный от 1.
 """
 num = int(input())
 delitel = 2
 while num % delitel != 0:
 	delitel += 1
 print(delitel)
 #_________________________________________________________________________________



#Task3_______________________________________________________________________________
 """По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N. Выведите показатель степени и саму степень.
Операцией возведения в степень пользоваться нельзя! """

N=int(input())
z=0
i=1
pover=0
while i<= N:
    i=i*2
    z+=1
print(z-1,i-i//2)
#____________________________________________________________________________________

#Task4_______________________________________________________________________________
"""  В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения. По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.

Программа получает на вход действительные числа x и y и должна вывести одно натуральное число. """

x=int(input())
y=int(input())
i=1
while x<y:
    x=x+((x/100)*10)
    i=i+1
print(i)
#___________________________________________________________________________________

#Task5_______________________________________________________________________________
""" Вклад в банке составляет x рублей. Ежегодно он увеличивается на p процентов, после чего дробная часть копеек отбрасывается. Определите, через сколько лет вклад составит не менее y рублей.

Выражение «дробная часть копеек отбрасывается» означает, что если у вас оказалось 123.4567 рублей, т. е. 123 рубля и 45.67 копеек, то после округления у вас получится 123 рубля и 45 копеек, т.е. 123.45 рублей.

Программа получает на вход три натуральных числа: x, p, y и должна вывести одно целое число. """
x=int(input())
p=int(input())
y=int(input())
i=0
while  x<y:
    x=x*(1+p/100)
    x=(x*100)//1/100
    i=i+1
print(i)
#____________________________________________________________________________________
#Task6_______________________________________________________________________________-
"""   Программа получает на вход последовательность целых неотрицательных чисел, каждое число записано в отдельной строке. Последовательность завершается числом 0, при считывании которого программа должна закончить свою работу и вывести количество членов последовательности (не считая завершающего числа 0). Числа, следующие за числом 0, считывать не нужно."""
i=0
x=int(input())
while x!=0:
    x=int(input())
    i=i+1
print(i)
#____________________________________________________________________________________


#Task7_______________________________________________________________________________-

""" Определите сумму всех элементов последовательности, завершающейся числом 0. В этой и во всех следующих задачах числа, следующие за первым нулем, учитывать не нужно. """

x =int(input())
y=0
y=x
z=0
while x!=0:
    x=int(input())
    z=x+z 
a=z+y
print(a)
#____________________________________________________________________________________

#Task8_______________________________________________________________________________-
"""  Определите среднее значение всех элементов последовательности, завершающейся числом 0. """
x=int(input())
y=0
y=x
i=0
z=0
while x!=0:
    x=int(input())
    z=x+z 
    i=i+1
Sum=(z+y)/i
print(Sum)
#____________________________________________________________________________________

#Task9_______________________________________________________________________________
"""
 Последовательность состоит из натуральных чисел и завершается числом 0. Определите значение наибольшего элемента последовательности. 
 """
 max = 0
 x = int(input())
 while x != 0:
     if max < x:
         max = x
     x = int(input())
 print(max)

#____________________________________________________________________________________

#Task10______________________________________________________________________________
"""
 +Последовательность состоит из натуральных чисел и завершается числом 0. Определите индекс наибольшего элемента последовательности. Если наибольших элементов несколько, выведите индекс первого из них. Нумерация элементов начинается с нуля. 
 """
 maximum = 0
 i = -1
 check = 0
 x = int(input())
 while x != 0:
     i += 1
     if maximum < x:
         maximum = x
         check = i
     x = int(input())
 print(check)


#____________________________________________________________________________________

#Task11______________________________________________________________________________

"""
 Определите количество четных элементов в последовательности, завершающейся числом 0. 
 """
 x = int(input())
 i = 0
 while x != 0:
     if x % 2 == 0:
         i += 1
     x = int(input())
 print(i)
 #____________________________________________________________________________________

#Task12______________________________________________________________________________
"""
 Последовательность состоит из натуральных чисел и завершается числом 0.
 Определите, сколько элементов этой последовательности больше предыдущего элемента.
 """
 x = int(input())
 x0 = 0
 i = -1
 while x != 0:
 	if x0 < x:
 		i += 1
 	x0 = x
 	x = int(input())
 print(i)
#____________________________________________________________________________________

#Task13______________________________________________________________________________
"""
 Последовательность состоит из различных натуральных чисел и завершается числом 0.
 Определите значение второго по величине элемента в этой последовательности.
Гарантируется, что в последовательности есть хотя бы два элемента.
 """
 max1 = 0
 max2 = 0
 x = int(input())
 while x != 0:
 	if x < max1 and x > max2:
 		max2 = x
 	if max1 < x:
 		max2 = max1
 		max1 = x
 	x = int(input())
 	print(max2)	
#____________________________________________________________________________________





