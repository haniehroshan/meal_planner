from controller.exceptions import UserNotFoundException
from model.database.patient_da import PatientDa
from model.entity.patient import Patient


class PatientController:
    patient_da = PatientDa()

    @classmethod
    def save(cls, patient_id, weight, height, age, gender):
        try:
            patient = Patient(patient_id, weight, height, age, gender)
            cls. patient_da.save(patient)
            return True, f"Patient {patient_id} Saved"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls,weight, height, age, gender):
        try:
            patient = Patient(weight, height, age, gender)
            cls.patient_da.edit(patient)
            return True, f"Patient {weight, height, age, gender} Edited"
        except Exception as e:
            return False, str(e)


    @classmethod
    def remove(cls,weight, height, age, gender):
        try:
            cls.patient_da.remove(weight, height, age, gender)
            return True, f"Patient {weight, height, age, gender} Removed"
        except Exception as e:
            return False, str(e)


    @classmethod
    def find_by_patient_id(cls, patient_id):
        try:
            patient = cls.patient_da.find_by_patient_id(patient_id)
            if patient:
                return True, patient
            else:
                raise UserNotFoundException("User not found !!!")
        except Exception as e:
            return False, str(e)
        
    @classmethod
    def get_patient_data(cls, patient_id):
        try:
            patient = cls.patient_da.get_patient_data(patient_id)
            if patient:
                return patient
            else:
                return None  # when no patient is found
        except Exception as e:
            return False, str(e)

