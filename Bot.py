import snscrape.modules.twitter as sntwitter
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = 'AAHY45Fc3cP6eCKSRrTmlaPOCxSYTLqyT2A'
TWITTER_ACCOUNT = 'cryptolaixe'
ALERT_KEYWORD = 'pump.fun'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Bot started!')

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for tweet in sntwitter.TwitterSearchScraper(f'from:{TWITTER_ACCOUNT}').get_items():
        if ALERT_KEYWORD in tweet.content:
            await update.message.reply_text(f"Found pump.fun tweet:\n\n{tweet.content}")
            break
    else:
        await update.message.reply_text("Geen pump.fun link gevonden in de laatste tweets.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("check", check))
    
    print("Bot is running...")
    app.run_polling()
