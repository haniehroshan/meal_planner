from datetime import datetime


class Visit:
    def __init__(self, patient, doctor):
        self.patient = patient
        self.doctor = doctor
        self.date = datetime.now()

    @property
    def patient(self):
        return self._patient

    @patient.setter
    def patient(self, patient):
        self._patient = patient

    @property
    def doctor(self):
        return self._doctor

    @doctor.setter
    def doctor(self, doctor):
        # self._password = Validation.password_validator(password)
        self._doctor = doctor

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date