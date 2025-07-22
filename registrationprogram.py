import os
import json
import random
import re
import sys
import calendar
import time
from datetime import datetime

print("=== Welcome to User Registration System ===")

# Step 1: Input name and email
name = input("Enter your name: ")
email = input("Enter your email: ")

# Step 2: Validate email using regex
if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("❌ Invalid email format!")
    sys.exit()

# Step 3: Take birth year & calculate age
birth_year = int(input("Enter your birth year (YYYY): "))
current_year = datetime.now().year
age = current_year - birth_year

# Step 4: Check if birth year is leap year
is_leap = calendar.isleap(birth_year)

# Step 5: OTP Verification
otp = random.randint(1000, 9999)
print(f"Your OTP is: {otp}")
time.sleep(1)
user_otp = int(input("Enter OTP: "))

if user_otp != otp:
    print("❌ Incorrect OTP. Exiting...")
    sys.exit()

# Step 6: Prepare data
user_data = {
    "name": name,
    "email": email,
    "age": age,
}