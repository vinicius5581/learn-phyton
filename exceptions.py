while True:
    try:
        x = int(input("Amount"))
        break
    except ValueError:
        print("Enter valid number")

try:
    x = int(input("amount:"))
except ValueError:
    print("value")
except (RuntimeError, TypeError):
    print("other")