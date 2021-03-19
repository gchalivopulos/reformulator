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
