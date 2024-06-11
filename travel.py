# Define the travel destinations
destination1 = "Sydney"
destination2 = "Maui"
destination3 = "Barcelona"

# Ask the user where they want to travel
user_destination = input("Where do you want to travel? ")

# Check the user's input and print the corresponding message
if user_destination == destination1:
    print(f"Enjoy your stay in {destination1}!")
elif user_destination == destination2:
    print(f"Enjoy your stay in {destination2}!")
elif user_destination == destination3:
    print(f"Enjoy your stay in {destination3}!")
else:
    print("Oops, that destination is not currently available.")
