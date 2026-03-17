import tkinter as tk
from tkinter import messagebox, ttk
import requests
import warnings

# Silenciar avisos de certificados
warnings.filterwarnings("ignore", category=UserWarning, module='urllib3')

# --- MODEL (Suas Classes de Domínio) ---
class Usuario:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

class Postagem:
    def __init__(self, userId, id, title, body):
        self.userId = userId
        self.id = id
        self.title = title
        self.body = body

class Comentario:
    def __init__(self, postId, id, name, body):
        self.postId = postId
        self.id = id
        self.name = name
        self.body = body

# --- VIEW & CONTROLLER (Interface Gráfica) ---
class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Startup Connect - Dashboard Interno")
        self.root.geometry("700x500")

        # Elementos Visuais
        tk.Label(root, text="Dashboard de Comunicação Interna", font=("Arial", 16, "bold")).pack(pady=10)
        
        self.btn_carregar = tk.Button(root, text="Sincronizar Dados da API", command=self.carregar_dados, 
                                      bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=20)
        self.btn_carregar.pack(pady=5)

        # Tabela (Treeview)
        self.tree = ttk.Treeview(root, columns=("Usuario", "Email", "Post", "Comentarios"), show="headings")
        self.tree.heading("Usuario", text="Colaborador")
        self.tree.heading("Email", text="E-mail")
        self.tree.heading("Post", text="Último Post")
        self.tree.heading("Comentarios", text="Comentários")
        
        # Ajuste de largura das colunas
        self.tree.column("Usuario", width=150)
        self.tree.column("Email", width=150)
        self.tree.column("Post", width=250)
        self.tree.column("Comentarios", width=100, anchor="center")
        
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.status_label = tk.Label(root, text="Status: Aguardando Sincronização", fg="gray")
        self.status_label.pack(side=tk.BOTTOM, pady=5)

    def carregar_dados(self):
        try:
            self.status_label.config(text="Buscando dados na API RESTful...", fg="blue")
            self.root.update()

            # Consumo da API (GET) com Timeout (Resiliência)
            res_users = requests.get("https://jsonplaceholder.typicode.com/users", timeout=5)
            res_posts = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=5)
            res_comments = requests.get("https://jsonplaceholder.typicode.com/comments", timeout=5)

            # Transforma JSON em Listas
            users_data = res_users.json()
            posts_data = res_posts.json()
            comments_data = res_comments.json()

            # Limpa a tabela
            for i in self.tree.get_children():
                self.tree.delete(i)

            # Processamento usando as Classes do Model
            for u in users_data[:8]: 
                # Instancia o Objeto Usuario
                user = Usuario(u['id'], u['name'], u['email'])
                
                # Busca postagem associada (Relacionamento 1:N)
                user_post_raw = next((p for p in posts_data if p['userId'] == user.id), None)
                
                if user_post_raw:
                    post = Postagem(user_post_raw['userId'], user_post_raw['id'], user_post_raw['title'], user_post_raw['body'])
                    # Conta comentários desse post
                    qtd_comments = len([c for c in comments_data if c['postId'] == post.id])
                    titulo_exibicao = post.title[:40] + "..."
                else:
                    titulo_exibicao = "Sem postagens"
                    qtd_comments = 0

                # Insere na View
                self.tree.insert("", tk.END, values=(user.name, user.email, titulo_exibicao, qtd_comments))

            self.status_label.config(text="Status: Dados Sincronizados com Sucesso!", fg="green")

        except requests.exceptions.Timeout:
            messagebox.showerror("Erro de Rede", "Tempo de resposta excedido (Timeout).")
            self.status_label.config(text="Erro: Timeout", fg="red")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao conectar: {e}")
            self.status_label.config(text="Status: Erro de Conexão", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()