import re
phoneRegex = re.compile(r'''
(
((\d\d\d) | (\(\d\d\d\)))? #area code
(\s|-) #first serparation
\d\d\d #first 3 digits
(\s|-) #second separation
\d\d\d\d #last digits
)
''', re.VERBOSE)

emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+ #user portion
@ 
[a-zA-Z0-9_.+]+ #domain poriton
''', re.VERBOSE)
print('Paste text here')
text = input()

nums = phoneRegex.findall(text)
email = emailRegex.findall(text)

allnums = []
for phonenumber in nums:
    allnums.append(phonenumber[0])
finalnum = '\n'.join(allnums)
finalemail = '\n'.join((email))
print('Phone numbers:')
print(finalnum)
print()
print('Emails:')
print(finalemail)

#Heavily inspired by Al Sweigert's example in Automate the Boring Stuff
