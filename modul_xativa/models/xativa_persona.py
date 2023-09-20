from odoo import models, fields     
class XativaPersona(models.Model): 
    _name = 'xativa.persona'
    name = fields.Char(compute='_get_name',string='Nom persona',readonly='true',store=False)
    
    nom = fields.Char('Nom', required=True)
    cognoms = fields.Char('Cognoms', required=True)
    tipusIdentificacio = fields.Char('Tipus Identificació', required=True)
    identificacio = fields.Char('Identificació', required=True)
    correuElectronic = fields.Char('Correu Electrònic', required=True)
    telefon = fields.Integer('Telèfon', required=True)
    sexe = fields.Char('Sexe', required=True)
    foto = fields.Image('Foto', required=True)

    categoria = fields.Char('Categoria', required=True)
    dataNaixement = fields.Date('Data Naixement', required=True)
    paisNaixement = fields.Char('Pais de Naixement', required=True)
    direccioResidencia = fields.Char('Direcció', required=True)
    codiPostal = fields.Integer('Codi Postal', required=True)
    localitat = fields.Char('Localitat', required=True)
    provincia = fields.Char('Província', required=True)
    paisResidencia = fields.Char('Pais', required=True)
    
    identificacioAnvers = fields.Image('Identificació Anvers', required=True)
    identificacioRevers = fields.Image('Identificació Revers', required=True)
    validesaIdentificacio = fields.Date('Validesa Identificació', required=True)

    afiliatFederacio = fields.Char('Afiliat En Fede.', required=True)
    validatFederacio = fields.Boolean('Validat Federació', required=True)
    segurObligatori = fields.Boolean('Segur Obligatori', required=True)
    segurSolicitat = fields.Boolean('Segur Sol·licitat', required=False)
    segurPagat = fields.Boolean('Segur Pagat', required=False)
    jugadorReconeixementMedic = fields.Binary('Reconeix. Médic', required=False)
    jugadorReconeixementMedicData = fields.Date('Rec. Médic Data')
    jugadorAutoritzacioCategoriaSuperior = fields.Binary('Aut. Cat. Superior', required=False)

    identificacioTutor = fields.Char('Identificació', required=False)
    nomTutor = fields.Char('Nom', required=False)
    documentAutoritzacioTutor = fields.Binary('Doc. Autorizació', required=False)
    documentIdentificacioTutor = fields.Binary('Doc. Identificació', required=False)
    telefonTutor = fields.Integer('Telèfon', required=False)
    mailTutor = fields.Char('Mail', required=False)
    
    entrenadorTitolMonitorNivell1 = fields.Binary('Títol Monitor Nivell 1', required=False)
    entrenadorTitolMonitorNivell2 = fields.Binary('Títol Monitor Nivell 2', required=False)
    entrenadorTitolMonitorNivell3 = fields.Binary('Títol Monitor Nivell 3', required=False)
    entrenadorCertificatDelictesSexuals = fields.Binary('Cert. Delites Sexuals', required=False)
    
    dorsal = fields.Integer('Dorsal', required=False)
    tallaCamiseta = fields.Char('Camiseta', required=False)
    tallaSudadera = fields.Char('Sudadera', required=False)
    tallaPolo = fields.Char('Polo', required=False)
    tallaJaquetaXandall = fields.Char('Jaqueta Xandall', required=False)
    tallaPantaloXandall = fields.Char('Pantaló Xandall', required=False) 

    equip_jugador_ids = fields.Many2many('xativa.equip', 'equip_jugador_rel', 'persona_id', 'equip_id', string='Equips com jugador')
    equip_convidats_ids = fields.Many2many('xativa.equip', 'equip_convidat_rel', 'persona_id', 'equip_id', string='Equips com convidat')
    equip_entrenador_ids = fields.Many2many('xativa.equip', 'equip_oficial_rel', 'persona_id', 'equip_id', string='Equips com oficial')
    equip_staff_addicional_ids = fields.Many2many('xativa.equip', 'equip_staff_addicional_rel', 'persona_id', 'equip_id', string='Equips como staff addicional')
    directiva_id = fields.Many2one('xativa.directiva', string='Càrrec directiu')
    pagaments_ids = fields.One2many('xativa.pagament', 'persona_id', string='Pagaments')
    cobraments_ids = fields.One2many('xativa.cobrament', 'persona_id', string='Cobraments')

    nomCamiseta = fields.Char('Nom', required=False)
    tallaPantaloneta = fields.Char('Pantaloneta', required=False)
    esJugador = fields.Boolean("Es Jugador")
    esOficial = fields.Boolean("Es Oficial")
    actiu = fields.Boolean("Actiu")

   


    def _get_name(self):
        for record in self:
            record.name = str(record.nom + ' ' + record.cognoms)