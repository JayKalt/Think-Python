# STRINGS
## Useful and nice-to-have methods
-----
<br>
. string.upper()  >  changes all string char from lower to upper<br>
. string.lower()  >  same as lower but viceversa<br>
. string.capitalize()  >  capitalize the first letter<br>
. string.swapcase()  >  revert the case of each char<br>
-----
<br>
. string.split()  >  splits a string of multi words into a list of single words, removing whitespace<br>
-----------------------------------------------------------------------------------------------------<br>
. string.find(target) > find the target in a string<br>
. string.rfind(target) > find the target but reverse (starting from the last position)<br>
-----------------------------------------------------------------------------------------------------<br>
. enumerate(list)  > associates each element to its index<br>
-----------------------------------------------------------------------------------------------------<br>


## Negative indexing
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


## String comparison
We can compare strings and it works as a normal dictionary.
The only thing to really remember is that upper case letteres come first then lowercase letters

## Strings are immutables!
String cannot be chainged unless we create new ones or re-assigne the existing ones

## Optional parameters in methods
Optional parameters are assigned if they find a match between the call and the arguments.
If they don't, it will be assigned a default vaule.
E.G:
```
  def find(haystack, needle, start=0):
    ...
```
In this case, if the call finds a match to the start parameter it will
assign the value, else start will be zero.


## Formatting methods
If we want to format a method we can do it using the ```format``` method:
E.G:
```
  print("His name is {0}".format("Arthur"))
```
This is done by using PLACEHOLDERS which are those {..} within a number
that match the position of the word to be replaced with.

There are also format specifications that can be used to personalize the
string. For example:

  .  {0:.3f} prints 3 decimal numbers after the integer part

  .  "|||{0:<15}|||{1:^15}|||{2:>15}|||Born in {3}|||" this string says
      to allineate the text to the left by 15 spaces
      then to do it in the middle by other 15 spaces
      then on the right by other 15 and finally to print something in the
      end
