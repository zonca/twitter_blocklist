![Python package](https://github.com/zonca/twitter_blocklist/workflows/Python%20package/badge.svg)
[![PyPI version](https://badge.fury.io/py/twitter-blocklist.svg)](https://badge.fury.io/py/twitter-blocklist)

# `twitter_blocklist`

Export and import Twitter blocklists.

## Execute on Google Colaboratory

It can also be used in the Google Colaboratory Notebook without installing anything
in the local machine, this also includes the documentation:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zonca/twitter_blocklist/blob/master/run_twitter_blocklist.ipynb)


## Documentation and execution

It can also be executed from a Notebook, which also includes instructions
for setting it up and step-by-step explanation, see:

* <`run_twitter_blocklist.ipynb`>


## Quick reference

`twitter_blocklist` provides a command-line tool to export a list of all
the accounts you block to a text file:

    $ twitter_blocklist --export my_blocks.csv

or import a list from someone else, or downloaded from <https://blocktogether.org>:

    $ twitter_blocklist list_to_import.csv

or block all member of a Twitter list:

    $ twitter_blocklist --list <list_id>

undo blocking with the --unblock flag:

    $ twitter_blocklist --unblock --list <list_id>
    $ twitter_blocklist --unblock list_to_unblock.csv

Consider that Twitter rate-limits their APIs, I have setup the client to automatically
sleep in case of a rate-limiting error, in case that happens, just leave the script
running and it will complete at some point. For example exporting the blocks needs
to make 1 request every 5000 blocked IDs, so you could hit the limit of 15 requests
every 15 minutes, in that case the script will sleep for 15 minutes and then resume.

## Install

    $ pip install twitter_blocklist

## Initial setup

Create a Twitter app following the [instructions from the `python-twitter` project](https://python-twitter.readthedocs.io/en/latest/getting_started.html)

Create a text file named `twitter_keys.toml` with this format:

```
consumer_key='xxxxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret='xxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_key='xxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret='xxxxxxxxxxxxxxxxxxxxxxxxx'
```

Make sure you have the single quotes.

From the same folder where you have `twitter_keys.toml`, run the tool as shown above.
