from odoo import models, fields     
class xativa_temporada(models.Model): 
    _name = 'xativa.temporada'
    temporada = fields.Char('Nombre Comercial', required=True)