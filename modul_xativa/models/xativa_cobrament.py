from odoo import models, fields     

class XativaCobrament(models.Model): 
    _name = 'xativa.cobrament'
    name = fields.Char(compute='_get_name',string='Cobrament',readonly='true',store=False)
    dataCobrament = fields.Date('Data de cobrament', required=True)
    importe = fields.Float('Import', required=True) # En castellà perque import es paraula reservada
    concepte = fields.Char('Concepte', required=True)
    justificant = fields.Binary('Justificant')
    persona_id = fields.Many2one('xativa.persona', string='Persona')
       
       

    def _get_name(self):
        for record in self:
            record.name = str(record.persona_id.name + ' ' + record.concepte + ' ' + str(record.importe) + ' ' + str(record.dataCobrament))