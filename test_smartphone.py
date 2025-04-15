from smartphone import Smartphone, SmartphoneWithFeatures

# Create a basic smartphone
basic_phone = Smartphone("Nokia", "3310", 50)
print(basic_phone.get_details())  # Output: Brand: Nokia, Model: 3310, Price: $50

# Create a smartphone with additional features
premium_phone = SmartphoneWithFeatures("Apple", "iPhone 14 Pro", 1200, 20, 48)
print(premium_phone.get_details())  # Output: Brand: Apple, Model: iPhone 14 Pro, Price: $1200, Battery Life: 20 hours, Camera: 48 MP

# Check if the premium phone is considered premium
print(premium_phone.is_premium())  # Output: True