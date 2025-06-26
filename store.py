import sqlite3

def init_db():
    conn = sqlite3.connect("inventory.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    conn = sqlite3.connect("inventory.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                  (username, hash_password(password)))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def login_user(username, password):
    conn = sqlite3.connect("inventory.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", 
              (username, hash_password(password)))
    user = c.fetchone()
    conn.close()
    return user is not None
    def add_product(name, quantity, price):
    conn = sqlite3.connect("inventory.db")
    c = conn.cursor()
    c.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)",
              (name, quantity, price))
    conn.commit()
    conn.close()

def get_low_stock(threshold=5):
    conn = sqlite3.connect("inventory.db")
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE quantity < ?", (threshold,))
    low_stock_items = c.fetchall()
    conn.close()
    return low_stock_items
    import tkinter as tk
from auth import login_user, register_user
from inventory import add_product, get_low_stock

def login_screen():
    root = tk.Tk()
    root.title("Inventory Login")

    tk.Label(root, text="Username").grid(row=0)
    tk.Label(root, text="Password").grid(row=1)
    username = tk.Entry(root)
    password = tk.Entry(root, show='*')
    username.grid(row=0, column=1)
    password.grid(row=1, column=1)

    def attempt_login():
        if login_user(username.get(), password.get()):
            root.destroy()
            dashboard()
        else:
            tk.Label(root, text="Login Failed").grid(row=3, columnspan=2)

    tk.Button(root, text="Login", command=attempt_login).grid(row=2, columnspan=2)
    root.mainloop()

def dashboard():
    win = tk.Tk()
    win.title("Dashboard")

    tk.Label(win, text="Add Product").pack()
    # Add product form, buttons, etc.
    win.mainloop()
