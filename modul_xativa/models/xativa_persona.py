from odoo import models, fields     
class XativaPersona(models.Model): 
    _name = 'xativa.persona'
    _order = 'nom asc'
    name = fields.Char(compute='_get_name',string='Nom persona',readonly='true',store=False)
    
    nom = fields.Char('Nom', required=False)
    cognoms = fields.Char('Cognoms', required=False)
    tipusIdentificacio = fields.Char('Tipus Identificació', required=False)
    identificacio = fields.Char('Identificació', required=False)
    correuElectronic = fields.Char('Correu Electrònic', required=False)
    telefon = fields.Integer('Telèfon', required=False)
    sexe = fields.Char('Sexe', required=False)
    foto = fields.Image('Foto', required=False)

    categoria = fields.Char('Categoria', required=False)
    dataNaixement = fields.Date('Data Naixement', required=False)
    paisNaixement = fields.Char('Pais de Naixement', required=False)
    direccioResidencia = fields.Char('Direcció', required=False)
    codiPostal = fields.Integer('Codi Postal', required=False)
    localitat = fields.Char('Localitat', required=False)
    provincia = fields.Char('Província', required=False)
    paisResidencia = fields.Char('Pais', required=False)
    
    identificacioAnvers = fields.Image('Identificació Anvers', required=False)
    identificacioRevers = fields.Image('Identificació Revers', required=False)
    validesaIdentificacio = fields.Date('Validesa Identificació', required=False)

    afiliatFederacio = fields.Char('Afiliat En Fede.', required=False)
    validatFederacio = fields.Boolean('Validat Federació', required=False)
    segurObligatori = fields.Boolean('Segur Obligatori', required=False)
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
    entrenadorCertificatDelictesSexuals = fields.Binary('Cert. Delictes Sexuals', required=False)
    entrenadorDataCertificatDelictesSexuals = fields.Date('Data Cert. Del. Sex.', required=False)
    
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
    esponsors_ids = fields.One2many('xativa.esponsor', 'persona_id', string='Esponsors Aportats')

    nomCamiseta = fields.Char('Nom', required=False)
    tallaPantaloneta = fields.Char('Pantaloneta', required=False)
    esJugador = fields.Boolean("Es Jugador")
    esOficial = fields.Boolean("Es Oficial")
    actiu = fields.Boolean("Actiu")
    IBAN = fields.Char('IBAN')
    documentAutoritzacioIBAN = fields.Binary('Doc. Aut. IBAN')
    domiciliaQuotes = fields.Boolean('Domicilia Quotes')
    observacioQuotes = fields.Text('Observacio Quotes')


    def _get_name(self):
        for record in self:
            record.name = str(record.nom + ' ' + record.cognoms)