from odoo import models, fields     

class XativaPago(models.Model): 
    _name = 'xativa.pago'
    name = fields.Char(compute='_get_name',string='Pago',readonly='true',store=False)
    fechaPago = fields.Date('Fecha de Pago', required=True)
    importe = fields.Float('Importe', required=True)
    concepto = fields.Char('Concepto', required=True)
    persona_id = fields.Many2one('xativa.persona', string='Persona')
       
       

    def _get_name(self):
        for record in self:
            record.name = str(record.persona_id.name + ' ' + record.concepto + ' ' + str(record.importe) + ' ' + str(record.fechaPago))