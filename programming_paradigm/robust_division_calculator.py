def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            return "Error: Cannot divide by zero."
        return f"The result of the division is {num / denom}"
    except ValueError:
        return "Error: Please enter numeric values only."


if __name__ == "__main__":
    print(safe_divide(10, 5))  
    print(safe_divide(10, 0))  
    print(safe_divide("ten", 5))  
    print(safe_divide(10, "five"))  
