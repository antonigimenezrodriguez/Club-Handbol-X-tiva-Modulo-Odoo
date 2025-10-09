from odoo import models, fields, api

class XativaFacturaEmesa(models.Model):
    _name = 'xativa.facturaemesa'
    _order = 'dataFactura desc, numeroFactura desc'

    name = fields.Char(compute='_get_name', string='Factura', readonly=True, store=False)
    numeroFactura = fields.Char('Número Factura')
    dataFactura = fields.Date('Data Factura')
    facturaDocument = fields.Binary('Document Factura')
    descripcio = fields.Text('Descripció')
    importSenseIVA = fields.Float('Import sense IVA')
    IVAPercentatge = fields.Float('IVA (%)', help="Percentatge d'IVA, per exemple 21 per a un 21%")

    importIVA = fields.Float(
        string='Import IVA',
        compute='_compute_imports',
        store=True,
        readonly=True
    )

    total = fields.Float(
        string='Total amb IVA',
        compute='_compute_imports',
        store=True,
        readonly=True
    )

    cobrada = fields.Boolean('Cobrada')
    justificantCobrament = fields.Binary('Justificant')
    empresa_id = fields.Many2one('xativa.empresa', string='Empresa')

    @api.depends('importSenseIVA', 'IVAPercentatge')
    def _compute_imports(self):
        for record in self:
            iva_percent = record.IVAPercentatge or 0.0
            base = record.importSenseIVA or 0.0

            # Calcular el importe del IVA
            record.importIVA = base * iva_percent / 100.0

            # Calcular el total con IVA
            record.total = base + record.importIVA

    def _get_name(self):
        for record in self:
            parts = []
            if record.numeroFactura:
                parts.append(str(record.numeroFactura))
            if record.empresa_id and record.empresa_id.rao_social:
                parts.append(record.empresa_id.rao_social)
            record.name = " - ".join(parts) if parts else "Factura sense dades"
