# Smart Home Device Tracker
# You’re building a Smart Home Device Tracker to monitor the status of electronic devices.

# Your Tasks:
# 1. Create a class called SmartDevice.
# 2. Add a class attribute brand = "HomeTech" (default manufacturer).
# 3. In the constructor, accept:
#   - device_name: Name of the smart device.
#   - power_status: True (ON) or False (OFF).
# 4. Shadow the class attribute brand by assigning self.brand = "CustomBrand" (to simulate user modification).
# 5. Define a method get_status():
# 6. Returns a string like: "AC is ON - CustomBrand" or "Fan is OFF - CustomBrand" based on power_status.

class SmartDevice:
    brand = "HomeTech"
    def __init__(self, device_name, power_status):
        self.device_name = device_name
        self.power_status = power_status
        self.brand = "CustomBrand"
    
    def get_status(self):
        state = "ON" if self.power_status else "OFF"
        return f"{self.device_name} is {state} - {self.brand}"
    
# Example usage:
device1 = SmartDevice("AC", True)
device2 = SmartDevice("Fan", False)
print(device1.get_status())  # Output: "AC is ON - CustomBrand"
print(device2.get_status())  # Output: "Fan is OFF - CustomBrand"
