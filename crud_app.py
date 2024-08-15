import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Função para criar um novo usuário
def create_user(name, email):
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print("User created successfully!")
    except sqlite3.IntegrityError:
        print("Error: Email already exists!")

# Função para ler os usuários
def read_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

# Função para atualizar um usuário
def update_user(user_id, new_name, new_email):
    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (new_name, new_email, user_id))
    conn.commit()
    if cursor.rowcount > 0:
        print("User updated successfully!")
    else:
        print("User not found!")

# Função para deletar um usuário
def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print("User deleted successfully!")
    else:
        print("User not found!")

# Menu simples para o CRUD
def menu():
    while True:
        print("\n1. Create User")
        print("2. Read Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            create_user(name, email)
        elif choice == '2':
            read_users()
        elif choice == '3':
            user_id = int(input("Enter user ID to update: "))
            new_name = input("Enter new name: ")
            new_email = input("Enter new email: ")
            update_user(user_id, new_name, new_email)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    menu()
    conn.close()
