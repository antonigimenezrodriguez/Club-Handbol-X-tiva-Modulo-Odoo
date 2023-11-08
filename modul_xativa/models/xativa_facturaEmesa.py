from odoo import models, fields     
class XativaFacturaEmesa(models.Model): 
    _name = 'xativa.facturaemesa'
    name = fields.Char(compute='_get_name',string='Factura',readonly='true',store=False)
    numeroFactura = fields.Char('Número Factura')
    dataFactura = fields.Date('Data Factura')
    facturaDocument = fields.Binary('Document Factura')
    descripcio = fields.Text('Descripció')
    importSenveIVA = fields.Float('Import')
    IVAPercentatge = fields.Float('IVA %')
    importIVA = fields.Float('Import IVA')
    total = fields.Float('Total')
    cobrada = fields.Boolean('Cobrada')
    justificantCobrament = fields.Binary('Justificant')
    empresa_id = fields.Many2one('xativa.empresa', string='Empresa')

    def _get_name(self):
        for record in self:
            record.name = str(record.numeroFactura) + ' - ' + record.empresa_id.rao_social