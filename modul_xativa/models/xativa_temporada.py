from odoo import models, fields     
class XativaTemporada(models.Model): 
    _name = 'xativa.temporada'
    name = fields.Char(compute='_get_name',string='Temporada',readonly='true',store=False)
    temporada = fields.Char('Temporada', required=True)
    equipos_ids = fields.One2many('xativa.equipo', 'temporada_id', string='Equipos')

    def _get_name(self):
        for record in self:
            record.name = str(record.temporada)