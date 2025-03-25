# Bot de Twitter (X)

Este es un bot de Twitter (X) desarrollado en Python con la librería Tweepy. El bot está diseñado para realizar las siguientes acciones:

-   Seguir a los seguidores del usuario.
-   Retuitear tweets basados en palabras clave.
-   Marcar tweets como favoritos basados en palabras clave.
-   Responder a tweets basados en palabras clave.

## Requisitos

-   Python 3.6+
-   Tweepy (`pip install tweepy python-dotenv`)
-   Variables de entorno configuradas en un archivo `.env` (ver ejemplo abajo).

## Configuración

1.  **Clona el repositorio:**

    ```bash
    git clone [[(https://github.com/paco550/bot_twitter/))
    cd [nombre del repositorio]
    ```

2.  **Crea un archivo `.env`:**

    Crea un archivo `.env` en la raíz del proyecto y agrega tus claves de API de Twitter (X):

    ```dotenv
    CONSUMER_KEY=tu_consumer_key
    CONSUMER_SECRET=tu_consumer_secret
    ACCESS_TOKEN=tu_access_token
    ACCESS_TOKEN_SECRET=tu_access_token_secret
    ```

3.  **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta el bot:**

    ```bash
    python bot_twitter.py
    ```

## Funcionalidades

### Seguir Seguidores

El bot sigue automáticamente a todos los usuarios que siguen a la cuenta autenticada.

### Retuitear Tweets

El bot busca tweets basados en una palabra clave y los retuitea.

### Marcar Tweets como Favoritos

El bot busca tweets basados en una palabra clave y los marca como favoritos.

### Responder a Tweets

El bot busca tweets basados en una palabra clave y responde a ellos con un mensaje predefinido.

## Manejo de Errores y Limitaciones de la API de X

Debido a los recientes cambios en la API de X (Twitter), es posible que experimentes errores `403 Forbidden`. Esto se debe a las restricciones de acceso a ciertos endpoints (como `followers/list` y `search/tweets`) basadas en tu nivel de acceso a la API.

-   **Nivel de Acceso "Leer y escribir":**
    -   Este nivel permite leer y escribir recursos, pero no garantiza acceso a todos los endpoints.
-   **Errores 403:**
    -   Indican que tu cuenta no tiene los permisos necesarios para realizar la acción solicitada.
    -   Debes revisar tu nivel de acceso en el [portal de desarrolladores de X](https://developer.x.com/en/portal/product) y considerar actualizarlo si es necesario.
-   **API v2:**
    -   Explora los endpoints disponibles en la API v2, ya que algunos podrían ser accesibles con tu nivel de permiso actual.

## Manejo de Errores en el Código

El código incluye manejo de errores para las excepciones de la API de Tweepy, como `Forbidden` y `TweepyException`. Los errores se registran en la consola.

## Contribución

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes sugerencias de mejora, por favor, abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).
