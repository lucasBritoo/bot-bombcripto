import acction
from time import sleep


def verificarErro(perfil, perfil_region):

    local = acction.verificarErro(perfil_region)

    if local is not None:
        print('Ocorreu um erro no game. Vamos recarregar a página')
        acction.recarregarPagina(perfil)
        return True

    else:
        return False


def soltarTodosHerois():

    print('Abrindo menu de herois')
    local = acction.menuHerois()

    if local is None:
        print('Falha ao abrir menu de herois')
        return False

    else:
        sleep(acction.DELAY_MENUS)
        local = acction.iniciarTodos()

        if local is None:
            print('Falha ao clicar em todos os herois')
            return False

        else:
            print('Todos os herois estão soltos')
            sleep(acction.DELAY_MENUS)

            local = acction.fecharMenu()

            if local is None:
                print('Falha ao fechar menu de herois')
                return False

            else:
                print('Entrando no treasure hunt')
                sleep(acction.DELAY_MENUS)

                local = acction.iniciarAventura()
                if local is None:
                    print('Falha ao entrar no treasure hunt')
                    return False

                else:
                    print("Iniciando mineracao")
                    return True


def pararTodosHerois():

    print('Abrindo menu de herois')
    local = acction.menuHerois()

    if local is None:
        print('Falha ao abrir menu de herois')
        return False

    else:
        sleep(acction.DELAY_MENUS)
        local = acction.pararTodos()

        if local is None:
            print('Falha ao clicar em todos os herois')
            return False

        else:
            print('Todos os herois estão parados')
            sleep(acction.DELAY_MENUS)

            local = acction.fecharMenu()

            if local is None:
                print('Falha ao fechar menu de herois')
                return False

            else:
                print("Herois dormindo")
                return True


def voltarMenuPrincipal():

    print('Voltando para o menu principal')

    local = acction.menuPrincipal()

    if local is not None:
        print('Menu principal')
        return True

    else:
        print('Erro ao voltar ao menu principal')
        return False
