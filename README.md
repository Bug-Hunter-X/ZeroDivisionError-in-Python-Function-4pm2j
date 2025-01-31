# ZeroDivisionError in Python Function

This repository demonstrates a common error in Python: the `ZeroDivisionError`. The error occurs when attempting to divide a number by zero, which is mathematically undefined.

## Bug Description
The Python function `function` takes two arguments, `a` and `b`, and returns the result of `a / b`. If `b` is zero, this causes a `ZeroDivisionError`. The bug is demonstrated in the `bug.py` file.

## Solution
The `bugSolution.py` file shows how to handle this error gracefully using a `try-except` block. The `try` block attempts the division, and the `except` block catches the `ZeroDivisionError` and prints a user-friendly message.  Alternatively, input validation can prevent the error altogether.