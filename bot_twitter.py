import dotenv
import tweepy
import os

# Cargar variables de entorno
dotenv.load_dotenv()
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Autenticación de la API de Twitter
try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.verify_credentials()
    print("Autenticación exitosa")
except tweepy.errors.TweepyException as e:
    print(f"Error en la autenticación: {e}")
    exit()

def follow_followers():
    """Sigue a todos los seguidores del usuario."""
    try:
        for follower in tweepy.Cursor(api.get_followers).items():
            follower.follow()
            print(f"Siguiendo a {follower.screen_name}")
    except tweepy.errors.Forbidden as e:
        print(f"Error al seguir seguidores: {e.response}")
    except tweepy.errors.TweepyException as e:
        print(f"Error al seguir seguidores: {e}")

def retweet_keyword(keyword, num_tweets):
    """Retuitea tweets basados en una palabra clave."""
    try:
        for tweet in tweepy.Cursor(api.search_tweets, q=keyword, tweet_mode='extended').items(num_tweets):
            try:
                if not tweet.retweeted:
                    api.retweet(tweet.id)
                    print(f"Retuiteado: {tweet.full_text}")
            except tweepy.errors.Forbidden as e:
                print(f"Error al retuitear: {e.response}")
            except tweepy.errors.TweepyException as e:
                print(f"Error al retuitear: {e}")
    except tweepy.errors.Forbidden as e:
        print(f"Error al buscar tweets: {e.response}")
    except tweepy.errors.TweepyException as e:
        print(f"Error al buscar tweets: {e}")

def like_tweets(keyword, num_tweets):
    """Marca como favorito tweets basados en una palabra clave."""
    try:
        for tweet in tweepy.Cursor(api.search_tweets, q=keyword, tweet_mode='extended').items(num_tweets):
            try:
                if not tweet.favorited:
                    api.create_favorite(tweet.id)
                    print(f"Me gusta en: {tweet.full_text}")
            except tweepy.errors.Forbidden as e:
                print(f"Error al dar 'me gusta': {e.response}")
            except tweepy.errors.TweepyException as e:
                print(f"Error al dar 'me gusta': {e}")
    except tweepy.errors.Forbidden as e:
        print(f"Error al buscar tweets: {e.response}")
    except tweepy.errors.TweepyException as e:
        print(f"Error al buscar tweets: {e}")

def reply_to_tweets(keyword, num_tweets, response_text):
    """Responde a tweets basados en una palabra clave."""
    try:
        for tweet in tweepy.Cursor(api.search_tweets, q=keyword, tweet_mode='extended').items(num_tweets):
            try:
                username = tweet.user.screen_name
                tweet_id = tweet.id
                api.update_status(f"@{username} {response_text}", in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)
                print(f"Respondido a @{username}")
            except tweepy.errors.Forbidden as e:
                print(f"Error al responder: {e.response}")
            except tweepy.errors.TweepyException as e:
                print(f"Error al responder: {e}")
    except tweepy.errors.Forbidden as e:
        print(f"Error al buscar tweets: {e.response}")
    except tweepy.errors.TweepyException as e:
        print(f"Error al buscar tweets: {e}")

def main():
    """Función principal para ejecutar las funciones del bot."""
    follow_followers()
    retweet_keyword("Python", 5)
    like_tweets("Python", 5)
    reply_to_tweets("Python", 5, "¡Excelente tweet!")

if __name__ == "__main__":
    main()