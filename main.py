from time import sleep
from datetime import datetime
import login
import acction
import game
import config


def logar(perfil):

    accept = 0
    while accept < config.TRY_LOGIN:

        logarConta = login.logarConta(perfil)

        if logarConta:
            return True

        sleep(3)
        accept += 1

    return False


def iniciarJogatina(perfil):

    if perfil == 1:
        region = config.REGION1

    else:
        region = config.REGION2

    accept = 0
    while accept < config.TRY_LOGIN:

        iniciar = game.soltarTodosHerois(region)

        if iniciar:
            return True

        sleep(3)
        accept += 1

    return False


def soltarHerois(region):
    contador = 0

    while contador < config.TRY_MENU:

        if game.voltarMenuPrincipal(region):
            sleep(config.DELAY_MENUS)
            if game.soltarTodosHerois(region):
                sleep(config.DELAY_MENUS)
                return True
        sleep(3)
        contador += 1

    return False


def voltarMenu(region):
    contador = 0
    while contador < config.TRY_MENU:
        if game.voltarMenuPrincipal(region):
            sleep(config.DELAY_MENUS)

            if acction.iniciarAventura(region):
                sleep(config.DELAY_MENUS)
                return True
        sleep(3)
        contador += 1

    return False


def main():

    inicio = 0
    contador = 0
    flag_reload = 0
    while True:

        if inicio == 0:
            if logar(1):
                if game.soltarTodosHerois(config.REGION1):
                    inicio = 1

        elif inicio == 1:
            if logar(2):
                if game.soltarTodosHerois(config.REGION2):
                    inicio = 2

        elif inicio == 2:

            if contador == 0:
                print("Iniciando monitoramento por tempo")
                minuto_menu = int(datetime.now().strftime('%M'))
                minuto_herois = int(datetime.now().strftime('%M'))
                contador = 1

            else:
                minuto_atual = int(datetime.now().strftime('%M'))

                if flag_reload != 0:
                    print(
                        f'Nao foi possivel interagir com a conta {flag_reload}'
                        + '.Reconectand')
                    logar(flag_reload)

                elif ((minuto_atual - minuto_menu) >= config.TIMER_MENU
                        or (minuto_atual - minuto_menu) < 0):
                    minuto_menu = int(datetime.now().strftime('%M'))

                    print('Voltando ao menu principal')

                    if voltarMenu(config.REGION1):
                        flag_reload = 0

                        sleep(3)
                        if voltarMenu(config.REGION2):
                            flag_reload = 0

                        else:
                            flag_reload = 2

                    else:
                        flag_reload = 1

                elif ((minuto_atual - minuto_herois) >= config.TIMER_HEROIS
                      or (minuto_atual - minuto_herois) < 0):
                    minuto_herois = int(datetime.now().strftime('%M'))

                    print('Soltando todos os herois')

                    if soltarHerois(config.REGION1):
                        print("Os herois da conta 1 estao trabalhando")
                        flag_reload = 0

                        sleep(3)
                        if soltarHerois(config.REGION2):
                            print("os herois da conta 2 estao trabalhando")
                            flag_reload = 0
                        else:
                            flag_reload = 2
                    else:
                        flag_reload = 1

        # sleep(60)


if __name__ == '__main__':
    main()
