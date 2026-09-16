#Expression Execution 

#Strings and numeric values can operate together with "*"

A,B = 2 ,3
Txt = "@"
print(A * Txt * B) #  #output :@@@@@@

#----------

A, B = 4, 2
Txt = "#"

print(A * Txt * B)   #output :########

# Strings can be added or multiplied with another strings 

A,B = "2" ,3
Txt = "@"
print((A + Txt )*B)  #output :2@2@2@

#--------
A, B = 2, 3
Txt = "@"
print(Txt * A + Txt * B)  #output : @@@@@
print(Txt * (A + B))      #output : @@@@@