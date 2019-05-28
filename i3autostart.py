#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ex: set ts=4 expandtab:

# i3autostart.py

# Copyright © 2019 Richard Danter. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#
#   * Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#
#   * Neither the name of the author nor the names of any contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

# Read .desktop files from the system (/etc/xdg/autostart) and user
# (~/.config/autostart) directories and run services which are enabled.

import configparser
import os

# Set to True for verbose/debug output
V=True

# List of places to search for autostart .desktop files
autostart_dirs = ['/etc/xdg/autostart',
                  os.environ['HOME'] + '/.config/autostart']


def process_desktop_file(f):
        if V:
                print("  Processing file:", f)

        # Check we really have a file
        if not os.path.isfile(f):
                return

        # Read the file content
        cfg = configparser.ConfigParser()
        cfg.read(f)

        # TODO - execute the service
        if V:
                print("    Executing:", cfg.get('Desktop Entry', 'Exec'))


def process_autostart_dir(d):
        if V:
                print("Processing directory:", d)

        # Check directory exists, exit if not
        if not os.path.isdir(d):
                return

        # Get a list of entries in the directory and sort them
        files = os.listdir(d)
        files.sort()

        for f in files:
                # Filter out non-.desktop files
                (p, e) = os.path.splitext(f)
                if e != '.desktop':
                        continue

                process_desktop_file(d+'/'+f)


### MAIN ###
for d in autostart_dirs:
        process_autostart_dir(d)
