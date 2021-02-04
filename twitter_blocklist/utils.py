import os
import twitter
import toml


def authenticate(auth_dict=None, twitter_keys_filename="twitter_keys.toml"):
    """Authenticate to the Twitter API

    It supports 3 ways of authenticating (in this order):
    * pass the auth_dict dictionarie as input argument with keys:
            consumer_key,consumer_secret,access_token_key,access_token_secret
    * set the environment variables:
            TWITTER_CONSUMER_KEY,TWITTER_CONSUMER_SECRET,TWITTER_ACCESS_TOKEN_KEY,
            TWITTER_ACCESS_TOKEN_SECRET
    * loads a TOML file (by default twitter_keys.toml in the current folder)

    Returns
    -------
    api : twitter.Api
        Authenticated twitter API instance
    """
    if auth_dict is None:
        if "TWITTER_CONSUMER_KEY" in os.environ:
            keys = [
                "consumer_key",
                "consumer_secret",
                "access_token_key",
                "access_token_secret",
            ]
            auth_dict = {k: os.environ["TWITTER_" + k.upper()] for k in keys}
        else:
            auth_dict = toml.load(twitter_keys_filename)
    api = twitter.Api(**auth_dict, sleep_on_rate_limit=True)
    return api
