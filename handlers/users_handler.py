from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from services.user_service import UserService
from services.db_service import DatabaseService

class UserHandler:
    db_service = DatabaseService()
    user_service = UserService(db_service)

    def __init__(self):
        """Initialize the UserHandler with UserService."""
        self.user_service = UserHandler.user_service

    async def handle_user_command(self, update: Update, context: CallbackContext):
        """Handles both /adduser and /getuser commands dynamically."""
        chat_id = update.message.chat_id
        action = context.args[0] if context.args else 'get'
        user_name = update.message.from_user.first_name if action == 'add' else None
        
        if action == 'add':
            response = self.user_service.check_or_add_tenant(chat_id, user_name)
        elif action == 'get':
            user_info = self.user_service.get_user_info(chat_id)
            print(user_info)
            if user_info:
                response = f"User info:\nName: {user_info[0]}"
            else:
                response = "User not found."

        await update.message.reply_text(response)


    @staticmethod
    def get_handler_add_user():
        """Returns the CommandHandler for /adduser."""
        user_handler = UserHandler()
        return CommandHandler("adduser", user_handler.handle_user_command)

    @staticmethod
    def get_handler_get_user():
        # TODO: Handle this will be valid only for the admin 
        """Returns the CommandHandler for /getuser."""
        user_handler = UserHandler()
        return CommandHandler("getuser", user_handler.handle_user_command)
