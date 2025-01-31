def function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None  # Or handle the error in a more appropriate way

result = function(10, 0) #Output Error: Cannot divide by zero.
result2 = function(10,2) # Output 5.0