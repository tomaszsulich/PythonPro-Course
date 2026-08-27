from aiohttp import web


def setup_routes(app: web.Application, create_user, get_users,
                 create_product, get_products, get_product,
                 update_product, delete_product, transfer, mock_chat):
    """Rejestruje wszystkie trasy aplikacji."""
    app.router.add_post("/users", create_user)
    app.router.add_get("/users", get_users)
    
    # Task 9 (challenge) - tworzenie produktu
    app.router.add_post("/products", create_product)
    
    # Task 10 (challenge) - pobieranie listy produktów
    app.router.add_get("/products", get_products)
    
    # Task 11 (challenge) - pobieranie pojedynczego produktu
    app.router.add_get("/products/{id}", get_product)
    
    # Task 14 (challenge) - aktualizacja produktu
    app.router.add_patch("/products/{id}", update_product)
    
    # Task 15 (challenge) - usuwanie produktu
    app.router.add_delete("/products/{id}", delete_product)
    
    # Task 16 (challenge) - transfer środków
    app.router.add_post("/transfer", transfer)
    
    # Task 18 (challenge) - mock API dla AI
    app.router.add_post("/api/v1/chat", mock_chat)    