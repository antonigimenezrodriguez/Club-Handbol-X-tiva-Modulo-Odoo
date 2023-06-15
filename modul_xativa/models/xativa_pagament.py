from odoo import models, fields     

class XativaPagament(models.Model): 
    _name = 'xativa.pagament'
    name = fields.Char(compute='_get_name',string='Pagament',readonly='true',store=False)
    dataPagament = fields.Date('Data de pagament', required=True)
    importe = fields.Float('Import', required=True) # En castellà perque import es paraula reservada
    concepte = fields.Char('Concepte', required=True)
    justificant = fields.Binary('Justificant')
    persona_id = fields.Many2one('xativa.persona', string='Persona')
       
       

    def _get_name(self):
        for record in self:
            record.name = str(record.persona_id.name + ' ' + record.concepte + ' ' + str(record.importe) + ' ' + str(record.dataPagament))