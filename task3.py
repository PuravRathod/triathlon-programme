# in line 3,4,5-  defined all 3 variables as (int) so it can  be used in arithmetic operators#
# in line 6 converted into string to do the calculation as discussed in the online lectures by chris.#
# used chat gpt to debug the errors-- TypeError: '<=' not supported between instances of 'str' and 'int'#
num1=100
num2=105
num3=110
swimming= int (input ("please enter time taken for swimming-"))
cycling= int (input("please enter time taken for cycling-"))
running= int (input("please enter time taken for running-"))
total_triathlon_time = str (swimming+cycling+running)
print ("total time taken-"+ total_triathlon_time)
if int (total_triathlon_time)<= num1:
    print ("Provincial colours")
elif int (total_triathlon_time) <=num2:
    print (" Provincial Half colours")
elif int (total_triathlon_time) <=num3:
    print ("Provincial scroll")
else:
    print ("No Award")