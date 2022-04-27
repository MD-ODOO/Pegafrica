# -*- coding: utf-8 -*-


from datetime import date, datetime
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Nextofkin(models.Model):
    _inherit = 'res.partner'
    
    first_name = fields.Char(string='First name')
    last_name = fields.Char(string='Last name')
    age = fields.Integer(string='Age',compute='compute_age')
    date = fields.Date(string='Date of birth')

   #methode to calculate age by using date of birth 
    @api.depends('date')
    def compute_age(self):
        '''Method to calculate age'''
        current_dt = date.today()
        for rec in self:
            if rec.date:
                start = rec.date
                age_calc = ((current_dt - start).days / 365)
                # Age should be greater than 0
                if age_calc > 0.0:
                    rec.age = age_calc
            else:
                rec.age = 0
