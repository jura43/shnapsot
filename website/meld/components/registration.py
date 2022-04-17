from flask_meld import Component
from forms.registration_form import RegistrationForm

class Registration(Component):
    form = RegistrationForm()

    def updated(self, field):
        self.validate(field)