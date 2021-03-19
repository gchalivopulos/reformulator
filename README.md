# Octeract Reformulator

The Reformulator is a tool that automatically generates and manipulates optimisation mathematics. In this repository you can find example files and reformulation snippets that you can use to produce complicated reformulations automatically.

# Community contributions

If you have a cool reformulation that you want to share with the world, just create a PR and we'll merge it in.

# Installation
1. Download and install [Octeract Engine](www.octeract.com) for your OS.
2. Install Python 3.7+
3. Create a Python file and type `from octeract import *`

That's it! You can now use the Reformulator Python API!

# What you can do
The core technology in the Reformulator is what we call Abstract Symbolic Recognition (ASR). This means that you can e.g. say "find all nonlinear terms that look like `log(f(x))`, and do stuff to `f(x)` and/or the original term". You can also use filters to refine the results of the ASR.

# Example

Let's say we have a toy model:

```
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

```
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
