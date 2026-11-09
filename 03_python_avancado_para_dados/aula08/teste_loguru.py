#Exemplo 1: Logging Básico
#Este exemplo mostra como fazer logging básico com Loguru, incluindo mensagens de diferentes níveis de severidade.

from loguru import logger

# Mensagens de log de diferentes níveis
logger.debug("Isso é uma mensagem de debug")
logger.info("Isso é uma mensagem informativa")
logger.warning("Isso é um aviso")
logger.error("Isso é um erro")
logger.critical("Isso é crítico")

#Neste exemplo, utilizamos o logger importado do Loguru para registrar mensagens de diferentes níveis de severidade. 
# O Loguru se encarrega de formatar e exibir essas mensagens no console, por padrão.

#Exemplo 2: Configuração de Arquivo de Log
#Aqui, configuramos o Loguru para salvar mensagens de log em um arquivo, incluindo a rotação do arquivo baseada no tamanho.

# Configurando o arquivo de log com rotação de 5MB
logger.add("meu_app.log", rotation="5 MB")

logger.info("Essa mensagem será salva no arquivo")

#No exemplo acima, logger.add() é usado para adicionar um "sink" (destino) que, neste caso, é um arquivo. 
# A opção rotation determina que um novo arquivo será criado sempre que o atual atingir 5MB.

#Exemplo 3: Capturando Exceções com Log
#Loguru também facilita o logging de exceções, capturando automaticamente informações de traceback.

def minha_funcao():
    raise ValueError("Um erro aconteceu!")

try:
    minha_funcao()
except Exception:
    logger.exception("Uma exceção foi capturada")

#Usando logger.exception(), Loguru automaticamente captura e loga o traceback da exceção, o que é extremamente útil para 
# diagnóstico de erros.

def log_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando '{func.__name__}' com {args} e {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"'{func.__name__}' retornou {result}")
            return result
        except Exception as e:
            logger.exception(f"'{func.__name__}' lançou uma exceção: {e}")
            raise
    return wrapper

#Neste decorador, log_decorator, usamos logger.info para registrar quando a função decorada é chamada e o que ela retorna. 
# Se uma exceção for lançada, usamos logger.exception para registrar a exceção, incluindo o traceback.

@log_decorator
def soma(a, b):
    return a + b

@log_decorator
def falha():
    raise ValueError("Um erro intencional")

# Testando as funções decoradas
soma(5, 3)  # Isso irá logar a chamada e o retorno
try:
    falha()  # Isso irá logar a chamada e a exceção
except ValueError:
    pass  # Ignora a exceção para fins de demonstração

#Ao decorar as funções soma e falha com @log_decorator, automaticamente logamos a entrada e saída (ou exceção) dessas 
# funções sem alterar o corpo delas. Isso é especialmente útil para debugar, monitorar a performance de aplicações ou 
# simplesmente manter um registro de quais funções estão sendo chamadas e com quais argumentos.
