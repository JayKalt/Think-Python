# CHAPTER 5, STRINGS
## 1. Summary of nice-to-have methods and functions
### METHODS
#### For the char case
```
. string.upper()       >  changes all string char from lower to upper<br>
. string.lower()       >  same as lower but viceversa<br>
. string.capitalize()  >  capitalize the first letter<br>
. string.swapcase()    >  revert the case of each char<br>
```
#### Convert string to list
```
. string.split()        >  splits a string of multi words into a list of single words, removing whitespace<br>
```
#### Find char in a string
```
. string.find(target) > find the target in a string<br>
. string.rfind(target) > find the target but reverse (starting from the last position)<br>
```
### FUNCTIONS
#### List function
```
. enumerate(list)  > associates each element to its index<br>
```
-----
<br><br>

## 2. String related notions
### 2.1 Negative indexing
We can work with negative index that starts from the end of the word and goes up to the first.
E.G:
```
  world = "Test"
  word[-1] = t
```
You can use it for index of any string.
To reverse a word you can say:
E.G:
```
  word[::-1]
```
It will print the string reversed!

-----
### 2.2 String comparison
We can compare strings and it works as a normal dictionary.
The only thing to really remember is that upper case letteres come first then lowercase letters

-----
### 2.3 Strings are immutables!
String cannot be chainged unless we create new ones or re-assigne the existing ones

-----
### 2.4 Optional parameters in methods
Optional parameters are assigned if they find a match between the call and the arguments.
If they don't, it will be assigned a default vaule.
E.G:
```
  def find(haystack, needle, start=0):
    ...
```
In this case, if the call finds a match to the start parameter it will
assign the value, else start will be zero.


-----
### 2.5 Formatting methods
If we want to format a method we can do it using the ```format``` method:
E.G:
```
  print("His name is {0}".format("Arthur"))
```
This is done by using PLACEHOLDERS ```{..}``` and associate each of them with a number that matches the position of the replacing word
There are also format specifications that can be used to personalize the string. For example:
```
.{0:.3f} ca                > prints 3 decimal numbers after the integer part
.{0:<15}|{1:^15}|{2:>15} > alienates the text on left/middle/right by 15 spaces
```
-----
<br><br>
## 3 Tuples
Similar to what other langugages call records (or "struct"), which are informations that belongs to something or someone like a student records.
The tuple chunks together information, without specifying the field name but we can guess.
Btw a tuple it's made of 2 values.

-----
### 3.1 Tuples are like strings
Like strings, tuples are immutables, support all the indexing operators.
Empty tuples looks like this:
```
  my_first_tuple = ()
```
A tuple with just one element specified looks like this:
```
  one_elem_tuple = (5,)
```
Pretty sad hu? We won't use it much.

-----
### 3.2 Packing, unpaking
Declaring:
```
personal_data = ("Bob", "Dalyton", 32, 7, 29, 1979)
```
Packing:
```
(name, surname, age, month, day, year)
```
Unpacking:
```
>>> name
'Bob'
>>> day
7
```

-----
### 3.3 Swap variables
As simple as that:
```
(a, b) = (b, a)
```
Note that first, tuple needs to be "packed".
