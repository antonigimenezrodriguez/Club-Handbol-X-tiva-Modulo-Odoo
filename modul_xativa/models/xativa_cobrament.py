from odoo import models, fields     

class XativaCobrament(models.Model): 
    _name = 'xativa.cobrament'
    name = fields.Char(compute='_get_name',string='Cobrament',readonly='true',store=False)
    categoria = fields.Char(compute='_get_categoria',string='Categoria',readonly='true',store=False)
    dataCobrament = fields.Date('Data de cobrament')
    importe = fields.Float('Import', required=True) # En castellà perque import es paraula reservada
    concepte = fields.Char('Concepte', required=True)
    justificant = fields.Binary('Justificant')
    formaCobrament = fields.Selection(string='Forma Cobrament',selection=[('transferencia', 'Transferència'),('enMa', 'En mà'),('compensacioFitxa','Compensació Fitxa'),('remesa','Remesa')])
    cobrat = fields.Boolean('Cobrat')
    persona_id = fields.Many2one('xativa.persona', string='Persona')
    temporada_id = fields.Many2one('xativa.temporada', string='Temporada')
       
       

    def _get_name(self):
        for record in self:
            record.name = str(record.persona_id.name + ' ' + record.concepte + ' ' + str(record.importe))

    def _get_categoria(self):
        for record in self:
            record.categoria = record.persona_id.categoria