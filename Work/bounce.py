# bounce.py
#
# Exercise 1.5

# Initial height from which the ball is dropped
initial_height = 100

# The bounce factor (fraction of the height to which the ball bounces back)
bounce_factor = 3 / 5

# Number of bounces to calculate
num_bounces = 10

# Print the table header
print(f"{'Bounce':>6} | {'Height':>10}")
print("-" * 20)

# Calculate and print the height of each bounce
for bounce in range(1, num_bounces + 1):
    # Update the height to the new height after the bounce
    initial_height *= bounce_factor
    
    # Print the current bounce number and the height after the bounce
    print(f"{bounce:>6} | {initial_height:>10.2f}")

