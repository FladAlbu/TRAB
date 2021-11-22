import logging

log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'

logging.basicConfig(filename='trabalho-comgraf-g2.log',
                    # w -> sobrescreve o arquivo a cada log
                    # a -> não sobrescreve o arquivo
                    filemode='w',
                    level=logging.DEBUG,
                    format=log_format)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def fullname(primeiro_nome: str, segundo_nome: str) -> str:
    """
        Essa função recebe o primeiro nome e o segundo nome de uma pessoa e retorna o nome completo dela.
    """

    # Aqui, verificamos se os parametros passados são do tipo string (str)
    if isinstance(primeiro_nome, str) and isinstance(segundo_nome, str):
        logger.info(f'{primeiro_nome} {segundo_nome}')
        return primeiro_nome + segundo_nome
    else:
        logger.error(
            f'{primeiro_nome} type: {type(primeiro_nome)} - {segundo_nome} type: {type(segundo_nome)}'
        )

fullname('Manu', 'Marques')
fullname('Manu', True)

logging.info('foi quando o user logou')