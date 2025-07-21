import tweepy
from typing import List

def get_tweets(
    query: str,
    api_key: str,
    api_secret: str,
    access_token: str,
    access_token_secret: str,
) -> List[str]:
    """Fetch tweets matching a query."""
    try:
        auth = tweepy.OAuthHandler(
            api_key, api_secret, access_token, access_token_secret
        )
        api = tweepy.API(auth)
        tweets = api.search_tweets(q=query, lang="en", count=10)
        return [tweet.text for tweet in tweets]
    except Exception as e:
        return [f"Twitter API error: {e}"]
