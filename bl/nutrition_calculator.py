
class NutritionCalculator:
    def __init__(self, patient, carbohydrate_percentage, protein_percentage, fat_percentage):
        self.patient = patient
        self.carbohydrate_percentage = carbohydrate_percentage
        self.protein_percentage = protein_percentage
        self.fat_percentage = fat_percentage

    def calorie_needed(self):
        if self.patient.gender == 'male':
            BEE = (10* self.patient.weight) + (6.25* self.patient.height)-(5* self.patient.age)+5
            TEE = BEE * 1.3 * 1.1
            restricted_TEE = TEE - 500
            return restricted_TEE
        else:
            BEE = (10 * self.patient.weight) + (6.25 * self.patient.height)-(5 * self.patient.age)-161
            TEE = BEE * 1.3 * 1.1
            restricted_TEE = TEE - 500
            return restricted_TEE

    def carbohydrate_needed(self):
        carbohydrate_needed = (self.carbohydrate_percentage * self.calorie_needed())/ 4
        return carbohydrate_needed

    def protein_needed(self):
        protein_needed = (self.protein_percentage * self.calorie_needed())/4
        return protein_needed

    def fat_needed(self):
        fat_needed = (self.fat_percentage * self.calorie_needed())/9
        return fat_needed
