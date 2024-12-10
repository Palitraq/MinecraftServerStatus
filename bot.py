import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from config import TELEGRAM_BOT_TOKEN, MINECRAFT_SERVER_IP, MINECRAFT_SERVER_PORT

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# Создаем клавиатуру с кнопками
def get_keyboard():
    keyboard = [
        ['О боте', 'Проверить онлайн', '🤘Heavy Metal🤘']
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Добро пожаловать! Я - многофункциональный бот-помощник by gladiatorbleid.\n\n'
        'Нажми кнопку "Проверить онлайн" чтоб посмотреть текущий онлайн на сервере',
        parse_mode='Markdown',
        reply_markup=get_keyboard()
    )


async def check_server(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        from mcstatus import JavaServer
        server = JavaServer(MINECRAFT_SERVER_IP, MINECRAFT_SERVER_PORT)

        # Get status
        status = server.status()
        players_online = status.players.online
        max_players = status.players.max

        # Create message
        msg = f"Статус сервера: 🟢 Онлайн\n"
        msg += f"Игроков онлайн: {players_online}/{max_players}"

        if players_online > 0 and hasattr(status.players, 'sample') and status.players.sample:
            msg += "\n\nНики игроков:"
            for player in status.players.sample:
                msg += f"\n• {player.name}"

        await update.message.reply_text(msg, reply_markup=get_keyboard())

    except Exception as e:

        await update.message.reply_text("Статус сервера: 🔴 Оффлайн\nСервер недоступен или выключен",
                                        reply_markup=get_keyboard())


async def heavymetal2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("НА ВСЕХ ЭКРАНАХ", reply_markup=get_keyboard())


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Обрабатываем команды кнопок только для текстовых сообщений
    if update.message.text:
        text = update.message.text
        if text == 'О боте':
            await start(update, context)
        elif text == 'Проверить онлайн':
            await check_server(update, context)
        elif text == '🤘Heavy Metal🤘':
            await heavymetal2(update, context)


if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('check', check_server))
    application.add_handler(CommandHandler('heavymetal2', heavymetal2))

    application.add_handler(MessageHandler(filters.ALL, message_handler))

    application.run_polling()
