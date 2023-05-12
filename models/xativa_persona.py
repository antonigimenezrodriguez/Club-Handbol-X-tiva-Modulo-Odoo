from odoo import models, fields     
class xativa_persona(models.Model): 
    _name = 'xativa.persona'
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    telefono = fields.Integer('Telefono', required=True)
    sexo = fields.Char('Sexo', required=True)
    paisNacimiento = fields.Char('País de Nacimiento', required=True)
    paisResidencia = fields.Char('País de Residencia', required=True)
    direccionResidencia = fields.Char('Dirección de Residencia', required=True)
    codigoPostal = fields.Integer('Codigo Postal', required=True)
    localidad = fields.Char('Localidad', required=True)
    provincia = fields.Char('Provincia', required=True)
    fechaNacimiento = fields.Date('Fecha de Nacimiento', required=True)
    correoElectronico = fields.Char('Correo Electrónico', required=True)
    tipoIdentificacion = fields.Char('Tipo de Identificación', required=True)
    identificacion = fields.Char('Identificación', required=True)
    validezIdentificacion = fields.Char('Validez Identificación', required=True)
    identificacionTutor = fields.Char('Identificación del Tutor', required=False)
    nombreTutor = fields.Char('Nombre del tutor', required=False)
    documentoAutorizacionTutor = fields.Binary('Documento Autorizacion Tutor', required=True)


    






