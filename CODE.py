import re

# Example API responses
responses = [
    "Restaurant Name - Cuisine Type",
    "ingredient1, ingredient2, ingredient3",
    "rgb(255, 255, 255)",
    "Check out my profile @username",
    "Here's a product code: ABC123",
    "Headline: Subheader",
    "Oct 15, 2023 - 08:30 AM",
    "Contact us at email@example.com",
]

# Extracting Restaurant Names and Cuisine Types
for response in responses:
    match = re.search(r"([\w\s]+) - ([\w\s]+)", response)
    if match:
        restaurant_name = match.group(1)
        cuisine_type = match.group(2)
        print(f"Restaurant Name: {restaurant_name}, Cuisine Type: {cuisine_type}")

# Extracting Event Dates and Times
for response in responses:
    match = re.search(r"(\w{3} \d{2}, \d{4} - \d{2}:\d{2} [APap][Mm])", response)
    if match:
        event_datetime = match.group(0)
        print(f"Event Date/Time: {event_datetime}")
        
