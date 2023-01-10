
from odoo import api, fields, models, _

class Student(models.Model):
    _name = 'school.student'
    _description = 'student'
    name = fields.Char('Student Name', required=True)
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    birth_date = fields.Date('Date of Birth')
    gender = fields.Selection([('M','Male'),('F','Female')],'Gender')

