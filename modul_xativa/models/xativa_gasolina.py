from odoo import models, fields     

class XativaGasolina(models.Model): 
    _name = 'xativa.gasolina'
    name = fields.Char(compute='_get_name',string='Kilómetres',readonly='true',store=False)
    kilometres = fields.Char('Kilómetres', required=True)
    importe = fields.Char('Import', required=True)
    

    def _get_name(self):
        for record in self:
            record.name = str(record.kilometres)