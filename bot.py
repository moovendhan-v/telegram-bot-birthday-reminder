from telegram.ext import Application
from config import TOKEN
from handlers.start_handler import StartHandler
from handlers.users_handler import UserHandler
from handlers.birthday_handler import BirthdayHandler
from handlers.help_handler import HelpHandler

def main():
    """Main entry point for the bot."""
    # Create the Application object
    application = Application.builder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(StartHandler.get_handler())
    application.add_handler(UserHandler.get_handler_get_user())
    application.add_handler(BirthdayHandler.get_handler_add_birthday())
    application.add_handler(BirthdayHandler.get_handler_list_birthdays())
    application.add_handler(HelpHandler.get_handler())

    # Start polling for updates (this listens for messages)
    application.run_polling()

if __name__ == '__main__':
    main()
