
# NOTES
# 1. Python uses indentation instead of {}
#    - Indentation is used to define blocks of code. 
#    - It indicates to the Python interpreter that a group of statements belongs to the same block.
#    - All statements with the same level of indentation are treated as part of the same code block.
#    - It is created using tabs or whitespaces and the commonly accepted convention is to use 4 spaces.
#    - Python expects the indentation level to be consistent within the same block else the inconsistency causes an IndentationError

# Example 1:
age = 18
if age>=18:
    print("Adult")
    print("Allowed to vote")
else:
    print("Not allowed to vote")



# Example 2:
marks = int(input("Enter the marks: "))
if marks>101 and marks<0:
    print("Invalid Marks")
elif marks>=90:
    print("A Grade")
elif marks >=80:
    print("B Grade")
elif marks>=70:
    print("C Grade")
elif marks >=60:
    print("D Grade")
elif marks >=40:
    print("E Grade")
else:
    print("NOT PASSED")





# ============================================== Strings ============================================================

name = "dheeraj"
empty=""
# Length of the string
print(f"Length of {name} is: ", len(name))   # 7
print(f"Length of {empty} is: ", len(empty)) # 0


# Indexing
print("Element at first index: ",name[0]) # d
print("Element at last index: ",name[-1]) # j


#Slicing 
print(name[1:]) # heeraj --> means from index 1 print till the last
print(name[2:]) # eeraj  --> means from index 2 print till the last 
print(name[-2:]) # aj    --> means from index -2 print till the last  --> -2 means 2 from the last which is 'a' so from a to the last character 


# Basic Methods
car = "MARUTI      "
bike= "bajaj"
print(f"Length of {car} is: ", len(car))      # 12 --> there are whitespaces
print(f"{car} in lowecase: ", car.lower())    # maruti
print(f"{bike} in UPPERCASE: ", bike.upper()) # BAJAJ


print("Strip: ", car.strip()) # strip() method in Python removes all leading and trailing whitespace by default.
print(f"Length of {car} is: ", len(car))
print("Length after strip: ", len(car.strip())) # strip() method in Python removes all leading and trailing whitespace by default. ---> since strings are immutable, hence strip returns a new string





river="narmada"
river.replace('a', 'o')
print(f"Name of the river is:  {river}") # Output: narmada --> this did not change as STRINGS ARE IMMUTABLE in python

#Correct way
speaker="philips"
speaker=speaker.replace('i','o');
print(f"{speaker} ") # pholops
# replace() does NOT modify original string. It returns a new string


sentence = "Hey Hey Hey hey how are you tomorrow is holiday holiday"
newSentence1= sentence.replace('Hey',"Hola", 1) # 1 here means that replace only till the first occurence 
newSentence2= sentence.replace('Hey',"Hola", 2) # 2 here means that replace only till the occurence 
print(newSentence1)
print(newSentence2)




# Membership ; checks if a substring exists in a string or not
movie="dhurandhar"
if('dha' in movie):
    print("Yes, it exists")
else :
    print("No, it does not exist")

if('dhd' in movie):
    print("Yes, it exists")
else :
    print("No, it does not exist")

# Inline check (best way)
print(f"Does {movie} include 'dhu'? {'dhu' in movie}")


device=input("Enter the device: ")
substr= input("Enter the substring: ")

print(f"Does {substr} exist in {device}: ", substr.lower() in device.lower())

# We can check for opposite ; instead of does exist we can check for does not exists
print(f"Does {substr} exist in {device}: ", substr.lower() not in device.lower()) 




# ========================================================= Exercise ====================================================
message="    All the best for placement DHEERAJ     "
# 1. Find Length
# 2. remove extra spaces
# 3. Length After Cleaning
# 4. check if "awesome" exists
# 5. convert to uppercase
# 6. convert to lowercase
# 7. Replace Word
# 8. Check if "placement" exists in string
# 9. Count how many words are in the string
# 10. Extract Substring
# 11. If "best" exists → print "Motivation detected" Else → print "Keep pushing"
# 12. Check if string starts with "All"
# 13. Check if string ends with "DHEERAJ"
# 14. Reverse the string


print("length of original message is: ", len(message))
message= message.strip()
print("Length of string after removing the whitespaces: ", len(message))
print("Does awesome exist in message: ", 'awesome' in message) # False
print("Message in lowercase: ", message.lower()) 
print("Message in uppercase: ", message.upper()) 
print("Replacing the word: ", message.replace("placement", "future")) #  replace() does NOT modify original string but returns a new string
print("Total words in the message: ", len(message.split())) #  split() will split the string into array ["All","the","best","for","placement","DHEERAJ"]

print("Extracting the substring: ", message[1:]) # ll the best for placement DHEERAJ
print("Extracting the substring: ", message[-1:]) # j

# Substring extraction improvement
start = message.find("for")
end =  message.find("DHEERAJ")
print("Starting indexing: ", start) # 13 
print("Ending indexing: ", end)     # 27

print(message[start:end]) # Output: for placement




if 'best' in message:
    print("Motivation detected")
else:
    print("Keep Pushing")

print("Does the message start with All ", message.startswith('All'))
print("Does the message end with All ", message.endswith('DHEERAJ'))


# Reverse String 
month="January"
print(f"Reversing the month {month}: ", month[::-1]) # yraunaJ --->s[::-1] does not modify but returns a new string



