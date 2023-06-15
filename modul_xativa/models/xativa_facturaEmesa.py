from odoo import models, fields     
class XativaFacturaEmesa(models.Model): 
    _name = 'xativa.facturaemesa'
    name = fields.Char(compute='_get_name',string='Factura',readonly='true',store=False)
    numeroFactura = fields.Char('Número Factura')
    CIF = fields.Char('CIF')
    empresa = fields.Char('Empresa')
    direccio = fields.Char('Direcció')
    dataFactura = fields.Char('Data Factura')
    facturaDocument = fields.Binary('Document Factura')
    descripcio = fields.Char('Descripció')
    importSenveIVA = fields.Float('Import')
    IVAPercentatge = fields.Float('IVA %')
    importIVA = fields.Float('Import IVA')
    total = fields.Float('Total')
    cobrada = fields.Boolean('Cobrada')
    justificantCobrament = fields.Binary('Justificant')

    def _get_name(self):
        for record in self:
            record.name = str(record.numeroFactura + record.empresa)