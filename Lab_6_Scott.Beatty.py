''' Submitted by Scott Beatty 040590468 '''

print("welcome to Scottys String Comparison")
def compare_strings():
    first_string = input("Enter the first string: They are case sensitive: ")
    second_string = input("Enter the second string: They are case sensitive: ")
    if first_string == second_string: # checking to see if the two strings match they are case sensitive
        print("those two strings match, Great job!")
        tryagain = input("Would you like to try again? y = yes n = no : ")
        if tryagain == 'y' or tryagain == 'Y':  # checking to see if they want to run the program again
            compare_strings()
        elif tryagain == 'n' or tryagain == 'N':
            exit()
        else:
            print("Sorry you entered an invalid answer")
            compare_strings()

    if first_string != second_string: # checking to see if the strings do not match
        print("those two strings do not match!")
        tryagain = input("Would you like to try again? y = yes n = no : ")
        if tryagain == 'y' or tryagain == 'Y':
            compare_strings()
        elif tryagain == 'n' or tryagain == 'N':
            exit()
        else:
            print("Sorry you entered an invalid answer")
            compare_strings()

compare_strings() # calling the function here because we have to create the functioln first