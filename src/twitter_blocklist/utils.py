import twitter
import toml

def authenticate():
    """Authenticate to the Twitter API

    it uses the ``twitter_keys.toml`` file in the current folder
    """
    api = twitter.Api(**toml.load("twitter_keys.toml"), sleep_on_rate_limit=True)
    return api
