# RCPY
RCPY is an esotheric programming language that is supposed to read as a recipe. It turned out te be something magical, where you can pass your 3 onions to cook potatos and end up with 100 potatos. This is really your party, but you have to program you own cake baking function... Don't tell your guests you made it with yogurt instead of whipped cream, they won't notice but still. 
How does it do this? 
By butchering the english language ofcourse! 
```
while: potatos < 100; (
    potatos + 1 potatos
)
```
^ this is verry correct syntax
## Current features:
Currently rcpy has the following features.
### literal arithmetic expressions
|Example|Explanation
 | :- | :- 
 | 12| a literal integer
 | onion| a variable
### Binary arithmetic expressions

| Operator        | Example           | Explanation  |
| :------------ |:-------------| :-----|
| +      | ``` onios + 2 ```|adds an arithmetic to the preceding one|
| - | ``` onions - 3```|   subtracts an arithmetic from the preceding one|
| * | ```onions * onions```| multiplies an arithmetic with the preceding one |
|/  | ``` 100 / onions```|divides an arithmetic with the preceding one |
### Relational expressions
|Operator|Example|Explanation|
|:-|:-|:-|
|==|```onions == scallions```|returns true if onions is equal to scallions false otherways
|<|```onions == scallions```|returns true if onions is smaller than scallions false otherways
|>|```onions == scallions```|returns true if onions is greater than scallions false otherways
|<=|```onions == scallions```|returns true if onions is smaller or equal to scallions false otherways
|>=|```onions == scallions```|returns true if onions is greater of equal to scallions false otherways
### Assign statements
Artimethic values can be assigned to variables.
```
2 onions 
3 scallions
```
Above here the value of '2' is assigned to onions and '3' is assigned to scallions. As you can see the assingment operator is not explicitly visible, that is because it is implicid. Also, as you can see assignments are also processed from right to left as opposed from normal languages. This allowes one to do... unconvential things.
```
scallions are better than onions and you cannot change my mind
```
^ This assigns all words in 'are better than onions and you cannot change my mind' to the same value as 'scallions', witch ironicaly disproves the statement
### If statements
As noted previously onions now equal scallions.
```
if: onions equal scallions; (
	onions + scallions onions
)
```
^ Following this onions now equals 6.
> sadly else () is not yet implemented
### While loops
While while loops work. 
```
while: potatos < 100; (
    potatos + 1 potatos
)
```
### Return 
Arthimetics can be returned with two keywords; ```return``` and ```serve```.
### Functions
This language has functions! Functions are declared by telling how to do something, with the keyword 'howto'.
```
howto cook: bread, butter ; (
    butter + bread soup then
    serve soup
)
```
Functions are then called like this:
```
:potatos, onions; cook potatos
```
The parameters are specified left of the function call.
## Fibonachi
Here's a fibonachi example:
```
300 onions
0 potatos

0 scalops
1 lettuce
1 index

1 loop

if: onions < 1; (
    0 loop
)

if: loop ; (
    while: index < onions ; (
        lettuce stash
        lettuce + scalops lettuce
        stash scalops

        index + 1 index
    )
    lettuce potatos
)

serve potatos

```
## Limitations
### Negativity
Negative ingedients don't exist, that would be stupid...
But if you do need them, don't thell anyone I told you this:
```
0 - 5 broccoli
``` 
it will equal -5 broccoli.
### Errors
If shit hits the fan, the interpreter won't help you.

## Comming features
**floats**, don't exist yet
**errors**, will probaply be in the form of a certain scottish chef telling you you are an idiot sandwitch, but wil at least tell where you failed.
**else**, and maybe even else if.
 ## Credits
 Idea  is credited to my brother, Colin.
