from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

class HelpHandler:
    @staticmethod
    async def help_command(update: Update, context: CallbackContext):
        """Handles the /help command."""
        await update.message.reply_text(
            # "/query - Query users based on parameters\n"
            "/addbirthday <name> <YYYY-MM-DD> - Add a friend's birthday\n"
            "/listbirthdays - List all birthdays for your chat"
        )

    @staticmethod
    def get_handler():
        """Returns the CommandHandler for /help."""
        return CommandHandler("help", HelpHandler.help_command)
