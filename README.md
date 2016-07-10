i3 Twitch
=========

This is a little service to let me interact with twitch chat through notifications and dmenu. It might do other things in the future.

Requirements
------------
* Python 3
* `pip install -r requirements.txt`
* dmenu
* The `gi` Python module from your package manager (Probably something like `python-gobject`)
* A notification daemon

NOTE: If you're using virtual environments, you will likely need to use `--system-site-packages` (or similar) for access to the `gi` module.