from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("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"))

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = client.responses.create(
        model="gpt-5-mini",
        input=update.message.text
    )
    await update.message.reply_text(response.output_text)

app = Application.builder().token(os.getenv("8671296769:AAGYxP49j3L9ij7CYI0q9XipXTfexbJIAeY")).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

app.run_polling()