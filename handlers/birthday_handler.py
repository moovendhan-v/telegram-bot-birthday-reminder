from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from services.db_service import DatabaseService
from services.birthday_service import BirthdayService
from handlers.users_handler import UserHandler
from services.user_service import UserService

class BirthdayHandler:
    db_service = DatabaseService()
    user_service = UserService(db_service)
    birthday_service = BirthdayService(db_service)
    
    def __init__(self):
        """Initialize UserHandler with the user service and other services."""
        self.user_handler = UserHandler(self.db_service)

    @staticmethod
    async def add_birthday(update: Update, context: CallbackContext):
        """Handles the /addbirthday command to store a friend's birthday."""
        chat_id = update.message.chat_id
        print(chat_id)
        try:
            friend_name, birthday = context.args
            
            BirthdayHandler.user_service.check_or_add_tenant(chat_id, update.message.chat.first_name)
            
            BirthdayHandler.birthday_service.add_birthday(chat_id, friend_name, birthday)
            
            await update.message.reply_text(f"Birthday added for {friend_name} on {birthday}.")
        except ValueError:
            await update.message.reply_text("Please provide a name and birthday in the format: /addbirthday <name> <YYYY-MM-DD>.")
        
        except Exception as error:
            await update.message.reply_text("An unexpected error occurred. Please try again later.")
            print(f"Unexpected error: {error}")

    @staticmethod
    async def list_birthdays(update: Update, context: CallbackContext):
        """Handles the /listbirthdays command to retrieve all birthdays."""
        chat_id = update.message.chat_id
        print(chat_id)
        birthdays = BirthdayHandler.birthday_service.get_birthdays(chat_id)
        if birthdays:
            birthday_list = "\n".join([f"{name}: {birthday}" for name, birthday in birthdays])
            await update.message.reply_text(f"Here are the birthdays:\n{birthday_list}")
        else:
            await update.message.reply_text("No birthdays found.")

    @staticmethod
    def get_handler_add_birthday():
        return CommandHandler("addbirthday", BirthdayHandler.add_birthday)

    @staticmethod
    def get_handler_list_birthdays():
        return CommandHandler("listbirthdays", BirthdayHandler.list_birthdays)
