from odoo import models, fields     

class XativaActaJunta(models.Model): 
    _name = 'xativa.actajunta'
    name = fields.Char(compute='_get_name',string='Número',readonly='true',store=False)
    numero = fields.Integer('Núm. Acta')
    data = fields.Datetime('Data i hora')
    lloc = fields.Char('Lloc')
    observacions = fields.Text('Obervacions')
    convocatoria = fields.Binary('Convocatòria')
    acta = fields.Binary('Acta')
    temporada_id = fields.Many2one('xativa.temporada', string='Temporada')
    

    def _get_name(self):
        for record in self:
            record.name = str(record.numero)