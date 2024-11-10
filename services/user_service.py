import uuid

class UserService:
    def __init__(self, db_service):
        self.db_service = db_service  # Inject db_service to handle database interactions

    def check_or_add_tenant(self, chat_id, name):
        """Checks if the tenant exists, otherwise adds them."""
        tenant_id = self.get_tenant_id(chat_id)  # Fetch tenant ID using the new method in UserService
        if not tenant_id:
            print(f"Tenant id does not exists tenant_id")
            # Tenant does not exist, so add them to the database
            self.add_tenant(chat_id, name)  # Add new tenant using the new method in UserService
            return f"Tenant {name} added to the system."
        else:
            print(f"Tenant with chat id already exists {chat_id}")
            return f"Tenant with chat_id {chat_id} already exists."

    def get_user_info(self, chat_id):
        """Fetch user info from the database."""
        user_info = self.get_user_by_chat_id(chat_id)
        if user_info:
            return user_info
        return None
    
    def get_tenant_id(self, chat_id):
        """Fetch tenant ID based on chat_id."""
        cursor = self.db_service.get_cursor()
        cursor.execute("SELECT id FROM tenants WHERE chat_id = ?", (chat_id,))
        result = cursor.fetchone()
        return result[0] if result else None

    def add_tenant(self, chat_id, name):
        """Add a new tenant to the database."""
        cursor = self.db_service.get_cursor()
        cursor.execute("INSERT INTO tenants (id, chat_id, name) VALUES (?, ?, ?)", (str(uuid.uuid4()), chat_id, name))
        self.db_service.conn.commit()

    def get_user_by_chat_id(self, chat_id):
        """Fetch user info by chat ID."""
        cursor = self.db_service.get_cursor()
        cursor.execute("SELECT name FROM tenants WHERE chat_id = ?", (chat_id,))
        result = cursor.fetchone()
        return result if result else None
