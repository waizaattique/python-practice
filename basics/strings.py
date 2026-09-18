#Strings 

#Question no 1 

A,B = 2 ,3
Txt = "@"
print(A * Txt * B) #  #output :@@@@@@

#Question no 2

A, B = 4, 2
Txt = "#"

print(A * Txt * B)   #output :########

#Question no 3

A,B = "2" ,3
Txt = "@"
print((A + Txt )*B)  #output :2@2@2@

#Question no 4
A, B = 2, 3
Txt = "@"
print(Txt * A + Txt * B)  #output : @@@@@
print(Txt * (A + B))      #output : @@@@@

#Question no 5
Txt = "@"
A = 5
print(Txt * A) #Output : @@@@@

#Question no 6

Txt = "*"
a , b = 3 , 2 
print(Txt * a + Txt * b) #Output : *****

#Question no 7

Txt = "#"
a , b = 2, 3
print(Txt *(a + b)) #Output : #####

#Question no 8

word = "Hi"
print(word * 3) #Output : HiHiHi

#Question no 9   ---**Challenge**---

a, b = 4 , 3
Txt = "$"
print(Txt * a) #Output : $$$$
print(Txt * b) #Output : $$$
print(Txt * (a + b)) #Output : $$$$$$$
