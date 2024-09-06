
# import to use json file 
import json

# Load the JSON data from the given file
file_path = "/home/dell/Downloads/Python-task.json" 
# open and read the file  
with open(file_path, 'r') as file:
    data = json.load(file)

# Get the main hotel info
hotel_info = data['assignment_results'][0]

# Prices shown to the user
room_prices = hotel_info['shown_price']  

# Actual prices without taxes
net_prices = hotel_info['net_price']  

# Taxes are in JSON string format
tax_info = json.loads(hotel_info['ext_data']['taxes'])  

 # Total guests
guests = hotel_info['number_of_guests'] 

# Function to find the cheapest room (without using min())
def get_cheapest_room(prices):
    cheapest_room = None
    lowest_price = float('inf')  # Set an initial high price to compare
    for room, price in prices.items():
        price = float(price)
        if price < lowest_price:
            lowest_price = price
            cheapest_room = room
    return cheapest_room, lowest_price

# Find the cheapest room and price
cheapest_room, cheapest_price = get_cheapest_room(room_prices)

# Calculate the total price for each room (net price + taxes)
total_price_by_room = {}
total_taxes = sum(float(val) for val in tax_info.values())  # Sum of all taxes

for room, net_price in net_prices.items():
    total_price = float(net_price) + total_taxes  # Total price for each room
    total_price_by_room[room] = total_price

# Write the results to a file
output_file = 'hotel_prices_output.txt'
with open(output_file, 'w') as file:
    file.write(f"Cheapest Room: {cheapest_room}\n")
    file.write(f"Cheapest Price: ${cheapest_price}\n")
    file.write(f"Number of Guests: {guests}\n\n")
    file.write("Total Prices (Net Price + Taxes) for all rooms:\n")
    for room, total_price in total_price_by_room.items():
        file.write(f"{room}: ${total_price:.2f}\n")

# Print confirmation message
print(f"Results saved to {output_file}")
