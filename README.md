# `twitter_blocklist`

Export and import Twitter blocklists.

`twitter_blocklist` provides a command-line tool to export a list of all
the accounts you block to a text file:

    $ twitter_blocklist --export my_blocks.csv

or import a list from someone else, or downloaded from <https://blocktogether.org>:

    $ twitter_blocklist list_to_import.csv

or block all member of a Twitter list:

    $ twitter_blocklist --list <list_id>

The files have a CSV extension but they are actually just text files with 1 Twitter
user ID per line.

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
