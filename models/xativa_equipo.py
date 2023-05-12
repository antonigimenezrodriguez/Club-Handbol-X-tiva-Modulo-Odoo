from odoo import models, fields     
class xativa_equipo(models.Model): 
    _name = 'xativa.equipo'
    nombreComercial = fields.Char('Nombre Comercial', required=True)
    superficie = fields.Char('Superficie', required=True)
    categoria = fields.Char('Categoría', required=False)