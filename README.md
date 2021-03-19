# Octeract Reformulator

The Reformulator is a tool that automatically generates and manipulates optimisation mathematics. In this repository you can find example files and reformulation snippets that you can use to produce complicated reformulations automatically.

## Community contributions ##

If you have a cool reformulation that you want to share with the world, just create a PR and we'll merge it in.

## Installation ##
1. Download and install [Octeract Engine](www.octeract.com) for your OS.
2. Install Python 3.7+
3. Create a Python file and type `from octeract import *`

That's it! You can now use the Reformulator Python API!

## What you can do ##
The core technology in the Reformulator is what we call Abstract Symbolic Recognition (ASR). This means that you can e.g. say "find all nonlinear terms that look like `log(f(x))`, and do stuff to `f(x)` and/or the original term". You can also use filters to refine the results of the ASR.

## Example ##

Let's say we have a toy model:

```python
from octeract import *

m = Model()

m.maximize("log(x^2)+y^2")
m.set("log(x^3)").to_at_least("y")
```

Printing this (`print(m)`) gives us:

```
Structure : NLP
Convexity : nonconvex
------------------------------------------
var y >= -1.79769e+308, <= 1.79769e+308;
var x >= -1.79769e+308, <= 1.79769e+308;

maximize obj : (y)^(2)+log((x)^(2))+0;

subject to

constraint : log((x)^(3))+-1.0*y+0.0 >= 0;
------------------------------------------
```

If I want to add constraints such that _any_ logarithm with an expression that _might_ take negative values is not allowed to do so, I can simply do:

```python
my_trigger = Match("log(E(fun))")
my_filters = IsMaybeFeasible("fun<=-1.e-12")
my_actions = AddConstraint("con1", "fun>=0")
my_mod = (my_trigger & my_filters).then(my_actions)
m.apply_mod(my_mod)
```

This results in the following model:

```
Structure : NLP
Convexity : nonconvex
------------------------------------------
var y >= -1.79769e+308, <= 1.79769e+308;
var x >= -1.79769e+308, <= 1.79769e+308;

maximize obj : (y)^(2)+log((x)^(2))+0;

subject to

constraint : log((x)^(3))+-1.0*y+0.0 >= 0;
con1_0 : (x)^(3)+0.0 >= 0;
------------------------------------------
```

where the reformulator only added a constraint to ensure that `x^3>=0` because of `log(x^3)`, while it ignored `log(x^2)` because we told it to.

## Syntax ##

### Symbolic recognition ###

Symbolic recognition is triggered through the `Match()` command, and its input is a string. Keep in mind that this works term-wise, i.e. the Reformulator will go through all terms in your problem and try to match this pattern.

All symbolic recognition is processed through strings, which have three keywords:
```python
V("some_handle")
```
this matches a single variable, e.g.: `trigger = Match("V(handle1)*V(handle2)"))`
```python
E("some_handle")
```
this matches an arbitrary expression, e.g.: `trigger = Match("log(E(x))")`
```python
C("some_handle")
```
this matches a constant, e.g.: `trigger = Match("C(n)*log(E(x))*V(y)")`

These can be combined fluidly to fine-tune the matching you want to do. For instance, this last command,  `trigger = Match("C(n)*log(E(x))*V(y)")`, will match `log(x^2+3*y)*w`, as well as `3*log(sin(w^2)/(3*x))*y`, but it will not match `3*log(sin(w^2)/(3*x))`, since it's missing the pattern of constant-times-log-time-variable. 

### Handles ###

Each time you define a matching pattern, you must define a handle for the result of the match. This handle is used for future manipulations, and the name of the handle is in no way related to the math in your problem. For instance, I can say: `trigger = Match("C(n)*log(V(x))")`, and this can match `log(y)`. Once this is matched, I can use `x` to refer to `y` in all my reformulator commands _that are part of the same rule_. Because the scope of this name is the rule itself, it means you can re-use the same building block for in other rules and you'll get no conflicts.

Keep in mind that this is the reformulator doing all the heavy lifting for you. All you need to know is that any term that matches your pattern can be abstractly manipulated using the handle. The manipulation will be applied in exactly the same way by the Reformulator for all different terms, and the Reformulator will automatically figure out the right names for everything and produce consistent math.

### Order ###

ASR is invariant to order of expressions, so `3*log(sin(w^2)/(3*x))*y` is equivalent to `y*log(sin(w^2)/(3*x))*3`.
