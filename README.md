# Python Health Check para Infraestrutura

Este projeto automatiza o monitoramento diário de recursos do servidor (CPU, memória e disco), enviando relatórios por e-mail e alertas via Telegram para facilitar a gestão e evitar problemas antes que aconteçam.

---

## Funcionalidades

- Monitoramento de CPU, memória e uso de disco  
- Relatório diário automático enviado por e-mail  
- Alertas em tempo real via Telegram se algum recurso ultrapassar limites críticos  
- Agendamento automático para rodar todo dia às 08:00 da manhã  

---

## Tecnologias usadas

- Python 3  
- [psutil](https://pypi.org/project/psutil/)  
- [schedule](https://pypi.org/project/schedule/)  
- smtplib (envio de e-mail)  
- requests (API do Telegram Bot)  

---

## Como usar

1. Clone o repositório:  
```bash
git clone https://github.com/chagasleandro/python-healthcheck-infra.git
cd python-healthcheck-infra
```

2. Instale as dependências:  
```bash
pip install psutil schedule requests
```

3. Configure as variáveis no arquivo `healthcheck.py`:
- EMAIL_FROM: seu e-mail remetente (Gmail recomendado)  
- EMAIL_TO: e-mail que receberá o relatório  
- EMAIL_PASS: senha de app do Gmail (não sua senha normal)  
- TELEGRAM_TOKEN: token do seu bot Telegram  
- TELEGRAM_CHAT_ID: seu chat ID no Telegram  

4. Execute o script:  
```bash
python healthcheck.py
```

---

## Exemplo de relatório enviado

```
Relatório de Recursos - 2025-05-20 08:00:00
CPU: 35%
Memória: 45%
Disco: 70%
```

---

## Contato

Leandro Chagas  
[LinkedIn](https://www.linkedin.com/in/leandro-chagas-)  
leandrosrs2012@gmail.com
