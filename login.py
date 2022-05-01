import acction
import config
from time import sleep


def conectarMetamask(perfil_region):

    local = acction.loginMetamask(perfil_region)

    if local is None:
        print('Falha ao se conectar com a metamask')
        return False

    else:
        print('Aceitando login na metamask')
        contador = 0

        while contador < config.TRY_METAMASK:

            sleep(config.DELAY_METAMASK)
            local = acction.clickSign(perfil_region)

            if local is not None:
                print('Logado na metamask com sucesso')
                return True

            print('Falha ao logar na metamask. Tentando novamente')
            contador += 1

        print('Falha ao aceitar login na metamask')
        return False


def connect(perfil_region):

    print('Tentando conectar')

    local = acction.login(perfil_region)

    if local is not None:
        sleep(config.DELAY_DEFAULT)
        return True

    return False


def verificarLogin(perfil_region):

    contador = 0
    while contador < config.TRY_LOGIN:
        print('Verificando se a conta está logada')
        local = acction.localizarChave(perfil_region)

        if local is not None:
            return True

        sleep(config.DELAY_LOGIN)
        contador += 1

    return False


def logar(perfil_region):

    condicao = 0
    while condicao < config.TRY_LOGIN:

        if connect(perfil_region):
            print('Realizando login na metamask')

            if conectarMetamask(perfil_region):
                if verificarLogin(perfil_region):
                    print('Podemos comecar a jogatina!!')
                    return True

                else:
                    condicao += 1
            else:
                condicao += 1

        else:
            condicao += 1

    print('0x1 - Problemas ao logar na conta. Recarregando a página.')
    return False


def logarConta(perfil):

    if perfil == 1:
        perfil_region = config.REGION1

    else:
        perfil_region = config.REGION2

    if logar(perfil_region):
        print('Conta logada com sucesso')
        return True

    else:

        if perfil == 1:
            acction.recarregarPagina(config.MID_LOCATION1)

        else:
            acction.recarregarPagina(config.MID_LOCATION2)

    return False
