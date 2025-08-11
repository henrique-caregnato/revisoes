import sqlite3

def conectar():
    conn = sqlite3.connect("sistema.db")
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL         
                )
                """)
    return conn, cur

def adicionar_cliente(cur, conn, nome, email):
    cur.execute("INSERT INTO clientes(nome,email) VALUES (?, ?)", (nome, email))
    conn.commit()
    print("Cliente adicionado")

def visualizar(cur):
    cur.execute("SELECT * FROM clientes")
    for c in cur.fetchall():
        print(c)

def atualizar(cur, conn, id, nome, email):
    cur.execute("UPDATE clientes SET nome=?, email=? WHERE id=?", (nome, email, id))
    conn.commit()
    print("Atualizado")

def remover(cur, conn, id):
    cur.execute("DELETE FROM clientes WHERE id=?", (id, ))
    conn.commit()
    print("Excluindo")
    
def run():
    conn, cur = conectar()
    while True:
        print("\n---Menu--")
        print("1. Adicionar")
        print("2. Visualizar")
        print("3. Atualizar")
        print("4. Remover")
        print("5. Sair")
        opcao = input("Escolha: ").strip()
        try:
            if opcao == "1":
                print("opcao 1 selecionada")
                adicionar_cliente(cur, conn, "Henrique", "hmcaregnato@gmail.com")
            elif opcao == "2":
                visualizar(cur)
            elif opcao == "3":
                atualizar(cur, conn, "2", "Vera", "vera@gmail.com")
            elif opcao == "4":
                id = input("Digite o id: ")
                remover(cur, conn, id)
            elif opcao == "5":
                break
        except Exception as e:
            print(f"Erro {e}")
    conn.close()

