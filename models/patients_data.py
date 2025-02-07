from odoo import fields, models,api
from odoo.exceptions import UserError,ValidationError
import datetime
import re

class PatientDescription(models.Model):
    _name = "patients.description"
    _description = "Patients Data Contains"

    name=fields.Char("Name",required=True)
    age = fields.Integer("Age",compute="_compute_age",required=True)
    mobile_number=fields.Char("Mobile_number")
    email_address=fields.Char("Email Address",required=True)
    address=fields.Char("Address")
    image=fields.Image("Image")
    disease=fields.Char("Diseases")
    description=fields.Text("Precautions")
    doctor_id=fields.Many2one(comodel_name="doctors.data")
    medicines_id=fields.Many2many(comodel_name="medicines.description",relation="patient_medincines_assign")
    date_of_birth = fields.Date("Date of Birth" ,required=True)

    def create(self,vals):
        """
        Vaildating the email and the mobile number before Creating the patient record
        """
        existing_email = self.env['patients.description'].search([('email_address', '=', vals['email_address'])])
        if existing_email:
            raise ValidationError("Email is Already Registered Please Use Another Email")
        else:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', vals['email_address']) # Apply Regex for email Vaildation
            if match==None: 
                raise ValidationError("Invalid Email Please Use A Valid Email")
        
        #Checking the Mobile Number 
        valid_number = re.match(r'^[6-9][0-9]{9}$', str(vals['mobile_number']))
        if valid_number == None:
            raise UserError("Invalid Mobile Number Please Enter A Valid Number")
        else:
            return super(PatientDescription,self).create(vals)

    def _compute_age(self):
        """
        Calculating the age of the patient using the Date of birth
        """
        for record in self:
            if record.date_of_birth:
                today = datetime.date.today()
                if today.strftime("%m%d") >= record.date_of_birth.strftime("%m%d"): #Comparing the current month and date with the date of birth month and date
                    record['age'] = today.year - record.date_of_birth.year
                else:
                    record['age'] = today.year - record.date_of_birth.year - 1
            else:
                record['age'] = 0 
        if record['age']<=-1:
            raise ValidationError("Invalid Date Of Birth") # Raising Validation Error for Provding the future date
    
    @api.constrains('mobile_number')
    def _check_unique_mobile_number(self):
        """
        Checking the Unique Mobile Number
        """
        for record in self:
            duplicate = self.search([('mobile_number', '=', record.mobile_number), ('id', '!=', record.id)])
            if duplicate:
                raise UserError(f"The mobile number {record.mobile_number} is already registered.")
    
    @api.constrains('name')
    def _check_name(self):
        """
        Checking the Name of the Patient is correct or not
        """
        for records in self:
            match=re.match('^[a-zA-Z][a-zA-z ]*',records.name)
            if match==None:
                raise ValidationError("Invaid Patient Name")
            

