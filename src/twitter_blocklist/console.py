import click
import toml
from progressbar import progressbar
import twitter
import sys

from . import __version__


@click.command()
@click.version_option(version=__version__)
@click.option("--export/--no-export", default=False)
@click.option("--list/--no-list", default=False)
@click.option("--unblock/--no-unblock", default=False)
@click.argument("filename")
def main(export, list, unblock, filename):

    api = twitter.Api(**toml.load("twitter_keys.toml"), sleep_on_rate_limit=True)

    if export:
        blocks_ids = api.GetBlocksIDs(stringify_ids=True)
        with open(filename, "w") as f:
            f.writelines("\n".join(blocks_ids))
        sys.exit(0)

    if list:
        user_ids = [
            user.id
            for user in api.GetListMembersPaged(
                list_id=int(filename), count=10000, skip_status=True
            )[2]
        ]
    else:
        with open(filename, "r") as f:
            user_ids = [l.strip() for l in f.readlines()]

    block = api.CreateBlock if not unblock else api.DestroyBlock
    for user_id in progressbar(user_ids, redirect_stdout=True):
        try:
            block(user_id=int(user_id))
        except Exception as e:
            print(e)
