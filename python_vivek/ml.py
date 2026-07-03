''' 
Machine learning is not magic it is just a geometry problem. 
Some people like to say ML is nothing more than glorified curve-fitting.
* Regression is nothing more than taking bunch of dots and finding a curve that fits nicely to those dots.
* Classification is nothing more than taking a bunch of colored dots and finding the curve that goes between them.

Supervised and supervised : Learn this first
Reinforcement learning
'''
# Tuples are defined by commas, not by parentheses.
'''
Yes. Parentheses () are used to create tuples, but there's one important exception.

1. Multiple values inside () → Tuple
t = (1, 2, 3)

print(type(t))

Output:

<class 'tuple'>
2. Empty parentheses → Empty tuple
t = ()

print(type(t))

Output:

<class 'tuple'>
3. Single element tuple (Common Interview Question)

This is NOT a tuple:

t = (5)

print(type(t))

Output:

<class 'int'>

Why?

Python treats (5) as just the number 5 inside parentheses, similar to how you use parentheses in math.

To create a tuple with one element, you must include a trailing comma:

t = (5,)

print(type(t))

Output:

<class 'tuple'>

The comma creates the tuple, not the parentheses.

4. Parentheses are optional for tuples

These are equivalent:

t1 = (1, 2, 3)
t2 = 1, 2, 3

print(type(t1))
print(type(t2))

Output:

<class 'tuple'>
<class 'tuple'>

Again, it's the commas that define the tuple.

5. Parentheses for grouping expressions

Sometimes () are just used to control the order of evaluation, not to create a tuple.

x = (2 + 3) * 4

print(x)

Output:

20

Here, (2 + 3) is not a tuple.

Summary
Expression	Type	Reason
()	tuple	Empty tuple
(1, 2, 3)	tuple	Multiple values separated by commas
(5,)	tuple	Single-element tuple (comma makes it a tuple)
(5)	int	Just parentheses around an integer
1, 2, 3	tuple	Commas create the tuple
(2 + 3)	int	Parentheses only group the expression
Golden Rule

A common saying among Python developers is:

Tuples are defined by commas, not by parentheses.

The parentheses are often used for readability or to avoid ambiguity, but the comma is what actually makes a tuple.
'''
cars = ['Brezza', 'Swift', 'Baleno', 'Alto', 'WagonR', 'Ertiga', 'Celerio', 'Dzire', 'Vitara Brezza', 'S-Cross']
trending = []
for car in cars:
    if car=='Brezza' or 'Alto':
        print('Trending car is', car)
        trending.append(car)

print(trending, len(trending), len(cars))

 