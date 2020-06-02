import click
import toml
import twitter

from . import __version__

@click.command()
@click.version_option(version=__version__)
@click.option('--export/--no-export', default=False)
@click.argument('filename')
def main(export, filename):

    api = twitter.Api(**toml.load("twitter_keys.toml"))

    if export:
        with open(filename, "w") as f:
            for user in api.GetBlocks():
                f.write(str(user.id) + "\n")
    else:
        with open(filename, "r") as f:
            for user_id in f.readlines():
                api.CreateBlock(user_id=int(user_id))
