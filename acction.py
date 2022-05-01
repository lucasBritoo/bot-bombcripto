import pyautogui
import config


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

    return pyautogui.locateCenterOnScreen(config.chave, region=perfil_region)


def verificarErro(perfil_region):

    for opcao in config.vet_erro:
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

    return clicar(config.conectar, perfil_region)


def loginMetamask(perfil_region):

    return clicar(config.metamask, perfil_region)


def clickSign(perfil_region):

    return clicar(config.sign, perfil_region)


def menuHerois(perfil_region):

    return clicar(config.herois, perfil_region)


def iniciarTodos(perfil_region):

    return clicar(config.todos_iniciar, perfil_region)


def fecharMenu(perfil_region):
    return clicar(config.fechar_menu, perfil_region)


def iniciarAventura(perfil_region):
    return clicar(config.treasure, perfil_region)


def pararTodos(perfil_region):

    return clicar(config.todos_parar, perfil_region)


def menuPrincipal(perfil_region):
    return clicar(config.voltar_menu, perfil_region)
