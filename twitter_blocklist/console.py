import os
import requests
import click
import toml
from progressbar import progressbar
import twitter
import sys

from .utils import authenticate
from . import __version__


@click.command()
@click.version_option(version=__version__)
@click.option("--export/--no-export", default=False)
@click.option("--list/--no-list", default=False)
@click.option("--unblock/--no-unblock", default=False)
@click.argument("filename")
def main(export, list, unblock, filename):

    api = authenticate()

    if export:
        with open(filename, "w") as f:
            for user in api.GetBlocks():
                f.write('{},"{}"\n'.format(user.id_str, user.screen_name))
        sys.exit(0)

    if list:
        user_ids = [
            user.id
            for user in api.GetListMembersPaged(
                list_id=int(filename), count=10000, skip_status=True
            )[2]
        ]
    else:
        if os.path.exists(filename):
            with open(filename, "r") as f:
                lines = f.readlines()
        else:
            if not filename.startswith("http"):
                print(
                    "Cannot find file {} locally, trying to get it via network".format(
                        filename
                    )
                )
            lines = requests.get(filename).text.split("\n")
        user_ids = [l.split(",")[0].strip() for l in lines if len(l.strip()) > 0]

    block = api.CreateBlock if not unblock else api.DestroyBlock
    for user_id in progressbar(user_ids, redirect_stdout=True):
        try:
            block(user_id=int(user_id))
        except Exception as e:
            print(e)
