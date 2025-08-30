import requests
import time
import telebot

# ==== CONFIGURAÇÕES ====
TOKEN = "8071037304:AAFiP1O1x5puoRbZ4FIci_ECQJdUMW4vba4"
CHAT_ID = "6209409362"

# Link da página que vamos monitorar
URL = "https://visa.vfsglobal.com/ago/en/prt/application-detail"

# Mensagens que indicam indisponibilidade
MENSAGEM_SEM_VAGAS = "We are sorry but no appointment slots are currently available."

# Inicializa o bot
bot = telebot.TeleBot(TOKEN)

def verificar_vagas():
    try:
        r = requests.get(URL, timeout=10)
        r.raise_for_status()
        conteudo = r.text

        if MENSAGEM_SEM_VAGAS in conteudo:
            print("Sem vagas no momento...")
            return False
        else:
            print("⚠️ POSSÍVEL VAGA DETECTADA!")
            bot.send_message(CHAT_ID, "🚨 ATENÇÃO: Pode haver vagas disponíveis! Verifique no site agora!")
            return True

    except Exception as e:
        print("Erro ao acessar:", e)
        bot.send_message(CHAT_ID, f"❌ Erro ao acessar o site: {e}")
        return False

if __name__ == "__main__":
    bot.send_message(CHAT_ID, "🤖 Bot iniciado e monitorando vagas da VFS...")
    while True:
        verificar_vagas()
        time.sleep(60)  # Verifica a cada 1 minuto
