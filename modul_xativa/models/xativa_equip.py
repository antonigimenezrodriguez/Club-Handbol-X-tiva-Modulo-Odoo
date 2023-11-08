from odoo import models, fields     

class XativaEquip(models.Model): 
    _name = 'xativa.equip'
    name = fields.Char(compute='_get_name',string='Nom equip',readonly='true',store=False)
    nomComercial = fields.Char('Nom Comercial', required=True)
    superficie = fields.Char('Superfície', required=True)
    categoria = fields.Char('Categoria', required=True)
    foto = fields.Image('Foto', required=False)
    tripticFederacio = fields.Binary('Tríptic Federació')
    tripticJOCSE = fields.Binary('Tríptic JOCSE')
    llicenciesFederacio = fields.Binary('Llicències Federació')
    llicenciesJOCSE = fields.Binary('Llicències JOCSE')

    temporada_id = fields.Many2one('xativa.temporada', string='Temporada')
    entrenador_id = fields.Many2one('xativa.persona', string='Entrenador')
    ajudant_entrenador_id = fields.Many2one('xativa.persona', string='Ajudant entrenador')
    jugadors_ids = fields.Many2many('xativa.persona', 'equip_jugador_rel', 'equip_id', 'persona_id', string='Jugadors')
    convidats_ids = fields.Many2many('xativa.persona', 'equip_convidat_rel', 'equip_id', 'persona_id', string='Convidats')
    entrenadors_ids = fields.Many2many('xativa.persona', 'equip_entrenador_rel', 'equip_id', 'persona_id', string='Oficials')
    staff_addicional_ids = fields.Many2many('xativa.persona', 'equip_staff_addicional_rel', 'equip_id', 'persona_id', string='Staffs adicionals')
    esponsors_ids = fields.Many2many('xativa.esponsor', 'equip_esponsor_rel', 'equip_id', 'esponsor_id', string='Esponsors')

    def _get_name(self):
        for record in self:
            record.name = str(record.nomComercial + ' ' + record.categoria)