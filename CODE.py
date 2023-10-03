import re

# Sample input string containing various data types
input_string = """
Restaurant ABC - Italian, Restaurant XYZ - Mexican, Restaurant DEF - Chinese
Ingredients: ingredient1, ingredient2, ingredient3, ingredient4
This is an RGB color: rgb(255, 0, 128)
Check out my profile: @username123 on Twitter
Product Codes: ABC123, XYZ456, DEF789
News Headlines: Breaking News: Important Update
Event Date: Sep 30, 2023 - 02:30 PM
Email Address: sample.email@example.com
"""

# Regular expressions for data extraction
restaurant_pattern = r"([A-Za-z\s]+) - ([A-Za-z\s]+)"
ingredient_pattern = r"Ingredients:\s*(.*)"
rgb_pattern = r"rgb\((\d+),\s*(\d+),\s*(\d+)\)"
username_pattern = r"@\w+"
product_code_pattern = r"[A-Z]{3}\d{3}"
news_headline_pattern = r"([^:]+):\s*(.*)"
event_datetime_pattern = r"(\w+\s\d{2},\s\d{4}) - (\d{2}:\d{2}\s[APap][Mm])"
email_pattern = r"[\w\.-]+@[\w\.-]+"

# Extract restaurant names and cuisines
restaurant_matches = re.findall(restaurant_pattern, input_string)
for match in restaurant_matches:
    restaurant_name, cuisine = match
    print("Restaurant Name: {}, Cuisine: {}".format(restaurant_name, cuisine))

# Extract ingredient lists
ingredient_matches = re.search(ingredient_pattern, input_string)
if ingredient_matches:
    ingredients = ingredient_matches.group(1).split(', ')
    print("Ingredients:", ', '.join(ingredients))

# Extract RGB color values
rgb_matches = re.search(rgb_pattern, input_string)
if rgb_matches:
    red, green, blue = rgb_matches.groups()
    print("Red: {}, Green: {}, Blue: {}".format(red, green, blue))

# Extract social media usernames
username_matches = re.findall(username_pattern, input_string)
print("Usernames:", ', '.join(username_matches))

# Extract product codes
product_code_matches = re.findall(product_code_pattern, input_string)
print("Product Codes:", ', '.join(product_code_matches))

# Extract news headlines
news_headline_matches = re.findall(news_headline_pattern, input_string)
for match in news_headline_matches:
    headline, subheader = match
    print("Headline: {}, Subheader: {}".format(headline, subheader))

# Extract event dates and times
event_datetime_matches = re.search(event_datetime_pattern, input_string)
if event_datetime_matches:
    event_date, event_time = event_datetime_matches.groups()
    print("Event Date: {}, Event Time: {}".format(event_date, event_time))

# Extract email addresses
email_matches = re.findall(email_pattern, input_string)
print("Email Addresses:", ', '.join(email_matches))
