# CHAPTER 5, DATA TYPES
## 1. Summary of nice-to-have methods and functions
### METHODS
#### For letter case
```
. string.upper()          >  changes all string char from lower to upper
. string.lower()          >  same as lower but viceversa
. string.capitalize()     >  capitalize the first letter
. string.swapcase()       >  revert the case of each char
```
#### Convert string to list
```
. string.split(separator)          >  splits a string of multi words into a list of single words, removing whitespace or the argument
. join.splitted-string(glue)       >  does the opposite of 
```
#### Find char in a string
```
. string.find(target)     > find the target in a string
. string.rfind(target)    > find the target but reverse (starting from the last position)
```
#### List methods
```
. list.appeand(value)     > adds the argument passed to it to the end of the list
. list.insert(val, pos)   > adds the first argument (a value), in a specific position (second argument)
. list.count(value)       > counts how many times the argument is in the list
. list.extend(list)       > concatenates the argument to the original list
. list.index(i)           > shows the values at the index i
. list.reverse()          > reverses the list
. list.sort()             > sorts the list from the lowest to the greatest
. list.remove(value)      > remove the first item that matches the argument
```
### FUNCTIONS
```
. enumerate(sequence)     > associates each element to its index
. len(sequence)           > gives the lenght of a sequence
```
### OPERATIONS
```
. in/not in               > boolean values to evaluates an item it's in a sequence
. a = a + b               > concatenates lists
. a = a * n               > repeats the list n times
. a[i:j]                  > slice operator (any expression that evaluates to an integer)
. a[i]                    > indexing operator
. a[i:j] = [...]          > modifying elements in a list 
. a[i:i] = [...]          > squeezing elements into a list
. a[i:j] = []             > removing elements from a list (watch out, error prone)
. del a[i/i:j]            > better to use to remove something from a list
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

### 2.2 String comparison
We can compare strings and it works as a normal dictionary.
The only thing to really remember is that upper case letteres come first then lowercase letters

### 2.3 Strings are immutables!
String cannot be chainged unless we create new ones or re-assigne the existing ones

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

### 3.2 Packing, unpaking
Declaring:
```
personal_data = ("Bob", "Dalyton", 32, 7, 29, 1979)
```
Packing:
```
(name, surname, age, month, day, year) = personal_data
```
Unpacking:
```
>>> name
'Bob'
>>> day
7
```

### 3.3 Swap variables
As simple as that:
```
(a, b) = (b, a)
```
Note that first, tuple needs to be "packed".

-----
<br><br>

## 4. Data types and memory management:
### 4.1 Python is heterogeneous
That means that something (a list, a tuple, or anything else) can be composed of elements of different types.
### 4.2 Data types
```
Syntax                  Name        Type            Category            Mutability        Memory management
------------------------------------------------------------------------------------------------------------
a = (2, 4, ...)         Tuple       Tuple           Sequences           Immutable         Non optimized
b = (2, 4)              Pair        Tuple           Sequences           Immutable         Non optimized
c = ['a', 9, ...]       List        List            Sequences           Mutable           Non optimized
d = "Hello World"       String      String          Sequences           Immutable         Optimized
```
### 4.3 Alias and clones
If we assign a variable to another we create an alias which is another name that referes to that specific item:
```
>>> money = [(100, 1), (50, 3), (20, 19), (10, 2), (5, 0)]
>>> happines = money
>>> money is happines
True
```
It will cause any changes to affect all the alias associated with that specific item.<br><br>
But what if we want to clone a list, to keep a copy of the original item?
Well, the easiest way to do that it's by using the slice operator:
```
>>> a = [1, 2, 3]
>>> b = a[:]
>>> b
[1, 2, 3]
```
It's so importat to remember that functions creates an alias, not a copy or a clone.<br>
That means if we modify the list in the _function_, the changes gonna be recorded back in the __main__.<br>
Those function are knonw as "modifiers" (and not "pure functions"), and the changes are known as "side effects".<br>
### 5. Nested lists aka Matrices
A nested list, or a matrix, looks like this:
```
list = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
list[1][2]
>>> 5
```

