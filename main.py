import logging, weather_funcs
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm a weather-bot. Enter your coordinates to return current weather or use /forecast command for forecast example: '/forecast 40 44' ")
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coordinates = [float(i) for i in update.message.text.split(' ')]
    await context.bot.send_message(chat_id=update.effective_chat.id, text=weather_funcs.weather_current(*coordinates))
async def forecast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coordinates = [int(i) for i in context.args]
    await context.bot.send_message(chat_id=update.effective_chat.id, text=weather_funcs.weather_forecast(*coordinates))

if __name__ == '__main__':
    application = ApplicationBuilder().token('6227032356:AAGqlpnjuqMt5pFxciUbaiTrVXsQq4qJaG0').build()
    
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler('forecast', forecast )
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    
    application.run_polling()
