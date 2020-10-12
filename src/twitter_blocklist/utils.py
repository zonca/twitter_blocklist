import os
import twitter
import toml


def authenticate():
    """Authenticate to the Twitter API

    it uses the ``twitter_keys.toml`` file in the current folder
    """
    if "TWITTER_CONSUMER_KEY" in os.environ:
        keys = [
            "consumer_key",
            "consumer_secret",
            "access_token_key",
            "access_token_secret",
        ]
        auth_dict = {k: os.environ["TWITTER_" + k.upper()] for k in keys}
    else:
        auth_dict = toml.load("twitter_keys.toml")
    api = twitter.Api(**auth_dict, sleep_on_rate_limit=True)
    return api
