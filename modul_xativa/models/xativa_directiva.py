from odoo import models, fields     

class XativaDirectiva(models.Model): 
    _name = 'xativa.directiva'
    name = fields.Char(compute='_get_name',string='Cargo',readonly='true',store=False)
    cargo = fields.Char('Cargo', required=True)
    personas_ids = fields.One2many('xativa.persona','directiva_id',string='Cargos directivos')
    personas = fields.Char(compute='_get_cargos',string='Personas',readonly='true',store=False)
    

    def _get_name(self):
        for record in self:
            record.name = str(record.cargo)

    def _get_cargos(self):
        for record in self:
            cargos=""
            for persona in record.personas_ids:
                cargos=cargos+persona.nombre+' '+persona.apellidos
            record.personas = cargos