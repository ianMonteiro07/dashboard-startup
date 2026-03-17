import requests
import warnings


warnings.filterwarnings("ignore", category=UserWarning, module='urllib3')


class Usuario:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

class Postagem:
    def __init__(self, userId, id, title):
        self.userId = userId
        self.id = id
        self.title = title


def buscar_dados():
    try:
        
        print(" [Sincronizando com API Cloud...] ")
        u_res = requests.get("https://jsonplaceholder.typicode.com/users", timeout=5)
        p_res = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=5)
        c_res = requests.get("https://jsonplaceholder.typicode.com/comments", timeout=5)

        if u_res.status_code == 200:
            return u_res.json(), p_res.json(), c_res.json()
    except Exception as e:
        print(f"Erro de Conexão: {e}")
        return None, None, None


def renderizar_dashboard():
    users_j, posts_j, comms_j = buscar_dados()
    
    if not users_j:
        return

    print("\n" + "="*75)
    print(f"{'ID':<3} | {'COLABORADOR':<20} | {'ÚLTIMO POST':<35} | {'CMTS'}")
    print("-" * 75)

    for u in users_j[:10]: 
       
        user = Usuario(u['id'], u['name'], u['email'])
        
        
        user_post = next((p for p in posts_j if p['userId'] == user.id), None)
        
        if user_post:
            post_obj = Postagem(user_post['userId'], user_post['id'], user_post['title'])
            
            qtd_c = len([c for c in comms_j if c['postId'] == post_obj.id])
            titulo = post_obj.title[:33] + ".."
        else:
            titulo = "Sem postagens"
            qtd_c = 0
            
        print(f"{user.id:<3} | {user.name[:20]:<20} | {titulo:<35} | {qtd_c}")
    
    print("="*75)
    print("Dashboard RESTful v1.0 - Startup Connect")

if __name__ == "__main__":
    renderizar_dashboard()
