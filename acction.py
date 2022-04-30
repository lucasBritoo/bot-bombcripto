import pyautogui
import os

caminho = r'/home/brito/Documents/bot/bombcripto/Imagens/'
os.chdir(caminho)
conectar = './conectar.png'
metamask = './metamask.png'
sign = './sign.png'
ok = './ok.png'
chave = './chave.png'
recarregar = './recarregar.png'
herois = './herois.png'
treasure = './treasure.png'
todos_parar = './todos_parar.png'
todos_iniciar = './todos_iniciar.png'
fechar_menu = './fechar_menu.png'
voltar_menu = './voltar_menu.png'
vida = './vida1.png'
barra = './barra.png'
work = './work.png'

vet_erro = [ok]

MID_LOCATION1 = [2384, 268]
MID_LOCATION2 = [2989, 352]

REGION1 = [1998, 4, 2652, 749]
REGION2 = [2652, 10, 3269, 756]

REGION_CONTA1 = (2128, 229, 2336, 255)
NUMERO_HEROIS = 15

DELAY_DEFAULT = 0.5
DELAY_METAMASK = 1.5
DELAY_LOGIN = 10
DELAY_RELOAD = 5
DELAY_MENUS = 5

TRY_METAMASK = 5
TRY_LOGIN = 5


def verificarPositiao():
    x, y = pyautogui.position()
    print(f'x: {x} Y:{y}')


def clicar(imagem, perfil_region):
    local = pyautogui.locateCenterOnScreen(imagem, region=perfil_region)

    if local is not None:
        pyautogui.moveTo(local, duration=0.2)
        pyautogui.click()

    return local


def localizarChave(perfil_region):

    return pyautogui.locateCenterOnScreen(chave, region=perfil_region)


def verificarErro(perfil_region):

    for opcao in vet_erro:
        erro = pyautogui.locateAllOnScreen(opcao, region=perfil_region)

        if erro is not None:
            break

    return erro


def recarregarPagina(midLocation):

    pyautogui.moveTo(midLocation, duration=0.2)
    pyautogui.click()
    pyautogui.keyDown('CTRL')
    pyautogui.press('F5')
    pyautogui.keyUp('CTRL')


def login(perfil_region):

    return clicar(conectar, perfil_region)


def loginMetamask(perfil_region):

    return clicar(metamask, perfil_region)


def clickSign(perfil_region):

    return clicar(sign, perfil_region)


def menuHerois(perfil_region):

    return clicar(herois, perfil_region)


def iniciarTodos(perfil_region):

    return clicar(todos_iniciar, perfil_region)


def fecharMenu(perfil_region):
    return clicar(fechar_menu, perfil_region)


def iniciarAventura(perfil_region):
    return clicar(treasure, perfil_region)


def pararTodos(perfil_region):

    return clicar(todos_parar, perfil_region)


def menuPrincipal(perfil_region):
    return clicar(voltar_menu, perfil_region)
