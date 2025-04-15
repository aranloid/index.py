class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def get_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}"

    def set_price(self, new_price):
        self.price = new_price


# Subclass with additional features
class SmartphoneWithFeatures(Smartphone):
    def __init__(self, brand, model, price, battery_life, camera_quality):
        # Call the parent class constructor
        super().__init__(brand, model, price)
        self.battery_life = battery_life  # in hours
        self.camera_quality = camera_quality  # in megapixels

    def get_details(self):
        # Override the parent method to include additional details
        base_details = super().get_details()
        return f"{base_details}, Battery Life: {self.battery_life} hours, Camera: {self.camera_quality} MP"

    def is_premium(self):
        # Determine if the smartphone is premium based on price and features
        return self.price > 1000 and self.camera_quality > 12