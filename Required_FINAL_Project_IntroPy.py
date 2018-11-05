
# coding: utf-8

# # Final Project Required Coding Activity  
# Introduction to Python (Unit 2) Fundamentals  
# 
# **This Activity is intended to be completed in the jupyter notebook, `Required_FINAL_Project_IntroPy.ipynb`, and then pasted into the assessment page that follows.**   
#  
# All course .ipynb Jupyter Notebooks are available from the project files download topic in Module 1, Section 1.  
# 
# This activity is based on modules 1 - 4 and is similar to exercises in the Jupyter Notebooks **`Practice_MOD03_IntroPy.ipynb`** and **`Practice_MOD04_IntroPy.ipynb`** which you may have completed as practice.
# 
# | **Assignment Requirements** |
# |:-------------------------------|
# |This program requires the use of **`print`** output and use of  **`input`**, **`for`**/**`in`** loop, **`if`**, file **`open`**, **`.readline`**, **`.append`**, **`.strip`**, **`len`**. and function **`def`** and **`return`**. The code should also consider using most of the following (`.upper()` or `.lower()`, `.title()`, `print("hello",end="")` `else`, `elif`, `range()`, `while`, `.close()`) |
# 
# 
# ## Program: Element_Quiz  
# In this program the user enters the name of any 5 of the first 20 Atomic Elements and is given a grade and test report for items correct and incorrect.  
# 
# 
# ### Sample input and output:  
# ```
# list any 5 of the first 20 elements in the Period table
# Enter the name of an element: argon
# Enter the name of an element: chlorine
# Enter the name of an element: sodium
# Enter the name of an element: argon
# argon was already entered          <--no duplicates allowed
# Enter the name of an element: helium
# Enter the name of an element: gold
# 
# 80 % correct
# Found: Argon Chlorine Sodium Helium 
# Not Found: Gold 
# ```  
# 
# 
# ### Create get_names() Function to collect input of 5 unique element names  
# 
# - The function accepts no arguments and returns a list of 5 input strings (element names)  
# - define a list to hold the input
# - collect input of a element name  
# - if input it is **not** already in the list add the input to the list  
# - don't allow empty strings as input  
# - once 5 unique inputs **return** the list  
# 
# 
# ### Create the Program flow  
# 
# #### import the file into the Jupyter Notebook environment   
# 
# - use `!curl` to download https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt" as `elements1_20.txt`  
# - open the file with the first 20 elements  
# - read one line at a time to get element names, remove any whitespace (spaces, newlines) and save each element name, as lowercase, into a list  
# 
# 
# ####  Call the get_names() function  
# 
# - the return value will be the quiz responses list  
# 
# #### check if responses are in the list of elements  
# Iterate through 5 responses  
# - compare each response to the list of 20 elements
#   - any response that is in the list of 20 elements is correct and should be added to a list of correct responses  
#   - if not in the list of 20 elements then add to a list of incorrect responses  
# 
# #### calculate the % correct  
#  
#  - find the the number of items in the correct responses and divide by 5, this will result in answers like 1.0, .8, .6,...  
#  - to get the % multiple the calculated answer above by 100, this will result in answers like 100, 80, 60...  
#  - *hint: instead of dividing by 5 and then multiplying by 100, the number of correct responses can be multiplied by 20*  
# 
# #### Print output  
# 
# - print the Score % right  
# - print each of the correct responses  
# - print each of the incorrect responses  
# 
# 
# ### create Element_Quiz  then paste code on edX submission page
# 
# 

# In[19]:


# [] create Element_Quiz
# [] copy and paste in edX assignment page

def get_names():
    five_element_list = []
    
    #element = element_input.lower()
    while len(five_element_list) < 5:
        element_input = input("Enter the name of an element: ")
        if element_input not in five_element_list and element_input != '':
            five_element_list.append(element_input) 
        #if element_input in five_element_list:
         #   print(element_input, "was already entered")
         #   element_input = input("Enter the name of an element: ")
        elif element_input == '':
                print("Invalid entry")
        #elif element_input not in five_element_list:
         #   five_element_list.append(element_input)
        else:
            print(element_input, "was already entered")
            
    return five_element_list
          
get_ipython().system(u'curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt')
    
element_file = open('elements1_20.txt', 'r')

elements = element_file.readline().strip()

element_list = []

while elements:
    element_list.append(elements.lower())
    elements = element_file.readline().strip()
    
print(element_list)
    
five_elements = get_names()

correct_list = []
incorrect_list = []

for i in range(0,len(five_elements)):
    if five_elements[i] in element_list:
        correct_list.append(five_elements[i].title())
    else:
        incorrect_list.append(five_elements[i].title())
            
num_correct = len(correct_list)
perc_correct = int((num_correct/5) * 100)

print("\n" + str(perc_correct) + "% correct")
print("Found:", ' '.join(correct_list))
print("Not Found:", ' '.join(incorrect_list))


# ### Need assignment tips and clarification? 
# See the video on the "Final coding assignment > Required Final Project" course page on [edX](https://courses.edx.org/courses/course-v1:Microsoft+DEV274x+4T2017/course)    
# 
# # Important:  [How to submit code by pasting](https://courses.edx.org/courses/course-v1:Microsoft+DEV274x+2T2017/wiki/Microsoft.DEV274x.2T2017/paste-code-end-module-coding-assignments/)
# 

# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
