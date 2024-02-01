def calculate_tip(amount, tip_percentage):
    tip = amount * (tip_percentage / 100)
    return tip

def main():
    bill_amount = float(input("Enter the bill amount: $"))
    tip_percentage = float(input("Enter the tip percentage you want to leave: "))

    calculated_tip = calculate_tip(bill_amount, tip_percentage)

    print(f"\nBill amount: ${bill_amount}")
    print(f"Tip percentage: {tip_percentage}%")
    print(f"Calculated tip: ${calculated_tip:.2f}")

    total = bill_amount + calculated_tip
    print(f"Total to pay: ${total:.2f}")

main()
