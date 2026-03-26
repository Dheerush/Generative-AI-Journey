import os


# ========================================== File Handling in Python ============================================
# 1. File handling = Performing operations on a file, such as creating, opening, reading, writing and closing it through a programming interface
#    - Managing the data flow between the program and the file system on the storage device, ensuring that data is handled safely and efficiently.
#    - File I/O = Read data from file + Write data to file
#    - Used in: logs, configs , datasets(AI), .csv/.json/.txt



# MODES
#          Mode      |     Meaning
# ---------------------------------------------         
#          "r"       |     Read  (default)
#          "w"       |     Write (overwrite)
#          "a"       |     Append
#          "r+"      |     Read + Write


# Tips: 
# 1) use "with" 
#    - It auto closes the file, safer and industry standard 




# Create New Folder using code
os.makedirs("1-basics/week2/data", exist_ok=True) 
# if the folder is already created, it wont create a new one, else a new one will be created



# ================================= Step 1: WRITE FILE ===================================
print("\n--- Writing to file ---")

# with open("test.txt", "w") as f:
#     f.write("Hello Dheeraj\n")
#     f.write("Learning File Handling\n")

# It will create a test.txt file in the root/working directory. 
# If you want to create the file in a specific folder



# Create file in a specific folder
with open("1-basics/week2/data/test.txt", "w") as f:
    f.write("Hello Dheeraj\n")
    f.write("Learning file handling\n")





# ================================= Step 2: READ FILE ===================================
print("\n--- Reading full file ---")
with open("1-basics/week2/data/test.txt", "r") as f:
    data=f.read()
    print("Printing all the read data: \n",data)






# =============================== Step 3: READ LINE BY LINE ================================
print("\n--- Read line by line ---")
with open("1-basics/week2/data/test.txt", "r") as f:
    for line in f:
        print(line.strip())





# =================================== Step 4: COUNT LINES ===================================
print("\n--- Counting lines ---")
lineCount=0

with open("1-basics/week2/data/test.txt", "r") as f:
    for line in f:
        lineCount=lineCount+1

print("Total number of lines in the data/test.txt file: ", lineCount)





# =================================== Step 5: COUNT WORDS ===================================
print("\n--- Counting words ---")
wordCount = 0
with open("1-basics/week2/data/test.txt", "r") as f:
    for line in f:
        wordCount += len(line.split())

print("Total number of words in the file: ", wordCount) 



# =================================== Step 6: CHECK FILE EXISTS OR NOT ===================================
print("\n--- Checking file exists ---")

if os.path.exists("1-basics/week2/data/test.txt"):
    print("File exists")
else:
    print("File not found")


# ================================ Step 7: USER INPUT LOGS/ADDS NEW LINE ====================================
print("\n--- Writing user input to file ---")

message = input("Enter the log message: ")
with open("1-basics/week2/data/test.txt", "a") as f:
    f.write(message + "\n")

print("Log saved successfully")




# NOTE: We have been mentioning the file path again and again (repititive). Use like this in future
# file_path = "1-basics/week2/data/test.txt"
# with open(file_path, "r") as f:



# =========================================== ADDITIONAL NOTES ====================================

# NOTE: f = file object (NOT just “file name”). It is a handle/connection to the file.


# 1. Using "with open()" (Recommended way)
#    - Automatically closes the file after block execution
#    - Prevents memory leaks and file corruption
#    - No need to manually call f.close()
#    - Industry standard (ALWAYS prefer this)

# Example:
# with open("file.txt", "r") as f:
#     data = f.read()



# 2. Manual File Handling (NOT recommended but important to know)
# f = open("file.txt", "r")
# data = f.read()
# f.close()   # must close manually

# ❌ Problem:
# If an error occurs before close(), file may remain open


# -------------------------------------------------------------

# 3. File Pointer (Cursor concept)

# When you read a file, a pointer moves forward

# Example:
# f.read() → reads entire file → pointer at end
# Next read() → returns empty

# Reset pointer:
# f.seek(0)


# -------------------------------------------------------------

# 4. Read Methods Difference

# f.read()       → returns full content (string)
# f.readline()   → returns one line
# f.readlines()  → returns list of all lines


# -------------------------------------------------------------

# 5. Write vs Append

# "w" → overwrite entire file (⚠️ dangerous)
# "a" → append to existing content (safe)

# Always be careful using "w"


# -------------------------------------------------------------

# 6. File Modes Combination

# "r+" → read + write (must exist)
# "w+" → write + read (overwrites)
# "a+" → append + read

# Example:
# with open("file.txt", "r+") as f:
#     data = f.read()


# -------------------------------------------------------------

# 7. File Paths

# Absolute Path → full system path
# Relative Path → project-based (preferred)

# Example:
# "data/file.txt"  → relative
# "C:/Users/..."   → absolute


# -------------------------------------------------------------

# 8. Always Handle File Errors (important for next topic)

# File may not exist → causes error

# Example:
# try:
#     with open("file.txt", "r") as f:
#         data = f.read()
# except FileNotFoundError:
#     print("File not found")


# -------------------------------------------------------------

# 9. Encoding (advanced but useful)

# Default encoding = system dependent

# Example:
# with open("file.txt", "r", encoding="utf-8") as f:
#     data = f.read()


# -------------------------------------------------------------

# 10. File as Iterable (VERY IMPORTANT)

# You can loop directly over file

# Example:
# with open("file.txt", "r") as f:
#     for line in f:
#         print(line.strip())

# This is memory efficient (used for large files)


# -------------------------------------------------------------

# 11. Good Practices

# ✔ Always use "with open()"
# ✔ Use relative paths
# ✔ Handle exceptions (try-except)
# ✔ Avoid using "w" unless needed
# ✔ Keep file path in a variable
# ✔ Use meaningful file names


# -------------------------------------------------------------

# 12. Real-World Usage

# Logs → append mode
# Configs → read mode
# Data processing → read line by line
# AI datasets → large file streaming






