my_tuple  = ('one',2,'three',4,-5) # create our tuple list called my_tuple
my_second_tuple = ('this',2,'will',3,'removed')
for x in range(5):  # loop through the list and print each element
    print(my_tuple[x])
which_one = int(input('Which element would you like to access?  ')) # ask user which element they would like to access
print(my_tuple[which_one]) # print the element from user input

which_negitive_index = int(input("Now please enter a negitive element  ")) # negitive indexing basically
# goes backwards through the tuple list - ask user for a negitive number this time to access the element
print(my_tuple[which_negitive_index])

print(my_second_tuple) # you will see that I printed the second tuple
del my_second_tuple
print(my_second_tuple + "This will throw an error because we jsut deleted the second tuple")