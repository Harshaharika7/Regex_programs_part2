import re

data = """
+1 123-456-7890
+44 20 7946 0958
+91 63741 56280
"""

pattern = re.compile(r'\+(\d+)\s(\d+[-\s]+\d+)')

matches = pattern.findall(data)

for match in matches:
    country_code, mobile_number = match
    print(f"Country Code: {country_code}, Mobile Number: {mobile_number}")
