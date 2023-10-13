from odoo import models, fields     

class XativaDesgrava(models.Model): 
    _name = 'xativa.desgrava'
    name = fields.Char(compute='_get_name',string='Import Publicitat',readonly='true',store=False)
    importPublicitat = fields.Char('Import Publicitat', required=True)
    importDesgravat = fields.Char('Import Desgravat', required=True)
    

    def _get_name(self):
        for record in self:
            record.name = str(record.importPublicitat)