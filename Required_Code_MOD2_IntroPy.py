
# coding: utf-8

# #  Module 2 Required Coding Activity  
# Introduction to Python (Unit 2) Fundamentals 
# 
# **This Activity is intended to be completed in the jupyter notebook, Required_Code_MOD2_IntroPy.ipynb, and then pasted into the assessment page that follows.**   
#  
# All course .ipynb Jupyter Notebooks are available from the project files download topic in Module 1, Section 1.
# 
# This is an activity based on code similar to the Jupyter Notebook **`Practice_MOD02_IntroPy.ipynb`** which you may have completed.  
# 
# | Important Assignment Requirements |  
# |:-------------------------------|  
# | **NOTE:** This program requires creating a function using **`def`** and **`return`**, using **`print`** output, **`input`**, **`if`**, **`in`** keywords, **`.append()`**, **`.pop()`**, **`.remove()`** list methods.  As well as other standard Python |   
# 
# ## Program: list-o-matic  
# This program takes string input and checks if that string is in a list of strings    
# - if string is in the list it removes the first instance from list  
# - if string is not in the list the input gets appended to the list  
# - if the string is empty then the last item is popped from the list 
# - if the **list becomes empty** the program ends  
# - if the user enters "quit" then the program ends  
# 
# program has 2 parts  
# - **program flow** which can be modified to ask for a specific type of item.  This is the programmers choice.  Add a list of fish, trees, books, movies, songs.... your choice.  
# - **list-o-matic** Function which takes arguments of a string and a list.  The function modifies the list and returns a message as seen below.  
# 
# ![TODO: upload image to blob](https://q4tiyg-ch3302.files.1drv.com/y4mkvwrxHSIqinTvp_nNGFiMn_yyJ0dsEtCzPpG_hsFMRdyEED4ExPdsWmbdPIKRpgU25VxFIUAGBdz0yzqumtxw7wy_pAJMJ3MeZ6PJQKyej6UwN6N6zOmnRq6106aqvXJB43RKRJgB2oMmidb9Zl0OBjmvFVowm-XtD2wUW5bJrgd4LS8I5Nso_vXqfpNCANRYcKe4WnjIWds4KoV4sjPIg?width=717&height=603&cropmode=none)
# 
# **[ ]** initialize a list with several strings at the beginning of the program flow and follow the flow chart and output examples
# 
#  *example input/output*  
#  ```
# look at all the animals ['cat', 'goat', 'cat']
# enter the name of an animal: horse
# 1 instance of horse appended to list
# 
# look at all the animals ['cat', 'goat', 'cat', 'horse']
# enter the name of an animal: cat
# 1 instance of cat removed from list
# 
# look at all the animals ['goat', 'cat', 'horse']
# enter the name of an animal: cat
# 1 instance of cat removed from list
# 
# look at all the animals ['goat', 'horse']
# enter the name of an animal:          (<-- entered empty string)
# horse popped from list
# 
# look at all the animals ['goat']
# enter the name of an animal:          (<-- entered empty string)
# goat popped from list
# 
# Goodbye!
# ```  
# 
# *example 2*
# ```
# look at all the animals ['cat', 'goat', 'cat']
# enter the name of an animal: Quit
# Goodbye!
# ```  
# 
# 

# In[18]:


# [] create list-o-matic
# [] copy and paste in edX assignment page
animal_list = ['cat', 'goat', 'cat']
def list_o_matic(animal_input):
    if animal_input == "":
        val = animal_list.pop()
        pop_msg = val + " popped from list\n"
        return pop_msg
    else:
        if animal_input in animal_list:
            animal_list.remove(animal_input)
            remove_msg = "1 instance of " + animal_input + " removed from list\n"
            return remove_msg
        else:
            animal_list.append(animal_input)
            append_msg = "1 instance of " + animal_input + " appended to list\n"
            return append_msg
    

while animal_list:
    print("Look at all the animals", animal_list)
    animal_input = input("Enter the name of the animal: ")
    if animal_input.lower() == 'quit':
        break
    else:
        print(list_o_matic(animal_input))

print("Goobye!")


# ### Need assignment tips and clarification? 
# See the video on the "End of Module coding assignment > Module 2 Required Code Description" course page on [edX](https://courses.edx.org/courses/course-v1:Microsoft+DEV274x+4T2017/course)    
# 
# # Important:  [How to submit code by pasting](https://courses.edx.org/courses/course-v1:Microsoft+DEV274x+2T2017/wiki/Microsoft.DEV274x.2T2017/paste-code-end-module-coding-assignments/)
# 

# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
