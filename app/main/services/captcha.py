from loguru import logger
import time
import captcha_pc
from anticaptchaofficial.imagecaptcha import *
from app.main.services.locators import generico
from app import config


def anti_captcha(path_image):
    solver = imagecaptcha()
    solver.set_verbose(1)
    solver.set_key(config.ANTI_CPT_TOKEN)
    result = {
        "status": False,
        "msg": ""
    }
    text = solver.solve_and_return_solution(path_image)
    if text != 0:
        result["status"] = True
        result["text"] = text
    else:
        result["msg"] = f"{solver.error_code} {solver.err_string}"
    return result


def prime_captcha_pc(path_image):
    result_captcha = captcha_pc.resolver_captcha_tipo1(
        username=config.CAPTCHA_USER, password=config.CAPTCHA_PASS,
        imagem=path_image, timeout=30
    )
    return result_captcha


def resolve_captcha(path_image):
    result_captcha = prime_captcha_pc(path_image)
    if result_captcha.get("status") and result_captcha.get("text"):
        return result_captcha
    else:
        logger.error(
            f"Erro ao resolver captcha. Detalhes: {result_captcha.get('msg')}")

    result_anti_captcha = anti_captcha(path_image)
    if result_anti_captcha.get("status") and result_anti_captcha.get("text"):
        return result_anti_captcha
    else:
        logger.error(
            f"Erro ao resolver captcha. Detalhes: {result_anti_captcha.get('msg')}")

    msg_capt = result_captcha.get("msg")
    msg_anti = result_anti_captcha.get("msg")
    result = {
        "status": False,
        "text": "",
        "msg": (f"Erro ao resolver captcha. "
                f"Death By Captcha: {msg_capt} | Anti-Captcha: {msg_anti}")
    }
    return result


def quebra_captcha(bw, chave=None):
    logger.info("Quebrando captcha...")

    if chave:
        bw.input_text(generico.INPUT_CHAVE, chave, clear=True)

    bw.click_element(generico.CAPTCHA_INPUT)
    outputdir = fr"{config.ROOT}\output\captcha.png"
    bw.wait_until_element_is_visible(generico.CAPTCHA_IMAGE)
    bw.capture_element_screenshot(generico.CAPTCHA_IMAGE,
                                  outputdir)

    result_captcha = resolve_captcha(outputdir)
    if result_captcha.get("status") and result_captcha.get("text"):
        text_captcha = result_captcha.get("text")
        logger.info(f"Valor do CAPTCHA: {text_captcha}")
    else:
        return result_captcha

    bw.press_keys(generico.CAPTCHA_INPUT, text_captcha)

    time.sleep(1.5)
    if bw.is_element_visible(generico.BUTTON_VALIDAR):
        bw.click_element_when_visible(generico.BUTTON_VALIDAR, modifier=False)

    elif bw.is_element_visible(generico.BUTTON_CONTINUAR):
        bw.click_element_when_visible(
            generico.BUTTON_CONTINUAR, modifier=False)

    if bw.is_element_visible(generico.ERRO_CAPTCHA):
        logger.warning(
            "Erro na tentativa de quebrar o captcha. Tentando novamente.")
        bw.click_element(generico.ELEMENT_VOLTAR)
        bw.clear_element_text(generico.CAPTCHA_INPUT)
        quebra_captcha(bw, chave)
    return result_captcha
