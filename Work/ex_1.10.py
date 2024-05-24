# mortgage2.py
# Exercise 1.10: Making a table

# Step 1: Initialize Fixed Variables
principal = 500000.0  # Initial principal amount of the mortgage
rate = 0.05           # Annual interest rate (5%)
payment = 2684.11     # Regular monthly payment amount

# Step 2: Get User Input for Extra Payment Details
extra_payment_start_month = int(input("Enter the start month for extra payments: "))
extra_payment_end_month = int(input("Enter the end month for extra payments: "))
extra_payment = float(input("Enter the extra monthly payment amount: "))

# Step 3: Initialize Variables for Total Paid and Months
total_paid = 0.0  # Total amount paid over the life of the mortgage
months = 0        # Number of months required to pay off the mortgage

# Step 4: Print Table Header
print(f"{'Month':<10}{'Monthly Payment':<20}{'Total Paid':<20}{'Remaining Principal':<20}")

# Step 5: Create the Loop to Calculate the Mortgage
while principal > 0:
    if extra_payment_start_month <= months < extra_payment_end_month:
        # If within the extra payment period
        total_payment = payment + extra_payment
    else:
        # If outside the extra payment period
        total_payment = payment

    principal = principal * (1 + rate / 12) - total_payment
    total_paid = total_paid + total_payment
    
    # Print the month, monthly payment, total paid so far, and remaining principal
    print(f"{months:<10}{total_payment:<20.2f}{total_paid:<20.2f}{principal:<20.2f}")
    
    # Increment the month counter
    months += 1

# Step 6: Print the Results
print('Total paid:', total_paid)
print('Months:', months)
