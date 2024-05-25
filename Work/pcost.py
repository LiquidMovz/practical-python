# pcost.py
#
# Exercise 1.27 and 1.30

def portfolio_cost(filename):
    # Open the file and read all lines
    with open(filename, 'rt') as file:
        lines = file.readlines()

    # Initialize a variable to hold the total cost
    total_cost = 0.0

    # Skip the header line (assuming the first line is a header)
    header = lines[0].strip().split(',')

    # Process each line in the file starting from the second line
    for line in lines[1:]:
        # Split the line into parts
        parts = line.strip().split(',')

        # Extract the quantity and price
        symbol = parts[0]
        quantity = int(parts[1])
        price = float(parts[2])

        # Calculate the cost for this line and add to the total cost
        total_cost += quantity * price

    # Return the total cost
    return total_cost

# Example usage:
cost = portfolio_cost('C:/111/GitHub/practical-python/Work/Data/portfolio.csv')
print('Total cost:', cost)
