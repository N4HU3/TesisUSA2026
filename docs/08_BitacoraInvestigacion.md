# Bitácora de investigación

## Entrada 001 — Configuración de notificaciones Telegram pendiente

- Intento: habilitar notificaciones de progreso vía Telegram para el proyecto
  `TesisUSA2026`.
- Acción realizada:
  - Búsqueda en el repositorio de variables `TELEGRAM_BOT_TOKEN` y
    `TELEGRAM_CHAT_ID` en archivos `.env`, `config*`, `README` y `docs`.
  - No se encontraron credenciales configuradas.
  - Creado script `scripts/notify_telegram.py` para enviar mensajes mediante
    la API de Telegram, y documentación en `docs/09_NotificacionesTelegram.md`.
- Limitación actual:
  - Sin los valores reales de `TELEGRAM_BOT_TOKEN` y `TELEGRAM_CHAT_ID`,
    no es posible enviar notificaciones reales todavía.
- Próximo paso requerido:
  - Definir estas variables de entorno en la máquina de desarrollo o como
    secretos en GitHub Actions.
