from time import sleep
from datetime import datetime
import login
import acction
import game


def main():

    logarConta1 = login.logarConta(1)
    # logarConta2 = login.logarConta(2)

    # iniciar = 0

    # logarConta()

    # print("Finalizado com sucesso")

    # print('Iniciando verificacao por tempo')

    # while True:

    #     if verificaErro():
    #         recarregarPagina()
    #         logarConta()

    #     else:

    #         if iniciar == 0:
    #             minuto = int(datetime.now().strftime('%M'))
    #             iniciar = 1

    #         else:
    #             sleep(60)
    #             minuto_atual = int(datetime.now().strftime('%M'))

    #             if (minuto_atual - minuto) >= 5 or (minuto_atual - minuto) < 0:
    #                 minuto = datetime.now().strftime('%M')

    #                 print('Irei soltar novamente os herois')

    #                 menuPrincipal()
    #                 menuPrincipal()

    #                 soltarTodosHerois()
    #                 soltarTodosHerois()
if __name__ == '__main__':
    main()
