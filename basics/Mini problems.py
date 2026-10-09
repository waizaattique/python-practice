#Question no 1 : A notebook costs 120 rupees. You buy 4 notebooks. Write a program to calculate the total cost.


cost = 120
quantity = 4
Total_cost = cost * quantity
print(Total_cost)      #Output: 480


#Question no 2 : You have 1000 rupees. You spend:
#• 250 rupees
#• 175 rupees
#• 80 rupees
#Write a program to calculate how much money remains

initial_amount = 1000
spend_1 = 250
spend_2 = 175
spend_3 = 80
remaining_amount = initial_amount - (spend_1 + spend_2 + spend_3)
print(remaining_amount)  #Output: 495


#Question no 3 : You scored: 85, 72, 90. Write a program to calculate the average

score_a = 85
score_b = 72
score_c = 90
average = (score_a + score_b + score_c) / 3
print(average)  #Output: 82.33333333333333

#Question no 4 :There are 47 students. Each group can have 6 students. Use // to find the number of complete groups. Then
#use % to find how many students are left over

Students = 47
Groups = 6
total_groups = Students // Groups
leftover_students = Students % Groups
print("Total_groups:", total_groups)  #Output: 7
print("Leftover_students:", leftover_students)  #Output: 5


#Question no 5 : Write a program to print the following pattern
#Your program should print:
#****
#***
#Then modify it so it prints the following, using the same variables:
#*******

a = 4
b = 3
Txt = "*"
print(Txt *   a  + "\n" + Txt *b  )
print(Txt *(a +b))


#Question no 6 : predict the output of the following code snippet and then run it to see if you were correct

A, B, C = 12, 5, 2
Txt = "#"
print(A + B)  #Output: 17
print(A - B)  #Output: 7
print(A * B)  #Output: 60
print(A / B)  #Output: 2.4
print(A // B) #Output: 2
print(A % B)  #Output: 2
print(A + B * C)  #Output: 22
print((A + B) * C)  #Output: 34
print(Txt * A) #Output: ############
print(Txt * (B + C))   #Output: #######