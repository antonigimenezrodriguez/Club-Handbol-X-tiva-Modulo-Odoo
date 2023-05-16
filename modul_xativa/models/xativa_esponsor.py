from odoo import models, fields     

class XativaEsponsor(models.Model): 
    _name = 'xativa.esponsor'
    name = fields.Char(compute='_get_name',string='Nombre Esponsor',readonly='true',store=False)
    nomEsponsor = fields.Char('Nom', required=True)
    importSenseIVA = fields.Float('Import sense IVA', required=False)
    importAmbIVA = fields.Float('Import amb IVA', required=False)
    dadesFiscals = fields.Text('Dades Fiscals', required=False)
    equips_ids = fields.Many2many('xativa.equipo', 'equip_esponsor_rel', 'esponsor_id', 'equip_id', string='Equips esponsoritzats')

    

    def _get_name(self):
        for record in self:
            record.name = str(record.nomEsponsor)