from loguru import logger
from app.main.services.browser import abrir_navegador

from app.main.schemas.chave_acesso import CriaChave, RetornaChave
from app.main.services.locators import generico
from app import config
from app.main.services.captcha import quebra_captcha


def erro_de_acesso(browser):
    error = browser.is_element_visible(generico.ELEMENT_ERROR_DADOS)
    if error:
        msg_error = browser.get_text(generico.ELEMENT_ERROR_DADOS)
        return msg_error
    else:
        False


def gerar_chave(dados: CriaChave):
    resultado = {
        "status": False,
        "chave": None,
        "msg": None,
        "erro_operacao": False
    }
    browser = abrir_navegador(config.SIMPLES_URL)
    try:
        logger.info("Acessando menu do simples")
        browser.click_element_when_visible(generico.SIMPLES_SERVICOS)
        browser.click_element_when_visible(generico.CRIAR_CHAVE)
        browser.wait_until_element_is_visible(generico.INPUT_CNPJ)
        browser.input_text(generico.INPUT_CNPJ, dados.cnpj)
        browser.input_text(generico.INPUT_CPF, dados.cpf)

        captcha = quebra_captcha(browser)

        if not captcha.get("status"):
            resultado['msg'] = (
                f"Erro ao quebrar captcha. Detalhes: {captcha.get('msg')}")
            resultado["erro_operacao"] = True
            return resultado

        error = erro_de_acesso(browser)
        if error:
            resultado["msg"] = error
            return resultado

        recibo = browser.is_element_visible(generico.INPUT_RECIBO)
        titulo = browser.is_element_visible(generico.INPUT_TITULO)
        if recibo:
            for reci in dados.recibo_irpf:
                browser.input_text(generico.INPUT_RECIBO, reci)
                captcha = quebra_captcha(browser)
                if not captcha.get("status"):
                    resultado['msg'] = resultado['msg'] = (
                        f"Erro ao quebrar captcha. Detalhes: {captcha.get('msg')}")
                    resultado["erro_operacao"] = True
                    return resultado
                error = erro_de_acesso(browser)
                if error:
                    resultado["msg"] = error
                    continue

        elif titulo:
            for titu in dados.titulo_eleitoral:
                browser.input_text(generico.INPUT_TITULO, titu)
                browser.press_keys(generico.INPUT_NASCIMENTO,
                                   dados.data_nascimento)
                captcha = quebra_captcha(browser)

                if not captcha.get("status"):
                    resultado['msg'] = resultado['msg'] = (
                        f"Erro ao quebrar captcha. Detalhes: {captcha.get('msg')}")
                    resultado["erro_operacao"] = True
                    return resultado

                error = erro_de_acesso(browser)
                if error:
                    resultado["msg"] = error
                    continue
        if browser.is_element_visible(generico.TEXT_CHAVE):
            chave = browser.get_text(generico.TEXT_CHAVE)
            if chave:
                logger.info(
                    f"Chave de acesso criada com sucesso para o CNPJ: {dados.cnpj}")
                resultado['status'] = True
                resultado['chave'] = chave
        return resultado
    except Exception as e:
        logger.error(
            f"Erro ao gerar chave de acesso para o CNPJ {dados.cnpj}. Detalhes: {e}")
        resultado['msg'] = str(e)
        resultado["erro_operacao"] = True
        return resultado
    finally:
        browser.close_browser()


def criar_chave(dados: CriaChave):
    try:
        resultado = gerar_chave(dados)
        chave = RetornaChave(
            dados=dados,
            status=resultado['status'],
            chave=resultado['chave'],
            msg=resultado['msg'],
            erro_operacao=resultado['erro_operacao']
        )
        return chave
    except Exception as e:
        logger.error(f"Erro na operação. Detalhes: {e}")
        chave = RetornaChave(
            dados=dados,
            status=False,
            msg=str(e),
            erro_operacao=True
        )
        return chave
