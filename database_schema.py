# db_schema.py

TENANTS_TABLE = '''
CREATE TABLE IF NOT EXISTS tenants (
    id TEXT PRIMARY KEY,  -- UUID as ID
    chat_id TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL
)
'''

BIRTHDAYS_TABLE = '''
CREATE TABLE IF NOT EXISTS birthdays (
    id TEXT PRIMARY KEY,  -- UUID as ID
    chat_id TEXT NOT NULL,
    tenant_id TEXT,
    friend_name TEXT NOT NULL,
    birthday TEXT NOT NULL,
    FOREIGN KEY (tenant_id) REFERENCES tenants(id)
)
'''
