from odoo import models, fields     

class XativaDirectiva(models.Model): 
    _name = 'xativa.directiva'
    name = fields.Char(compute='_get_name',string='Càrrec',readonly='true',store=False)
    carrec = fields.Char('Càrrec', required=True)
    persones_ids = fields.One2many('xativa.persona','directiva_id',string='Càrrecs directius')
    persones = fields.Char(compute='_get_carrecs',string='Persones',readonly='true',store=False)
    

    def _get_name(self):
        for record in self:
            record.name = str(record.carrec)

    def _get_carrecs(self):
        for record in self:
            carrecs=""
            for persona in record.persones_ids:
                carrecs=carrecs+persona.nom+' '+persona.cognoms
            record.persones = carrecs