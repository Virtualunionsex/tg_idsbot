#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import os


class Config:
    API_ID = int(os.environ.get("API_ID", "16246834"))  # Change 12345 to your API_ID
    API_HASH = os.environ.get("API_HASH", "29b3ffa9245c07f05375b92f38e8f13d")  # Change None to your API_HASH
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5636298682:AAFZGfJhMuUZGo98GlPvuXg-7Id3TXjh230")  # Change None to your BOT_TOKEN
    OWNER_ID = int(os.environ.get("OWNER_ID", "1715348447"))  # Change 0 to your OWNER_ID
    OWNER_NAME = os.environ.get("OWNER_NAME", "cyellaku")  # Change None to your OWNER_NAME

    # For Local Deploys edit above 5 lines.
    # Put your API_ID and OWNER_ID (without comma) and API_HASH,BOT_TOKEN n OWNER_NAME (with commas) below.
    # If got any problem ask in @ZauteBot
