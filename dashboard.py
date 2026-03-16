import requests
import warnings


warnings.filterwarnings("ignore", category=UserWarning, module='urllib3')

def carregar_dashboard():
    url_users = "https://jsonplaceholder.typicode.com/users"
    url_posts = "https://jsonplaceholder.typicode.com/posts"

    try:
        print("Buscando dados no servidor (API)...")
        
        
        res_users = requests.get(url_users, timeout=5)
        res_posts = requests.get(url_posts, timeout=5)

        if res_users.status_code == 200:
            usuarios = res_users.json()
            posts = res_posts.json()

            print(f"\n=== DASHBOARD DE COMUNICAÇÃO INTERNA ===")
            print(f"Status: Conectado ao Servidor RESTful")
            
            for user in usuarios[:5]: # 
                print(f"\n[Perfil] Colaborador: {user['name']} ({user['email']})")
                
                
                user_posts = [p for p in posts if p['userId'] == user['id']]
                print(f" > Postagens recentes: {len(user_posts)}")
                
                if user_posts:
                    print(f" > Título do último post: {user_posts[0]['title']}")
        
    except requests.exceptions.Timeout:
        print("\nERRO DE RESILIÊNCIA: O servidor demorou muito a responder (Timeout).")
    except Exception as e:
        print(f"\nERRO INESPERADO: {e}")

if __name__ == "__main__":
    carregar_dashboard()