import random

# TAKE user input, how many people want to join including the user
people = int(input("Enter the number of friends joining (including you):\n"))

# IF people is 0 or negative, say no one is joining
if people > 0:
  
    # DEFINE number of inputs from people
    inputs = people
  
    # DEFINE the lines as strings
    lines = ""
  
    # PRINT 'Enter the name of every friend (including you), each on a new line:'
    print("\n" + "Enter the name of every friend (including you), each on a new line:")
  
    # FOR each person in int(people)
    for i in range(inputs):
      
        # TAKE integer input
        lines += input() + " "
      
    # DEFINE names as a one new string of each line combined into one
    names = lines.split()
  
    # DEFINE a new dict from names, where the keys are names and the value is 0
    names_dict = dict.fromkeys(names, 0)
  
    # INPUT total bill
    total = float(input("\n" + "Enter the total bill value:\n"))
  
    # DEFINE total for each person as total / the number of people
    total_each = total / people
  
    # FORMAT the split bill value to 2 decimal places
    total_each = "{:.2f}".format(total_each)
  
    # UPDATE the value in each key:value pair with the value of total_each
    for key in names_dict:
        names_dict[key] = names_dict[key] + float(total_each)
      
    # INPUT yes or no for if user is feeling lucky
    feeling_lucky = input("\nDo you want to use the 'Who is lucky' feature? Write Yes/No:\n")
  
    # IF statement checking whether user is feeling_lucky
    if feeling_lucky == 'Yes' or feeling_lucky == 'yes' or feeling_lucky == 'YES':
      
        # GENERATE random name from to list(names_dict)
        lucky_person, lucky_value = random.choice(list(names_dict.items()))
      
        # PRINT random lucky person
        print(f'\n{lucky_person} is the lucky one!')
      
        # DEFINE value to decrement from lucky person
        value_to_decrement = float(total_each)
      
        # ADD decremented value to total
        total = value_to_decrement * people
      
        # CALCULATE total_each after the value of 1 person has been set to 0
        total_each = total / (people - 1)
      
        # FORMAT the split bill value to 2 decimal places
        total_each = float("{:.2f}".format(total_each))
      
        # GENERATE new_dict from names_dict and total_each
        names_dict = dict.fromkeys(names_dict, total_each)
      
        # DEFINE updates to be performed
        updates = {lucky_person: 0}
      
        # UPDATE names_dict
        names_dict.update(updates)
      
        # PRINT TOTAL
        print(f"\n{names_dict}")
      
    # ELSE not feeling lucky
    else:
      
        # PRINT no one will be lucky
        print('No one is going to be lucky')
      
        # PRINT dict of names
        print(f'\n{dict(names_dict)}')
      
else:
    print("No one is joining for the party")
