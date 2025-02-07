from odoo import fields,models,api

class PatientsWizards(models.TransientModel):
    _name="patients.wizards"
    _description=" Delete Teachers Data"

    patients_id=fields.Many2one(
        string="Patient Details",
        comodel_name="patients.description",
        relation='patient_data_rel'
    )
    medicine_ids=fields.Many2many(
        string="Medicines",
        comodel_name="medicines.description",
        relation='medicines_data_rel'
    )
    precautions=fields.Text("Precautions")

    def action_delete_data(self):
        self.patients_id.description=self.precautions
        self.patients_id.medicines_id=self.medicine_ids