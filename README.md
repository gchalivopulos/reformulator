# Octeract Reformulator

The Reformulator is a tool that automatically generates and manipulates optimisation mathematics. In this repository you can find example files and reformulation snippets that you can use to produce complicated reformulations automatically.

# Installation
1. Download and install [Octeract Engine](www.octeract.com) for your OS.
2. Install Python 3.7+
3. Create a Python file and type `from octeract import *`

That's it! You can now use the Reformulator Python API!

# What you can do
The core technology in the Reformulator is what we call Abstract Symbolic Recognition (ASR). This means that you can e.g. say "find all nonlinear terms that look like `log(f(x))`, and do stuff to `f(x)` and/or the original term". You can also use filters to refine the results of the ASR.
