import re

text = "My email is sai123@gmail.com and my phone number is 9876543210"

if re.match(r"My", text):
    print("Match found at beginning")

phone = re.search(r"\d{10}", text)
print("Phone:", phone.group())

email = re.findall(r"\w+@\w+\.\w+", text)
print("Email:", email)

print("Replaced:", re.sub(r"\d", "X", text))
