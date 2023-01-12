#1. Under the num_list create a new for loop and print out each value on the list in sequential order.

#2. Inside the for loop, create a condition that will look for all numbers that are greater than 45 and print out only numbers that meet that condition

#3. Change the print statement to “Over 45” and add an else condition with a print statement of “Under 45”.

#4. Update the for loop to use the enumerate function so you can get and use the index. Alter the condition to look for number 36 and print out the following: ‘Number found at position: ‘, index number

#5. Next, create a new variable called count and assign it a value of 0 and place it outside the for loop.

#6. Inside the for loop increment the counter by 1.

#7. Add a print statement outside the for loop to print the value of the count variable.

#8. Finally, add a break statement directly after the print statement inside the if condition for finding the number. 



Here is the List to use in this test:

num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
count = 0
x = len(num_list)
print (x)

for i in num_list:
    print(i)

#a condition that will look for all numbers that are greater than 45 and print out only numbers that meet that condition

for i in num_list:
    if i > 45:
        print("over 45:",i)
    else:
        print("Under 45:",i)

for index, num_list in enumerate(num_list):
    if num_list == 36:
        count += 1
        print(f'Number found at position: {index}')
        break
print(f'Number 36 found {count} times in the list')