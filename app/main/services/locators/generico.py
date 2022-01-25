SIMPLES_SERVICOS = '//*[@id="botaoSimples"]'
CRIAR_CHAVE = '//*[@id="grupo"]/ul/li[1]/p/a[contains(., "Clique Aqui")]'

# Formulario
INPUT_CNPJ = '//*[@id="ctl00_ContentPlaceHolder_txtCNPJ"]'
INPUT_CPF = '//*[@id="ctl00_ContentPlaceHolder_txtCPFResponsavel"]'
INPUT_TITULO = '//input[@id="ctl00_ContentPlaceHolder_txtTituloEleitor"]'
INPUT_RECIBO = '//input[@id="ctl00_ContentPlaceHolder_txtReciboIRPF"]'
FIELD_ANO_RECIBO = '//select[@id="ctl00_ContentPlaceHolder_ddlExercicio"]'
INPUT_NASCIMENTO = '//*[@id="ctl00_ContentPlaceHolder_txtDataNascimento"]'
LIST_ANO_RECIBO = '//select[@id="ctl00_ContentPlaceHolder_ddlExercicio"]/option'
BUTTON_VALIDAR = '//*[@id="ctl00_ContentPlaceHolder_btValidar"]'
BUTTON_CONTINUAR = '//input[@id="ctl00_ContentPlaceHolder_btContinuar"]'
INPUT_CHAVE = '//*[@id="ctl00_ContentPlaceHolder_txtCodigoAcesso"]'
ELEMENT_ERROR_DADOS = '//span[@id="ctl00_ContentPlaceHolder_lblErroAutentica"]'

# Chave
TEXT_CHAVE = '//*[@id="ctl00_ContentPlaceHolder_lblResultado"]/span'

# Captcha
CAPTCHA_IMAGE = '//*[@id="captcha-img"]'
CAPTCHA_INPUT = '//*[@id="txtTexto_captcha_serpro_gov_br"]'
ERRO_CAPTCHA = '//span[contains(., "anti-robô inválido")]'
ELEMENT_VOLTAR = '//*[@id="ultimo"]/a'
ELEMENT_ATUALIZAR_CAPTCHA = '//*[@id="btnRecarregar_captcha_serpro_gov_br"]'

# Enquadrar
ELEMENT_ENQUADRAR = '//*[@id="grupo"]/table[1]/tbody/tr[1]/td[2]/a/img'
ELEMENT_ERROR = '//*[@id="ctl00_ContentPlaceHolder_lblErro"]'
ELEMENT_IFRAME = '//iframe[@id="frame"]'
ELEMENT_AVISO = '//div[@id="mensagem-aviso"]'
ELEMENT_MENSAGEM = '//span[@id="ctl00_ContentPlaceHolder1_pnlMensagem_lblMensagem"]'
ELEMENT_ERROR_DADOS_ENQUADRAR = '//span[@id="ctl00_ContentPlaceHolder_lblErro"]'
ELEMENT_CONFIRMAR = '//*[@id="ctl00_ContentPlaceHolder1_btnConfirma"]'
ELEMENT_ACEITAR = '//*[@id="ctl00_ContentPlaceHolder1_btnAceitar"]'
ELEMENT_DT_CNPJ = '//*[@id="ctl00_ContentPlaceHolder1_txtDataInscricao"]'
ELEMENT_CONFIRMAR_DT = '//*[@id="ctl00_ContentPlaceHolder1_btnConfirmaData"]'
ELEMENT_SALVAR = '//*[@id="btnSalva"]'
ELEMENT_TEXT_DT = '//*[@id="ctl00_ContentPlaceHolder1_pnlMensagem_lblMensagem"]'
ELEMENT_ACOMPANHAMENTO = '//a[contains(.,"Acompanhamento de Solicitação")]'
ELEMENT_INICIO_ATIVIDADE = '//*[@id="ctl00_ContentPlaceHolder1_btnInicioAtividade"]'

mensagem_ja_enquadrou = ('Solicitação de opção pelo Simples Nacional não aceita.\n'
                         'Motivo: existe uma solicitação de opção pelo Simples Nacional'
                         ' pendente de confirmação para esta pessoa jurídica.\nCaso deseje'
                         ' verificar detalhes, acione o link a seguir.'
                         ' Acompanhamento de Solicitação de Opção pelo Simples Nacional')

mensagens = [
    ('Solicitação de opção pelo Simples Nacional não aceita.\n'
     'Motivo: período não permitido para a pessoa jurídica que '
     'já iniciou atividade solicitar a opção pelo Simples Nacional.'
     'A solicitação de opção pelo Simples Nacional de pessoa jurídica'
     ' que já iniciou atividade somente pode ser solicitada no '
     'mês de janeiro.'),
    'Código de acesso inválido'
]
