from odoo import models, fields     
class XativaNomina(models.Model): 
    _name = 'xativa.nomina'
    _order = 'any desc, mes desc, persona_id'
    name = fields.Char(compute='_get_name',string='Nomina',readonly='true',store=False)
    any = fields.Integer('Any')
    mes = fields.Integer('Mes')
    IRPF = fields.Float('IRPF')
    totalBrut = fields.Float('Brut')
    totalNet = fields.Float('Net')
    document = fields.Binary('Document')
    justificant = fields.Binary('Justificant')
    persona_id = fields.Many2one('xativa.persona', string='Persona')

    def _get_name(self):
        for record in self:
            record.name = str(str(record.any) + ' ' + str(record.mes) + ' ' + record.persona_id.name)