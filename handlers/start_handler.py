from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from services.user_service import UserService
from services.db_service import DatabaseService

class StartHandler:
    @staticmethod
    async def start(update: Update, context: CallbackContext):
        """Handles the /start command by adding the tenant if they are new."""
        chat_id = update.message.chat_id
        user_name = update.message.from_user.first_name 

        db_service = DatabaseService()
        cursor = db_service.get_cursor()
        user_service = UserService(db_service)

        response = user_service.check_or_add_tenant(chat_id, user_name)
        
        await update.message.reply_text(
            f"Hello, {user_name}! 👋\n\n"
            "I am your bot! 🎉 Here’s what I can do for you:\n\n"
            "1️⃣ Save your friends' birthday details 🗓️\n"
            "2️⃣ Alert you when a friend's birthday is coming up 🎂\n\n"
            "Just type /help to see all available commands!"
        )

    @staticmethod
    def get_handler():
        """Returns the CommandHandler for /start."""
        return CommandHandler("start", StartHandler.start)
