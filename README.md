## ✨ Funcionalidades del Backend

Este proyecto implementa una API RESTful desarrollada con **FastAPI** y **SQLModel** que cumple con todos los requisitos de la prueba técnica. A continuación, se detallan las funcionalidades disponibles:

### 👤 Usuarios
- `POST /api/users`: Registrar un nuevo usuario
- `POST /api//users/login`: Iniciar sesión y obtener un token JWT
- `GET /api//users/me`: Obtener el perfil del usuario autenticado
- `PUT /api//users/me`: Actualizar nombre, correo o contraseña
- `DELETE /api//users/me`: Eliminar cuenta del usuario autenticado

### 🛒 Productos
- `POST /api//products`: Crear un nuevo producto (**requiere autenticación**)
- `GET /api//products`: Listar todos los productos (público)
- `GET /api//products/{id}`: Obtener un producto por su ID
- `PUT /api//products/{id}`: Actualizar un producto (**requiere autenticación**)
- `DELETE /api//products/{id}`: Eliminar un producto (**requiere autenticación**)

### 🧾 Compras
- `POST /purchases`: Registrar una compra (**requiere autenticación**)  
  - Recibe: `product_id` y `total_products`  
  - El `user_id` se obtiene automáticamente desde el token JWT
- `GET /purchases/me`: Consultar el historial de compras del usuario autenticado  
  - Muestra: `id_purchase`, `product_name`, `total_products`

### 🔐 Autenticación
- Login basado en **JWT**
- Uso de `Bearer Token` en Swagger o Postman
- Protege rutas como `/products`, `/purchases`, `/users/me`

---

## 🧰 Tecnologías

- **FastAPI** (framework backend)
- **SQLModel** (ORM sobre SQLAlchemy + Pydantic)
- **PostgreSQL** (base de datos en Neon)
- **bcrypt** (hash de contraseñas)
- **python-jose** (manejo de JWT)
- **Swagger UI** (documentación automática)