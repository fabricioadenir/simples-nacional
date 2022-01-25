from loguru import logger
import re


class Regex:
    """Retorna uma valor do formato se der match no texto.

    Tipos de dados mapeados:
        Datas no formato:
            - dd/mm/yyyy
            - dd-mm-yyyy
            - yyyy/mm/dd
            - yyyy-mm-dd
        cpf, cnpj

    Caso seja passado o format ele retona se encontrar a data
    no formato fornecido.

    Args:
        text (str): uma string qualquer que contenha em seu conteúdo
        uma data.
        format (str): string com o tipo de formato.

    Returns:
        str: Com o valor encontrado pelo formato passado.
    """

    types_regex = {
        "dd/mm/yyyy": r"\d{2}/\d{2}/\d{4}(?=[^0-9])",
        "dd-mm-yyyy": r"\d{2}-\d{2}-\d{4}(?=[^0-9])",
        "yyyy/mm/dd": r"\d{4}/\d{2}/\d{2}(?=[^0-9])",
        "yyyy-mm-dd": r"\d{4}-\d{2}-\d{2}(?=[^0-9])",
        "cpf": r"(\d{3}.?\d{3}.?\d{3}-?\d{2})",
        "cnpj": r"\d{2}.?\d{3}.?\d{3}/?\d{4}-?\d{2}"
    }

    def __init__(self, text: str, format: str) -> None:
        self.text = text
        self.format = format

    def get_full_value(self) -> str:
        logger.info(f"Buscando por: {self.format} no texto informado.")
        regex = self.types_regex.get(self.format, "")

        mat = re.search(regex, self.text.lower())
        if mat:
            result = mat.group(0)
            logger.info(
                f"{self.format.upper()} encontrado. Detalhes: {result}.")
            return result
        return ""

    def get_value_without_characters(self):
        logger.info(
            f"Buscando por: {self.format} no texto informado. Sem caracteres.")
        value = self.get_full_value()
        new_value = re.sub(r"\W", "", value)

        logger.info(
            f"{self.format.upper()} encontrado. Detalhes: {new_value}.")

        return new_value
