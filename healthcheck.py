import psutil
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import schedule
import time
import requests

# Configurações
EMAIL_FROM = "seu_email@gmail.com"
EMAIL_TO = "destino_email@gmail.com"
EMAIL_PASS = "sua_senha_app"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

TELEGRAM_TOKEN = "seu_token_telegram"
TELEGRAM_CHAT_ID = "seu_chat_id"

def enviar_email(assunto, corpo):
    msg = MIMEText(corpo)
    msg['Subject'] = assunto
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_FROM, EMAIL_PASS)
    server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    server.quit()

def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": mensagem}
    requests.post(url, data=data)

def checar_recursos():
    cpu = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory().percent
    disco = psutil.disk_usage('/').percent
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    relatorio = f"""Relatório de Recursos - {now}
CPU: {cpu}%
Memória: {memoria}%
Disco: {disco}%
"""

    print(relatorio)

    alertas = []
    if cpu > 80:
        alertas.append(f"⚠️ CPU alta: {cpu}%")
    if memoria > 80:
        alertas.append(f"⚠️ Memória alta: {memoria}%")
    if disco > 90:
        alertas.append(f"⚠️ Disco quase cheio: {disco}%")

    enviar_email(f"Relatório diário de recursos - {now}", relatorio)

    if alertas:
        enviar_telegram("\n".join(alertas))

def job():
    print("Iniciando health check...")
    checar_recursos()
    print("Health check concluído.")

# Agendamento para rodar todo dia às 08:00
schedule.every().day.at("08:00").do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)
