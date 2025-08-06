import pandas as pd
import pyautogui
from time import sleep
import emoji


# 🧾 Carregar a planilha
df = pd.read_excel('teste.xlsx')  # Substitua pelo nome da sua planilha

# 🔁 Iterar sobre cada linha a partir da segunda
for index, row in df.iterrows():
    if index == 0:
        continue  # pula o cabeçalho


    nome = row.iloc[0]  # primeira coluna
    numero = row.iloc[1]  # segunda coluna

    # 💬 Criar mensagem personalizada
    mensagem = f"Essa mensagem é somente deve verificação, não precisa responder! Obrigada"
    pyautogui.keyDown('win')
    pyautogui.keyUp('win')
    sleep(2)
    pyautogui.write('edge')
    sleep(5)
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    sleep(3)
    # 🖱️ Abrir conversa no WhatsApp Web
    link = f"https://web.whatsapp.com/"
    pyautogui.write(link)
    pyautogui.press('enter')
    sleep(20)  # tempo para carregar a página
    mais = pyautogui.locateCenterOnScreen('mais.png')

    pyautogui.click(mais)
    sleep(1)
    pyautogui.write(str(numero))
    sleep(2)
    pyautogui.press('enter')
    sleep(1)


    # 📝 Escrever e enviar mensagem
    pyautogui.write(mensagem)
    sleep(1)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.moveTo(3,3)

    # 🔙 Voltar para a aba anterior (opcional)
    ##pyautogui.hotkey('alt', 'left')
    ## sleep(3)
