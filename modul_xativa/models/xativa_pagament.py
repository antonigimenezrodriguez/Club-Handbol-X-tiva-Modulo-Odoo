from odoo import models, fields     

class XativaPagament(models.Model): 
    _name = 'xativa.pagament'
    name = fields.Char(compute='_get_name',string='Pagament',readonly='true',store=False)
    categoria = fields.Char(compute='_get_categoria',string='Categoria',readonly='true',store=False)
    dataPagament = fields.Date('Data de pagament', required=False)
    importe = fields.Float('Import', required=True) # En castellà perque import es paraula reservada
    concepte = fields.Char('Concepte', required=True)
    justificant = fields.Binary('Justificant')
    pagat = fields.Boolean('Pagat')
    formaPagament = fields.Selection(string='Forma Pagament',selection=[('transferencia', 'Transferència'),('enMa', 'En mà'),('compensacioFitxa','Compensació Fitxa')])
    persona_id = fields.Many2one('xativa.persona', string='Persona', required=True)
    temporada_id = fields.Many2one('xativa.temporada', string='Temporada')
       
       

    def _get_name(self):
        for record in self:
            record.name = str(record.persona_id.name + ' ' + record.concepte + ' ' + str(record.importe))

    def _get_categoria(self):
        for record in self:
            record.categoria = record.persona_id.categoria