# References for Day 2
## Variables and user input
In programming a **varable** is a place in memory to hold a value.  For example:

```
name = "Chad"
distance = 100
```

This creates a variable named `name` and a variable named `distance`.  These variable can then be used just as the value would.  For example:
```
t = turtle.Pen()  
t.forward(distance)
```

## User input
Variables can be assigned values within our program like above or they can be assigned values from user input.  
```
name = input("What is your name")
```
However, if we want to read a number from user input we need to tell the computer to treat it as a number.  Using `int( )` says it is an integer, `float( )` says it is a decimal number.
```
number = int( input("How many? ") )
distance = float( input("How far? ") )
```


## Printing output
The ***print*** statement lets you output to the command line:

```
print("How are you today?")
```
Outputs:  
*How are you today?*

It can also be used with placeholders for variables you want to output in a string.  If there are multiple placeholders you put their replacements in parentheses:

```
name = "Chad"
print("Hello %s", name)
weather = "sunny"
print("%s the weather today is %s." % (name, weather))
```
Outputs:  
*Hello Chad*  
*Chad the weather today is sunny*


# Python conditions
## Otherwise known as ***if statements***

## Condition statements

```
<   less than (ex. age < 10)
>   greater than (ex. items > 5)
<=  less than or equal (ex. quantity <= 3)
>=  greater than or equal (ex. quantity >= 3)
==  equal - make sure to note it is TWO equal signs (ex. age == 10)
```


### Simple conditional  
```
name = "Chad"
if name == "Chad":  
  print("Chad is awesome!")  
else:  
  print("Not everybody can be a Chad")
```

### ***elif***  Else if
```
if food == "pizza":
  print("Great!")
elif food == "candy":
  print("sweets!")
else:
  print("Oh ok, I'm hungry that will work")
```

### Compound conditional
Combines two comparisons: and, or

```
if temperature < 5 or temperature > 100:
  print("It is uncomfortable!")

if month == "July" and day == 4:
  print("Happy 4th of July")
```

## Adding some randomness ##
Random numbers/values
```
import random
dice = random.randint(1,7)
list = ['apple','orange','banana']
random.shuffle(list)
```
Or a random decimal from 0 to 1
> number = random.random()

Find more info here:
https://docs.python.org/2/library/random.html

# Loops #
Two kinds of loops:


## Repeat a specified number of times (***for loop***): ##
```
for i in range(0,4):
  t.forward(100)  
  t.left(90)

```

## Repeat while some condition still holds ##
```
response = input("Are you done? ")
while response != "yes":
  response = input("Are you done now? ")
print("Finally!")
```

Or repeat forever
```
while True:
  print("I want my $2!")
```
