from odoo import models, fields     
class XativaPersona(models.Model): 
    _name = 'xativa.persona'
    name = fields.Char(compute='_get_name',string='Nombre persona',readonly='true',store=False)
    
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    tipoIdentificacion = fields.Char('Tipo Identificación', required=True)
    identificacion = fields.Char('Identificación', required=True)
    correoElectronico = fields.Char('Correo Electrónico', required=True)
    telefono = fields.Integer('Telefono', required=True)
    sexo = fields.Char('Sexo', required=True)
    foto = fields.Image('Foto', required=True)

    categoria = fields.Char('Categoria', required=True)
    fechaNacimiento = fields.Date('Fecha Nacimiento', required=True)
    paisNacimiento = fields.Char('País de Nacimiento', required=True)
    direccionResidencia = fields.Char('Dirección', required=True)
    codigoPostal = fields.Integer('Codigo Postal', required=True)
    localidad = fields.Char('Localidad', required=True)
    provincia = fields.Char('Provincia', required=True)
    paisResidencia = fields.Char('País', required=True)
    
    identificacionAnverso = fields.Image('Identificacion Anverso', required=True)
    identificacionReverso = fields.Image('Identificacion Reverso', required=True)
    validezIdentificacion = fields.Date('Validez Identificación', required=True)

    afiliadoFederacion = fields.Char('Afiliado En Fede.', required=True)
    validadoFederacion = fields.Boolean('Validado Federacion', required=True)
    seguroObligatorio = fields.Boolean('Seguro Obligatorio', required=True)
    seguroSolicitado = fields.Boolean('Seguro Solicitado', required=False)
    seguroPagado = fields.Boolean('Seguro Pagado', required=False)
    jugadorReconocimientoMedico = fields.Binary('Reconoc. Medico', required=False)
    jugadorAutorizacionCategoriaSuperior = fields.Binary('Aut. Cat. Superior', required=False)

    identificacionTutor = fields.Char('Identificación', required=False)
    nombreTutor = fields.Char('Nombre', required=False)
    documentoAutorizacionTutor = fields.Binary('Doc. Autorizacion', required=False)
    documentoIdentificacionTutor = fields.Binary('Doc. Identificacion', required=False)
    telefonoTutor = fields.Integer('Teléfono', required=False)
    mailTutor = fields.Char('Mail', required=False)
    
    entrenadorTituloMonitorNivel1 = fields.Binary('Titulo Monitor Nivel 1', required=False)
    entrenadorTituloMonitorNivel2 = fields.Binary('Titulo Monitor Nivel 2', required=False)
    entrenadorTituloMonitorNivel3 = fields.Binary('Titulo Monitor Nivel 3', required=False)
    entrenadorCertificadoDelitosSexuales = fields.Binary('Cert. Delitos Sexuales', required=False)
    
    dorsal = fields.Integer('Dorsal', required=False)
    tallaCamiseta = fields.Char('Camiseta', required=False)
    tallaSudadera = fields.Char('Sudadera', required=False)
    tallaPolo = fields.Char('Polo', required=False)
    tallaChaquetaChandal = fields.Char('Chaqueta Chandal', required=False)
    tallaPantalonChandal = fields.Char('Pantalón Chandal', required=False) 

    equipo_jugador_ids = fields.Many2many('xativa.equipo', 'equipo_jugador_rel', 'persona_id', 'equipo_id', string='Equipos como jugador')
    equipo_invitados_ids = fields.Many2many('xativa.equipo', 'equipo_invitado_rel', 'persona_id', 'equipo_id', string='Equipos como invitado')
    equipo_entrenador_ids = fields.Many2many('xativa.equipo', 'equipo_oficial_rel', 'persona_id', 'equipo_id', string='Equipos como oficial')
    equipo_staff_adicional_ids = fields.Many2many('xativa.equipo', 'equipo_staff_adicional_rel', 'persona_id', 'equipo_id', string='Equipos como staff adicional')
    directiva_id = fields.Many2one('xativa.directiva', string='Cargo directivo')
    pagos_ids = fields.One2many('xativa.pago', 'persona_id', string='Pagos')

   


    def _get_name(self):
        for record in self:
            record.name = str(record.nombre + ' ' + record.apellidos)
    
    def _check_jugador(self):
        for record in self:
            if(len(record.equipo_jugador_ids)>0):
                record.esJugador = True
    
    def _check_oficial(self):
        for record in self:
            if(len(record.equipo_entrenador_ids)>0):
                record.esJugador = True