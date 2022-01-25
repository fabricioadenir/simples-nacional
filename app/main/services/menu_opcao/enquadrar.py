from loguru import logger
from app.main.services.browser import abrir_navegador

from app.main.schemas.enquadramento import (
    SolicitarEnquadramento, RetornarEnquadramento)
from app import config
from app.main.services.locators import generico
from app.main.services.captcha import quebra_captcha
from app.main.services.my_regex import Regex


def get_data_resultado(browser):
    browser.wait_until_element_is_visible(
        generico.ELEMENT_TEXT_DT, timeout=config.TIMEOUT)
    texto_dt = browser.get_text(generico.ELEMENT_TEXT_DT)
    regex = Regex(texto_dt, format="dd/mm/yyyy")
    dt_resultado = regex.get_full_value()
    logger.info(f"Data de resultado capturada. Data: {dt_resultado}")
    return dt_resultado


def enquadrar_cnpj(dados: SolicitarEnquadramento):
    resultado = {
        "status": False,
        "data": None,
        "msg": None,
        "erro_operacao": False
    }
    browser = abrir_navegador(config.SIMPLES_URL)
    try:
        logger.info("Acessando menu de enquadramento.")
        browser.click_element_when_visible(generico.SIMPLES_SERVICOS)
        browser.click_element_when_visible(generico.ELEMENT_ENQUADRAR)
        browser.wait_until_element_is_visible(generico.INPUT_CNPJ)
        browser.input_text(generico.INPUT_CNPJ, dados.cnpj)
        browser.input_text(generico.INPUT_CPF, dados.cpf)

        captcha = quebra_captcha(browser, dados.chave)

        if not captcha.get("status"):
            resultado['msg'] = (
                f"Erro ao quebrar captcha. Detalhes: {captcha.get('msg')}")
            resultado["erro_operacao"] = True
            return resultado

        error = browser.is_element_visible(
            generico.ELEMENT_ERROR_DADOS_ENQUADRAR)
        if error:
            msg_error = browser.get_text(
                generico.ELEMENT_ERROR_DADOS_ENQUADRAR)
            resultado["msg"] = msg_error
            return resultado

        error = browser.is_element_visible(generico.ELEMENT_ERROR)
        mensagem = browser.get_text(generico.ELEMENT_ERROR) if error else ''
        if browser.is_element_visible(generico.ELEMENT_AVISO):
            mensagem = browser.get_text(generico.ELEMENT_AVISO)
            resultado["msg"] = mensagem
            return resultado
        elif browser.is_element_visible(generico.ELEMENT_IFRAME):
            browser.select_frame(generico.ELEMENT_IFRAME)
            if browser.is_element_visible(generico.ELEMENT_MENSAGEM):
                mensagem = browser.get_text(generico.ELEMENT_MENSAGEM)
                if mensagem in generico.mensagem_ja_enquadrou:
                    logger.info("CNPJ já enquadrado, pegando resultado...")
                    browser.click_element_when_visible(
                        generico.ELEMENT_ACOMPANHAMENTO)
                    dt_resultado = get_data_resultado(browser)
                    resultado['status'] = True
                    resultado['data'] = dt_resultado
                    return resultado
                resultado['msg'] = mensagem
                return resultado

            browser.click_element_when_visible(generico.ELEMENT_CONFIRMAR)
            browser.click_element_when_visible(generico.ELEMENT_ACEITAR)
            # TODO criar nova versão em casos de mudança no site so simples, hoje fazemos um merge no futuro deve ser feito uma versão.
            # browser.press_keys(generico.ELEMENT_DT_CNPJ,
            #                    dados.data_cnpj)
            # browser.click_element_when_visible(generico.ELEMENT_CONFIRMAR_DT)
            if browser.is_element_visible(generico.ELEMENT_INICIO_ATIVIDADE):
                browser.click_element_when_visible(
                    generico.ELEMENT_INICIO_ATIVIDADE)
            if browser.is_element_visible(generico.ELEMENT_SALVAR):
                browser.click_element_when_visible(generico.ELEMENT_SALVAR)
            else:
                msg = browser.get_text(generico.ELEMENT_TEXT_DT)
                resultado["status"] = False
                resultado["msg"] = msg
                return resultado
            dt_resultado = get_data_resultado(browser)
            resultado['status'] = True
            resultado['data'] = dt_resultado
            return resultado
        if any(mensagem in s for s in generico.mensagens):
            logger.warning(
                f"Enquadramento gerou uma mensagem de aviso: {mensagem}")
            resultado['msg'] = mensagem

        return resultado

    except Exception as e:
        logger.error(f"Erro ao tentar enquadrar. Detalhes: {e}")
        resultado['msg'] = str(e)
        resultado["erro_operacao"] = True
        return resultado
    finally:
        browser.close_browser()


def enquadrar(dados: SolicitarEnquadramento):
    try:
        resultado = enquadrar_cnpj(dados)
        if resultado.get("status"):
            logger.info(
                f"Enquadramento solicitado com sucesso para o CNPJ: {dados.cnpj}")

        enquadramento = RetornarEnquadramento(
            dados=dados,
            status=resultado['status'],
            data_resultado=resultado['data'],
            msg=resultado['msg'],
            erro_operacao=resultado['erro_operacao']
        )
        return enquadramento
    except Exception as e:
        logger.error(f"Erro enquadrar o CNPJ {dados.cnpj}. Detalhes: {e}")
        enquadramento = RetornarEnquadramento(
            dados=dados,
            status=False,
            data_resultado=None,
            msg=str(e),
            erro_operacao=True
        )
        return enquadramento
