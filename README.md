i3autostart
===========

This is a little script for starting desktop services from i3wm. It looks for
`.desktop` files in both the standard system location and the user's own
configuration directory.

To use, simply add the following to your i3 config file (usually located in
`~/.config/i3`):

    exec --no-startup-id /path/to/i3autostart.py

I typically put this in a bin directory in my home area.
