from temperature import Temperature

class Calorie:
    """
    Calculates the amount of calories a person needs based
    on this formula:
    BMR = 10*weight + 6.25*height - 5*age + 5 - 10*temperature
    """
    def __init__(self, height, weight, age, temperature):
        self.height = height
        self.weight = weight
        self.age = age
        self.temperature = temperature

    def calc(self):
        bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5 - 10 * self.temperature
        return bmr


if __name__ == "__main__":
    temperature = float(Temperature(country='italy', city='rome').get())
    calorie = Calorie(temperature=temperature, weight=70, height=175, age=32)
    print(calorie.calc())
