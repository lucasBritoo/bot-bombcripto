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


def soltarTodosHerois(perfil_region):

    print('Abrindo menu de herois')
    local = acction.menuHerois(perfil_region)

    if local is None:
        print('Falha ao abrir menu de herois')
        return False

    else:
        sleep(acction.DELAY_MENUS)
        local = acction.iniciarTodos(perfil_region)

        if local is None:
            print('Falha ao clicar em todos os herois')
            return False

        else:
            print('Todos os herois estão soltos')
            sleep(acction.DELAY_MENUS)

            local = acction.fecharMenu(perfil_region)

            if local is None:
                print('Falha ao fechar menu de herois')
                return False

            else:
                print('Entrando no treasure hunt')
                sleep(acction.DELAY_MENUS)

                local = acction.iniciarAventura(perfil_region)
                if local is None:
                    print('Falha ao entrar no treasure hunt')
                    return False

                else:
                    print("Iniciando mineracao")
                    return True


def pararTodosHerois(perfil_region):

    print('Abrindo menu de herois')
    local = acction.menuHerois(perfil_region)

    if local is None:
        print('Falha ao abrir menu de herois')
        return False

    else:
        sleep(acction.DELAY_MENUS)
        local = acction.pararTodos(perfil_region)

        if local is None:
            print('Falha ao clicar em todos os herois')
            return False

        else:
            print('Todos os herois estão parados')
            sleep(acction.DELAY_MENUS)

            local = acction.fecharMenu(perfil_region)

            if local is None:
                print('Falha ao fechar menu de herois')
                return False

            else:
                print("Herois dormindo")
                return True


def voltarMenuPrincipal(perfil_region):

    print('Voltando para o menu principal')

    local = acction.menuPrincipal(perfil_region)

    if local is not None:
        return True

    else:
        print('Erro ao voltar ao menu principal')
        return False
