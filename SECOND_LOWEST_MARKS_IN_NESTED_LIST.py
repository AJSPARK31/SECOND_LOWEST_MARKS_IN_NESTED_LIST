#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# second_lowest_marks_in_nested_list

# Given the names and grades for each student in a class of  students, 
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, 
#       order their names alphabetically and print each name on a new line.


student_list=[]

# input from users and creating nested list of student and their scores
for i in range(int(input())):
        student_list.append([])
        name = input()
        score = float(input())
        student_list[i].append(name)
        student_list[i].append(score)
        
# printing nested list of student and their scores
print(student_list)

# getting minimum score in the list
min_value=min(student_list,key=lambda x:x[1])
print(min_value)

# creating a new list without minimum score
list_with_out_min=[]
for  i in range(len(student_list)):
    if student_list[i][1]!=min_value[1]:
        list_with_out_min.append(student_list[i])
print(list_with_out_min)

# getting second lowest score from the without minimum score of list
second_lowest=min(list_with_out_min,key=lambda x:x[1])
print(second_lowest)
# creating a new list if there is more students with minimum scores
second_lowest_scorers=[]
for  i in range(len(list_with_out_min)):
    if list_with_out_min[i][1]==second_lowest[1]:
        second_lowest_scorers.append(list_with_out_min[i][0])

print(second_lowest_scorers)

# sorting the second lowest scorers via alphabets
second_lowest_scorers=sorted(second_lowest_scorers)

# printing the second lowest scorer names
for i in second_lowest_scorers:
    print (i)       
    


# In[1]:


print("second_lowest_marks_in_nested_list".upper())


# In[ ]:




