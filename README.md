# ivpy
A programming language focusing on hacky syntax at the cost of readability and intuitiveness.

## Syntax

### Print

#### ivpy

```
."Hello, world!";
```

#### Python equivalent

```python
print("Hello, world!")
```

---

### Input

#### ivpy

```
."Enter your name:";
,x;
."Hello, " + x;
```

#### Python equivalent

```python
print("Enter your name:")
x = input()
print("Hello, " + x)
```

---

#### ivpy

```
,x:"Enter your name: ";
.f"Hello, {x}";
```

#### Python equivalent

```python
x = input("Enter your name: ")
print(f"Hello, {x}")
```

---

### If statement

#### ivpy

```
a = 33;
b = 200;

?b > a:
    ."b is greater than a";
?;
```

#### Python equivalent

```python
a = 33
b = 200

if b > a:
    print("b is greater than a")
```

---

#### ivpy

```
a = 33;
b = 33;

?b > a:
    ."b is greater than a";
:?a == b:
    ."a and b are equal";
?;
```

#### Python equivalent

```python
a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
```

---

#### ivpy

```
a = 200;
b = 33;

?b > a:
    ."b is greater than a";
:?a == b:
    ."a and b are equal";
:
    ."a is greater than b";
?;
```

#### Python equivalent

```python
a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
```

---

### While loop

#### ivpy

```
i = 1;

[
    ?i > 5:
        \;
    ?;

    .i;
    +i;
]
```

#### Python equivalent

```python
i = 1

while True:
    if i > 5:
        break

    print(i)
    i += 1
```

---

#### ivpy

```
i = 1;

[
    ?i > 10:
        \;
    ?;

    ?i == 5:
        +i;
        /;
    ?;

    .i;
    +i;
]
```

#### Python equivalent

```python
i = 1

while True:
    if i > 10:
        break

    if i == 5:
        i += 1
        continue

    print(i)
    i += 1
```

---

### Functions

#### ivpy

```
>my_function()
    ."Hello from a function";
<;

my_function();
```

#### Python equivalent

```python
def my_function():
    print("Hello from a function")

my_function()
```

---

#### ivpy

```
>my_function(x)
<5 * x;

.my_function(3);
.my_function(5);
.my_function(9);
```

#### Python equivalent

```python
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
```

---

#### ivpy

```
>myfunction()
    ;
<;
```

#### Python equivalent

```python
def myfunction():
    pass
```

---

### Try except

#### ivpy

```
!:
    .x;
!!:
    ."An exception occurred";
!;
```

#### Python equivalent

```python
try:
    print(x)
except:
    print("An exception occurred")
```

---

#### ivpy

```
!:
    .x;
!!NameError:
    ."Variable x is not defined";
!!:
    ."Something else went wrong";
!;
```

#### Python equivalent

```python
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
```

---

#### ivpy

```
x = -1;

?x < 0:
    !!!Exception("Sorry, no numbers below zero");
?;
```

#### Python equivalent

```python
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")
```

---

### Exit

#### ivpy

```
."Before exit";
!1;
."After exit"; // This line will not be executed
```

#### Python equivalent

```python
print("Before exit")
exit(1)
print("After exit")  # This line will not be executed
```

---

### Assignment operators

#### ivpy

```
+x;
-x;
*x;
/x;
%x;
**x;

+x:5;
-x:5;
*x:5;
/x:5;
%x:5;
**x:5;
```

#### Python equivalent

```python
x += 1
x -= 1
x *= 2
x /= 2
x %= 2
x **= 2

x += 5
x -= 5
x *= 5
x /= 5
x %= 5
x **= 5
```

---

### Import module

#### ivpy

```
$datetime;

x = datetime.datetime.now();
.x;
```

#### Python equivalent

```python
import datetime

x = datetime.datetime.now()
print(x)
```

---

#### ivpy

```
$datetime from datetime as dt;

x = dt.now();
.x;
```

#### Python equivalent

```python
import datetime from datetime as dt

x = dt.now()
print(x)
```

---

### Import ivpy

#### ivpy

*add.ivpy*

```
>add(x, y)
<x + y;
```

*main.ivpy*

```
@add.ivpy;
.add(9, 10);
```

#### Python equivalent

```python
def add(x, y):
    return x + y

print(add(9, 10))
```

---

### Other syntax

#### ivpy

```
x = ++;
x = --;
x = ??;
x = a && b;
x = a || b;
x = !a;
x = a >> b;
```

#### Python equivalent

```python
x = True
x = False
x = None
x = a and b
x = a or b
x = not a
x = a in b
```

### Short syntax examples

#### ivpy

```
a = 200;
b = 33;

?b > a:
    ."b is greater than a";
:?a == b:
    ."a and b are equal";
:
    ."a is greater than b";
?;
```

#### short ivpy

```
a=33;b=33;?b>a:."b is greater than a";:?a == b:."a and b are equal";:."a is greater than b";?;
```

#### Python equivalent

```python
a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
```

---

#### ivpy

```
i = 1;

[
    ?i > 10:
        \;
    ?;

    ?i == 5:
        +i;
        /;
    ?;

    .i;
    +i;
]
```

#### short ivpy

```
i=1;[?i>10:\;?;?i==5:+i;/;?;.i;+i;]
```

#### Python equivalent

```python
i = 1

while True:
    if i > 10:
        break

    if i == 5:
        i += 1
        continue

    print(i)
    i += 1
```