from odoo import models, fields     
class XativaEmpresa(models.Model): 
    _name = 'xativa.empresa'
    name = fields.Char(compute='_get_name',string='Empresa',readonly='true',store=False)
    rao_social = fields.Char('Raó Social', required=True)
    cif = fields.Char('CIF', required=True)
    direccio = fields.Char('Direcció', required=True)
    poblacio = fields.Char('Població', required=True)
    provincia = fields.Char('Provincia', required=True)
    codi_postal = fields.Integer('Codi Postal', required=True)
    
    facturesRebudes_ids = fields.One2many('xativa.facturarebuda', 'empresa_id', string='Factures rebudes')
    facturesEmeses_ids = fields.One2many('xativa.facturaemesa', 'empresa_id', string='Factures emeses')
    sponsors_ids = fields.One2many('xativa.esponsor', 'empresa_id', string='Esponsors')

    def _get_name(self):
        for record in self:
            record.name = str(record.rao_social)