from odoo import models, fields     

class XativaEsponsor(models.Model): 
    _name = 'xativa.esponsor'
    name = fields.Char(compute='_get_name',string='Nom Esponsor',readonly='true',store=False)
    nomEsponsor = fields.Text('Nom', required=True)
    importSenseIVA = fields.Float('Import sense IVA', required=False)
    importAmbIVA = fields.Float('Import amb IVA', required=False)
    cif = fields.Char('CIF', required=False)
    direccio = fields.Char('Direcció', required=False)
    codiPostal = fields.Integer('Codi postal', required=False)
    localitat = fields.Char('Localitat', required=False)
    provincia = fields.Char('Província', required=False)
    pais = fields.Char('Pais', required=False)
    telefonsContacte = fields.Text('Telèfons de contacte', required=False)
    mailsContacte = fields.Text('Mails de contacte', required=False)
    personesContacte = fields.Text('Persones de contacte', required=False)
    observacions = fields.Text('Observacions', required=False)
    contracte = fields.Binary('Contracte', required=False)
    factura = fields.Binary('Factura', required=False)
    justificant = fields.Binary('Justificant')

    equips_ids = fields.Many2many('xativa.equip', 'equip_esponsor_rel', 'esponsor_id', 'equip_id', string='Equips esponsoritzats')
    temporada_id = fields.Many2one('xativa.temporada', string='Temporada')

    

    def _get_name(self):
        for record in self:
            record.name = str(record.nomEsponsor)