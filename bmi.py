class bmi:
    def __init__(self, height=None, weight=None, val=None):
        self.height = height
        self.weight = weight
        self.val = val

    def calculate(self):
        self.val = self.weight / (self.height ** 2)
        return self.val

    def Health(self, val):
        if val <= 15:
            return "low"
        elif val >= 15 and val <= 30:
            return "medium"
        else:
            return "overweight"

    @staticmethod
    def main(height, weight):
        bmi_obj = bmi(height=height, weight=weight)
        bmi_val = bmi_obj.calculate()
        weight_status = bmi_obj.Health(bmi_val)
        return weight_status

# Example usage:
height = float(input("Please enter the Height in meter"))
weight = int(input("Please enter the Weight in kg"))
weight_status = bmi.main(height, weight)
print(f"Your Bmi Index is ",weight_status)