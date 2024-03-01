try:
    # Some code that may raise an exception
    x = 1 / 0
except ZeroDivisionError as e:
    print("Caught an exception:", e)
