import re  

# create a function isPasswordStrong 
def isStrongPass(password):
# create the Regex object from re.compile
    passwordRegex = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$', re.VERBOSE)
    passEvaluation = passwordRegex.search(password)
    if passEvaluation != None:  # if it is matched
         return True # Return this 

print('Enter your password: ')
password = input()

test = isStrongPass(password)
if test == True:
     print('Your password is STRONG')
else:
     print('Weak password')