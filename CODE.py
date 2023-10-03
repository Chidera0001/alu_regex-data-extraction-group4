import re

# API responses
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

# Extracting RGB Color Values
for response in responses:
    match = re.search(r"rgb\((\d+),\s*(\d+),\s*(\d+)\)", response)
    if match:

# Extracting Event Dates and Times
for response in responses:
    match = re.search(r"(\w{3} \d{2}, \d{4} - \d{2}:\d{2} [APap][Mm])", response)
    if match:
        event_datetime = match.group(0)
        print(f"Event Date/Time: {event_datetime}")
        r = match.group(1)
        g = match.group(2)
        b = match.group(3)
        print(f"RGB Color: ({r}, {g}, {b})")   

# Extracting Social Media Usernames
for response in responses:
    usernames = re.findall(r"@(\w+)", response)
    if usernames:
       print(f"Username: {', '.join(usernames)}")

     # Extracting Product Codes
for response in responses:
    match = re.search(r"([A-Z]{3}\d{3})", response)
    if match:
        product_code = match.group(1)
        print(f"Product Code: {product_code}")

# Extracting Ingredient Lists
for response in responses:
    ingredients = re.findall(r"([^,]+)(?:,\s*([^,]+))*", response)
    if ingredients:
        print(f"Ingredients: {', '.join(ingredients)}")

# Extracting Email Addresses
for response in responses:
    email = re.search(r"([\w.-]+@[\w.-]+)", response)
    if email:
        email_address = email.group(1)
        print(f"Email Address: {email_address}")
