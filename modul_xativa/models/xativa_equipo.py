from odoo import models, fields     

class XativaEquipo(models.Model): 
    _name = 'xativa.equipo'
    name = fields.Char(compute='_get_name',string='Nombre equipo',readonly='true',store=False)
    nombreComercial = fields.Char('Nombre Comercial', required=True)
    superficie = fields.Char('Superficie', required=True)
    categoria = fields.Char('Categoría', required=False)
    foto = fields.Image('Foto', required=False)
    temporada_id = fields.Many2one('xativa.temporada', string='Temporada')
    jugadores_ids = fields.Many2many('xativa.persona', 'equipo_jugador_rel', 'equipo_id', 'persona_id', string='Jugadores')
    entrenadores_ids = fields.Many2many('xativa.persona', 'equipo_entrenador_rel', 'equipo_id', 'persona_id', string='Entrenadores')

    def _get_name(self):
        for record in self:
            record.name = str(record.nombreComercial + ' ' + record.categoria)