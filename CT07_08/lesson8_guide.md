# Lesson 8 - String splitting, list joining, and
#            finding substring

## Recap 1: List Manipulation
Given 3 lists, merge them into a single list, remove
duplicates, and then split the list into 2 halves,
ensuring both halves are sorted.

list1 = [3, 2, 1]
list2 = [6, 5, 5]
list3 = [9, 8, 7]

1. Merge the 3 lists and remove duplicates.
2. Sort the resulting list.
3. Split the list into 2 sorted halves.
4. Print the halves.
5. 
---------------------------------------------------------------

## Task 1: Password Validation

A website requires all password to:
1. Be at least 8 characters long
2. Contain an upper and lower case
3. Contain a number
4. No other characters except alphabets or numbers

Task:
Write a program that will ask the user for a password, and
check if the password fits all criteria

You may use some of the following passwords to test your
program:
1. PassW0rd
2. H3ll0W0r1d
3. BestF00d
4. pa55Me

---------------------------------------------------------------

## Task 2: Mocking Text Generator

Create a program that will turn regular sentences into a
"SpongeBob Mocking" meme.

For example, the program will turn "Hello my name is James"
into "HeLlO mY nAmE iS jAmEs"

1. Using 'input()', ask the user for a sentence
2. Use loops to iterate through each letter of the sentence
3. Alternate between '.upper()' and '.lower()' for each letter
4. Print the result

---------------------------------------------------------------

## Task 3: Splitting a Sentence into Words (.split())
**Task 3a**:
Write a program to split the following string into a list of
words using space as the delimiter:

Example:
Input:
"Computers empower our modern world with their digital brains."

Output:
['Computers',
 'empower',
 'our',
 'modern',
 'world',
 'with',
 'their',
 'digital',
 'brains.']

**Task 3b**:
Write a program to split the following string into a list of
words using a comma (,) as the delimiter:

"Computers,empower,our,modern,world,with,their,digital,brains"

Example:
Input: "Computers,empower,our,modern,world,with,their,digital,brains"
Output: ['Computers',
         'empower',
         'our',
         'modern',
         'world',
         'with',
         'their',
         'digital',
         'brains.']

---------------------------------------------------------------

## Task 4: Joining Words into a Sentence (.join())
**Task 4a**:
Given the following list of words, write a program to join
these words into a single string, separated by spaces:

['Computers', 'empower', 'our', 'modern', 'world', 'with', 'their', 'digital', 'brains.']

Example:
Input: ['Computers', 'empower', 'our', 'modern', 'world', 'with', 'their', 'digital', 'brains.']
Output: "Computers empower our modern world with their digital brains."

**Task 4b**:
Given the following list of words, write a program to join
these words into a single string, separated by commas:

['Computers', 'empower', 'our', 'modern', 'world', 'with', 'their', 'digital', 'brains.']

Example:
Input: ['Computers', 'empower', 'our', 'modern', 'world', 'with', 'their', 'digital', 'brains.']
Output: "Computers,empower,our,modern,world,with,their,digital,brains"

---------------------------------------------------------------

## Task 5: Reversing Words in a Sentence
Create a program that takes the sentence "Hello World",
reverses each word, and then joins them back into a sentence.

1. Split the sentence "Hello World" into a list of words using
   space as the delimiter
2. Go through the list and reverse each word
3. Using space as the separator, join the list of reversed
   words back into a string
4. Print the reversed string

Example:
Sentence = "Hello World"
Output: 'olleH dlroW'

---------------------------------------------------------------

## Task 6: Checking if a Word is a Palindrome
Write a program to check if the word "radar" is a palindrome.
A word is a palindrome if it reads the same backward as forward.

Example:
Input: "radar"
Output: True

---------------------------------------------------------------

## Task 7: Checking user input for Palindrome
Create a while loop that will endlessly ask user for a word and
check if the word is a Palindrome.

The while loop will end when user says "end"

---------------------------------------------------------------

## Task 8: Checking user input for presence of Palindrome
Create a program that will check if a palindrome exists in a
sentence.

### Example:
Input:
Enter a sentence: <<"This is a sentence, check for palindrome">>

Output:
1 palindrome detected:
a

# Actual Lesson below!! :

# Lesson 8 - Input Validation

## Recap 1: List Manipulation
You have a list of student index numbers who attended the Math Enrichment class. 
However, some students’ attendance were recorded more than once due to a human error.
Your task is to clean the list and produce a list of unique Student Indexes

Given a list of student index numbers (with duplicates), create a cleaned list where each student appears once.
Sort the cleaned list in ascending order.
- Print the final list and also print how many duplicates were removed.
- Print the count of how many students attended the Math Enrichment Class.

student_indexes = [1042, 1099, 1031, 1120, 1075, 1042, 1108, 1019, 1063, 1099, 1156, 1027, 1084, 1111, 1031, 1143, 1055, 1108, 1070, 1132, 1055, 1168, 1020, 1084, 1175]

## Task 1: Data Format Check

### Task 1a
Ask the user to input their first name until it is a valid name. 
A valid name only contains alphabets.
Keep asking for a name until a valid name is input.

### Task 1b
Ask the user to input their age until it is a valid number. 
Keep asking for a name until a valid number is input.

### Task 1c
Ask the user to input a valid username. A valid username must contain alphabets and numbers, but not contain special characters

## Task 2: Length Check (using a while loop)

### Task 2a
Ask the user to input their phone number until it is valid using a while loop.
Make sure to check if the input is the correct data type as well!

### Task 2b
Ask the user to a username and check if it is between 5 to 18 characters long.

## Task 3: Range Check (using a while loop)

### Task 3a
Ask the user to input their birth year and check if it is between 1900 and the current year. Keep asking until a correct value is given.

### Task 3b
Ask the user to input their volume setting and check if it is between 0 and 100.

## Task 4: Mocking Text Generator
Create a program that will turn regular sentences into a “SpongeBob Mocking” meme.
For example, the program will turn “Hello my name is James” into “HeLlO mY nAmE iS jAmEs”

1. Using input(), ask the user for a sentence
2. Use loops to iterate through each letter in the sentence
3. Alternate between .upper() and .lower() for each letter
4. Print the result.

## Task 5: Slice String
word = “SINGAPORE”

Slice the string and print these words:
a. SING
b. GAP
c. PORE
d. SNAOE

## Task 6: Palindrome
Ask the user for an input and check if it is a palindrome, until the input is ‘end’.

You can try this list of words:
- civic, kayak, level, madam, radar, refer, rotator, tenet, racecar, deified, stats, wow

## Task 7: Presence and Existence Checks
You are hosting a Birthday Party and have invited your friends.

Create a list with your friends’ names
- e.g. [“Alice”, “Bob”, Carl”, “Dylan”]

Write a program to ask for the visitor’s name and check if:
- Name is entered (presence check)
- Name is in your friend list (existence check)

Ask for an input again if a name was not entered.
Accept the visitor if they are in the list, else deny their entry.

## Task 8: Format Check
Ask the user to input their NRIC you need to check:
1. First and last character are alphabets in upper case
2. First letter must be S, T, F, G, or M.
3. Have 7 digits between the alphabets
4. Be 9 characters long

## Task 9: Password Validation
A website requires all passwords to
1. Be at least 8 characters long
2. Contain an upper and lower case
3. Contain a number
4. No other characters except alphabets or numbers.

Write a program that will ask the user for a password, and check if the password fits all criteria

You may use some of the following passwords to test your program:
- PassW0rd
- H3ll0W0r1d
- BestF00d
- pa55Me
