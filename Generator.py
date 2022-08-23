from multiprocessing.sharedctypes import Value
import os
import random
import string
from datetime import datetime

# Chooses all characters to create a password from
passwordChars = string.ascii_letters + string.digits + string.punctuation

# Set the correct path for "logs" to be created
path = "logs"

# Get current time to get a unique name for the created ".txt" file. Prevents .txts to be overwriten (not impossible that it happens, but way harder to do).
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# Tries to create the directory "logs". Checks if the OS throws an error. If it doesn't the directory is created. Else it isn't.
try: 
    os.mkdir(path)

except OSError:
    print("")

else:
    print("Successfully created the directory %s." % path)

# Asks how long the generated password should be. If it's not a number it'll keep asking the user to input a valid number.
lengthAccepted = False
while lengthAccepted == False:
    try: 
        passwordLength = int(input("How long do you want your generated password to be?"))
    except ValueError:
        print("Unaccepted length given. Please enter a number")
        lengthAccepted = False
    else: 
        lengthAccepted = True
    # Checks if input is "0". If 0 it'll not be accepted.    


# Generates the password with all the characters given above.
password = "".join(random.choice(passwordChars) for i in range (passwordLength))
passwordLength = str(passwordLength)

# Terminal output
print("Generating password with " + passwordLength + " characters..")
print("Password successfully generated.")
print("Password: " + password)

# Asks user to select a name for the file in which the password is saved.
print("\033[41m" + "WARNING: Using duplicated names will result in the old file being overwritten!" + "\033[0m")
fileName = input("Please enter a name for the file including the generated password.")

# Creates ".txt" file including the password.
try:    
    with open("logs/" + fileName + ".txt", "w") as f:
        f.write("Password: ")
        f.write(password)
except OSError:
    print("Unaccepted file name.")
else: 
    print("File creation successful.")
    
try:    
    with open("latest.txt", "w") as f:
        f.write("Password: ")
        f.write(password)
except OSError:
    print("")
else: 
    print("Your latest.txt has been updated.")








