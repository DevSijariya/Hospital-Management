from odoo import fields, models,api
from odoo.exceptions import UserError


class MedicinesDescription(models.Model):
    _name = "medicines.description"
    _description = "Medicines Description"

    name=fields.Char("Name" ,required=True)
    description=fields.Text("Description",required=True)
    price=fields.Integer("Price",required=True)
    
    # Vaildating the name and the price of the medicine using sql constraint 
    _sql_constraints = [('name_unique','UNIQUE(name)','The medicine is already added'),('check_price_value','CHECK(price>0)','Price must be non zero positive value ')]