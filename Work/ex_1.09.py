# mortgage.py
# Exercise 1.8: Extra payments

# mortgage.py# mortgage.py

# Fixed mortgage details
principal = 500000.0
rate = 0.05
payment = 2684.11

# Get user inputs for extra payment details
extra_payment_start_month = int(input("Enter the start month for extra payments: "))
extra_payment_end_month = int(input("Enter the end month for extra payments: "))
extra_payment = float(input("Enter the extra monthly payment amount: "))

# Total amount paid over the life of the mortgage
total_paid = 0.0

# Number of months required to pay off the mortgage
months = 0

# Loop until the principal is paid off
while principal > 0:
    # Check if the current month is within the extra payment period
    if extra_payment_start_month <= months < extra_payment_end_month:
        principal = principal * (1 + rate / 12) - (payment + extra_payment)
        total_paid = total_paid + (payment + extra_payment)
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
    
    # Increment the month counter
    months += 1

# Print the total amount paid
print('Total paid:', total_paid)

# Print the number of months required
print('Months:', months)


# Fixed mortgage details
principal = 500000.0
rate = 0.05
payment = 2684.11

# Get user inputs for extra payment details
extra_payment_start_month = int(input("Enter the start month for extra payments: "))
extra_payment_end_month = int(input("Enter the end month for extra payments: "))
extra_payment = float(input("Enter the extra monthly payment amount: "))

# Total amount paid over the life of the mortgage
total_paid = 0.0

# Number of months required to pay off the mortgage
months = 0

# Loop until the principal is paid off
while principal > 0:
    # Check if the current month is within the extra payment period
    if extra_payment_start_month <= months < extra_payment_end_month:
        principal = principal * (1 + rate / 12) - (payment + extra_payment)
        total_paid = total_paid + (payment + extra_payment)
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
    
    # Increment the month counter
    months += 1

# Print the total amount paid
print('Total paid:', total_paid)

# Print the number of months required
print('Months:', months)
