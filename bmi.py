# The above class calculates the BMI (Body Mass Index) based on the given height and weight, and
# determines the weight status (low, medium, or overweight) based on the calculated BMI.
class bmi:
    def __init__(self, height=None, weight=None, val=None):
        """
        The function is a constructor that initializes the height, weight, and val attributes of an
        object.
        
        """
        self.height = height
        self.weight = weight
        self.val = val

    def calculate(self):
        """
        The function calculates the body mass index (BMI) using the weight and height values.
        :return: The value of `self.val` is being returned.
        """
        self.val = self.weight / (self.height ** 2)
        return self.val

    def Health(self, val):
        """
        The function determines whether a person's health is underweight, healthy, or overweight based
        on their input value.
        """
        if val < 18.5:
            return "You are Underweight"
        elif val >= 18.5 and val <= 24.9:
            return "You are healthy "
        else:
            return "You are overweight"

        """
        The main function calculates the BMI based on the given height and weight and returns the weight
        status.
        """
        
    @staticmethod
    def main(height, weight):
        bmi_obj = bmi(height=height, weight=weight)
        bmi_val = bmi_obj.calculate()
        weight_status = bmi_obj.Health(bmi_val)
        return weight_status


height = float(input("Please enter the Height in meter"))
weight = int(input("Please enter the Weight in kg"))
weight_status = bmi.main(height, weight)
print(f"Your Bmi Index is ",weight_status)
