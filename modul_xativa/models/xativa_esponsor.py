from odoo import models, fields     

class XativaEsponsor(models.Model): 
    _name = 'xativa.esponsor'
    name = fields.Char(compute='_get_name',string='Nombre Esponsor',readonly='true',store=False)
    nombreEsponsor = fields.Char('Nombre', required=True)
    importeSinIVA = fields.Float('Importe sin IVA', required=False)
    importeConIVA = fields.Float('Importe con IVA', required=False)
    datosFiscales = fields.Text('Datos Fiscales', required=False)
    equipo_ids = fields.Many2many('xativa.equipo', 'equipo_esponsor_rel', 'esponsor_id', 'equipo_id', string='Equipos esponsorizados')

    

    def _get_name(self):
        for record in self:
            record.name = str(record.nombreEsponsor)