import json
import termcolor
from pathlib import Path

# -- Change the json file that is going to be read
jsonstring = Path("people-EX01.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)
# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'


# People counter
print (f"Total people in the database: {len(person)}")

for p in person:

    # Print the information on the console, in colors
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(p['Firstname'], p['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(p['age'])

    # Get the phoneNumber list
    phoneNumbers = p['phoneNumber']

    # Print the number of elements in the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    # Print all the numbers
    for i, num in enumerate(phoneNumbers):
        termcolor.cprint("  Phone {}:".format(i), 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])