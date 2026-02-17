# Notificaciones de progreso por Telegram

Este proyecto incluye un script simple para enviar notificaciones de progreso
de la tesis al chat de Telegram del autor.

## 1. Variables de entorno necesarias

Defina las siguientes variables de entorno en el entorno donde ejecute
los comandos (por ejemplo, en un `.env` local, en su shell, o como secrets
en GitHub Actions):

- `TELEGRAM_BOT_TOKEN`: token del bot de Telegram.
- `TELEGRAM_CHAT_ID`: ID del chat (usuario o grupo) donde se enviarán
  las notificaciones.

## 2. Script de notificación

El script se encuentra en:

- `scripts/notify_telegram.py`

Uso básico desde la raíz del repositorio:

```bash
export TELEGRAM_BOT_TOKEN="<tu_token>"
export TELEGRAM_CHAT_ID="<tu_chat_id>"

./scripts/notify_telegram.py "[TesisUSA2026] 🔔 Notificaciones Telegram activas."
```

El mensaje se envía usando la API oficial de Telegram (`sendMessage`) con
`parse_mode=Markdown`.

## 3. Errores comunes

- Si no se definen las variables de entorno, el script termina con código
  de salida `2` y muestra un mensaje indicando la falta de configuración.
- Si hay un error de red o en la API de Telegram, se mostrará el error en
  `stderr` y el script terminará con código de salida `3`.

## 4. Integración futura (opcional)

Se puede crear un workflow de GitHub Actions para notificar automáticamente
cuando haya commits relevantes o releases, utilizando los secretos
`TELEGRAM_BOT_TOKEN` y `TELEGRAM_CHAT_ID` configurados en el repositorio.
