import pyautogui
import time
from screeninfo import get_monitors

pyautogui.PAUSE = 3
pyautogui.FAILSAFE = True

# Abrir o navegador

pyautogui.press('win')
pyautogui.write('Brave') # Meu navegador padrão
pyautogui.press('enter')

# Acessar o twitter

pyautogui.write('Twitter')
pyautogui.press('enter')
time.sleep(15) # Irei pausar o código por 15 segundos para o navegador carregar

# Fazer um tweet

tweet = 'Este tweet foi feito automaticamente com o uso da biblioteca #pyautogui.\n'
github = 'Encontre o código do bot que criou este tweet neste link: https://github.com/Dheovani/Pyautogui'
hashtags = '\n\n#python #dev'
pyautogui.write('n') # A letra 'n' representa o atalho do teclado que cria um novo tweet
time.sleep(3)
pyautogui.write(tweet)
pyautogui.write(github)
pyautogui.write(hashtags)
time.sleep(3)
pyautogui.hotkey('ctrl', 'enter') # Atalho do teclado para enviar o tweet
time.sleep(5)

# Abrir o tweet

pyautogui.hotkey('g', 'p') # Atalho do teclado para acessar meu perfil
time.sleep(5)
pyautogui.press('j') # Atalho do teclado para seguir para o próximo tweet
pyautogui.press('enter')

# Tirar um print do tweet

pyautogui.screenshot('tweet.png')

# Copiar o link desse tweet

pyautogui.hotkey('ctrl', 'l') # Atalho do teclado para copiar um link
pyautogui.hotkey('ctrl', 'x')
for monitors in get_monitors():
    screen_height = monitors.height
    screen_width = monitors.width
pyautogui.click(screen_width, screen_height) # Estamos minimizando todas as janelas
# Através da lixeira, vamos buscar o repositório local do GitHub onde está o código desse bot
pyautogui.write('lixeira')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'e') # Atalho do teclado para abrir a aba de pesquisa
pyautogui.press('tab')
for b in range(7):
    pyautogui.press('down')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.write('Pyautogui')
pyautogui.press('enter')
pyautogui.write('links')
pyautogui.press('enter')
time.sleep(5)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 's')
pyautogui.hotkey('ctrl', 'w')
