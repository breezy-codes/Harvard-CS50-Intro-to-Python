# Lecture 4
# Program task number 4
# Using funny libraries

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])