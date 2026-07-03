'''
Unlike JavaScript, Python does not have a === operator.

If you try to use it:

a = 5
b = 5

print(a === b)

You'll get:

SyntaxError: invalid syntax
== : Equality operator

== checks whether two values are equal.

a = 10
b = 10

print(a == b)

Output:

True

Another example:

print([1, 2] == [1, 2])

Output:

True

Even though these are two different list objects, their contents are the same.

is : Identity operator

Python uses is instead of JavaScript's === for a different purpose.

is checks whether both variables refer to the exact same object in memory.

a = [1, 2]
b = [1, 2]

print(a == b)
print(a is b)

Output:

True
False

Explanation:

== → The values are equal.
is → They are different list objects stored at different memory locations.
Example where is is True
a = [1, 2]
b = a

print(a == b)
print(a is b)

Output:

True
True

Both variables point to the same list.

a ───► [1, 2] ◄─── b
JavaScript vs Python
JavaScript	Python	Meaning
==	==	Compare values (JavaScript may perform type coercion; Python does not.)
===	No equivalent	JavaScript compares value and type without coercion.
Object reference (obj1 === obj2)	is	Check whether both variables reference the same object.
Type coercion difference
JavaScript
5 == "5"

Output:

true

Because JavaScript converts "5" to the number 5.

With strict equality:

5 === "5"

Output:

false
Python

Python does not perform this kind of automatic type coercion with ==.

5 == "5"

Output:

False

Since Python already compares values without converting between unrelated types, there is no need for a separate === operator.

When should you use is?

Use is when checking for singleton objects, especially None.

if value is None:
    print("No value")

Instead of:

if value == None:   # Works, but not recommended
    print("No value")

is None is the Pythonic and recommended style because there is only one None object.

Summary
== → Compares values.
is → Compares object identity (same object in memory).
=== → Does not exist in Python.
Python's == is already "strict" in the sense that it does not perform JavaScript-style type coercion.
'''
name = 'vivek'
name2 = 'vivek'
print(name is name2)  # True, because both refer to the same string object in memory because of string interning.
print(name==name2)  # True, because their values are equal because they are the same string.
'''
String interning is an optimization where Python stores only one copy of identical immutable strings in memory and reuses it whenever possible.

Instead of creating multiple objects with the same value:

a = "hello"
b = "hello"

Python may store only one "hello" object, and both a and b point to it.

       ┌─────────┐
a ───► │ "hello" │ ◄─── b
       └─────────┘

This saves memory and can make comparisons faster.

is vs ==

Remember this difference:

a = "python"
b = "python"

print(a == b)   # True (values are equal)
print(a is b)   # True (same object, usually because of interning)
== → compares values
is → compares object identity (memory)
'''


'''
== → Do these two objects have the same value?
is → Are these two names pointing to the exact same object in memory?
JavaScript equivalent

Python's is is very similar to JavaScript's === for objects, not for primitives.

const a = { name: "Vivek" };
const b = { name: "Vivek" };

a === b // false

because they are different objects.

Python:

a = {"name": "Vivek"}
b = {"name": "Vivek"}

print(a == b)   # True
print(a is b)   # False

Why?

Memory

a ─────► {"name":"Vivek"}   (Object #1)

b ─────► {"name":"Vivek"}   (Object #2)

The values are equal.

But they're different objects.

Example 1 (Different result)
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

Output

True
False

because

a ----> [1,2,3]

b ----> [1,2,3]

Two separate lists.

Example 2 (Same object)
a = [1, 2, 3]
b = a

print(a == b)
print(a is b)

Output

True
True
      [1,2,3]
        ▲
        │
   a ───┘
   b ───┘

Both variables point to exactly the same object.

Example 3 (Integers)

This surprises everyone.

a = 100
b = 100

print(a == b)
print(a is b)

Often outputs

True
True

Why?

Python interns many small integers, so both variables point to the same object.

       100
      ▲   ▲
      │   │
      a   b
But...
a = 1000
b = 1000

print(a == b)
print(a is b)

You might expect

True
False

However, don't rely on this. Depending on the Python implementation and execution context, a is b may be either True or False. The language does not guarantee object identity for integers created this way.

This is why you should never use is to compare numbers.

Example 4 (Strings)
a = "hello"
b = "hello"

print(a == b)
print(a is b)

Often

True
True

because Python interns many string literals.

But again, don't rely on it.

Example 5 (Constructed strings)
a = "hello world"
b = "".join(["hello", " ", "world"])

print(a == b)
print(a is b)

Output

True
False

The values match, but they are different string objects.

When should you use is?

Almost exclusively when comparing with singletons.

The most common example is None.

✅ Correct

name = None

if name is None:
    print("No name")

❌ Don't write

if name == None:

because None is a singleton object in Python.

The same applies to True and False in identity checks, though for boolean values you'll usually just write:

if flag:

instead of

if flag is True:
Summary
Situation	==	is
Same values, different objects	✅ True	❌ False
Same object	✅ True	✅ True
Lists with same contents	✅ True	❌ False
Dictionaries with same contents	✅ True	❌ False
None	Avoid	✅ Use is None
Numbers	✅ Use ==	❌ Don't use is
Strings	✅ Use ==	❌ Don't use is
Rule of thumb
Use == for almost all comparisons.
Use is only when you want to know whether two variables refer to the same object, or when checking against singleton objects like None.

This distinction is one of the most common Python interview topics because it tests your understanding of object identity vs. value equality.
'''


