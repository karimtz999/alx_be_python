from bank_account import BankAccount

def main():
    # Create a BankAccount object with an initial balance
    account = BankAccount(250.0)

    # Display the balance
    balance_output = account.display_balance()

    # Check if the output matches the expected format
    expected_output = "Current Balance: $250.00"
    if balance_output == expected_output:
        print("Output matches expected format:")
        print(balance_output)
    else:
        print("Output does not match expected format.")
        print(f"Expected: {expected_output}")
        print(f"Got: {balance_output}")

if __name__ == "__main__":
    main()
