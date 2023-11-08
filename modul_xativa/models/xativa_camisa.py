# from odoo import models, fields     

# class XativaCamisa(models.Model): 
#     _name = 'xativa.camisa'
#     name = fields.Char(compute='_get_name',string='Camisa',readonly='true',store=False)
#     persona_id = fields.Many2one('xativa.persona', string='Persona demana',required=True)
#     dorsal = fields.Integer('dorsal')
#     talla = fields.Char('Talla')
#     porter = fields.Boolean('Porter')
#     manega = fields.Selection(string='Mànega',selection=[('curta','Curta'),('llarga','Llarga')])
#     nomCamisa = fields.Char('Nom Camisa')
#     equip = fields.Selection(string='Equip',selection=[('benjami', 'Benjamí'),('aleviF', 'Aleví F'),('aleviM','Aleví M'),('infantil','Infantil'),('cadet','Cadet'),('juvenil','Juvenil'),('seniorM','Senior M'),('seniorF','Senior F'),('segona','Segona equipació')])
#     patro = fields.Selection(string='Patró',selection=[('xic','Xic'),('xica','Xica')])
#     dataDemanat = fields.Date('Data Demanat')
#     dataArribada = fields.Date('Data Arribada')
#     pagat = fields.Boolean('Pagat')
#     entregat = fields.Boolean('Entregat')
#     preu = fields.Float('Preu')
#     observacions = fields.Text('Observacions')
#     temporada_id = fields.Many2one('xativa.temporada', string='Temporada')
       
       

#     def _get_name(self):
#         for record in self:
#             record.name = str(record.persona_id.name)