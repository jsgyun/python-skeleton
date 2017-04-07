#!/usr/bin/python3.6
"""TEMPLATE Module Docstring

Say something about what TEMPLATE is for. Docstring line limit 72. -->|
"""

### IMPORTS ###################################################################
import sys


### SOMETHING ELSE ############################################################
def main():
    """
    My Example function prints and returns 'Hello, world'

    Arguments:
        - None

    Returns
        - 'Hello, world'

    Examples / Tests
        >>> main()
    """
    greeting = "Hello, world"
    print(greeting)
    print(sys.version)
    return greeting


### EOC #######################################################################
if __name__ == "__main__":
    main()