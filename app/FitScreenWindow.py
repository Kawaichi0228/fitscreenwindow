#! /usr/bin/env python3.9

# ===============================================================================
# - FitScreenWindow -
#
# Copyright (C) Kawaichi0228
# ===============================================================================
"""
import src.fitscreenwindowapp as app

app.main()
"""

"""
from src.lib.config import GuiService
gui_service = GuiService()
gui_service.start()
"""

#"""
from src.lib.config import Config, ConfigJsonRepository
json = ConfigJsonRepository()
json.setupConfigPython()

Config.Size.base_width_toleft_px = 800
json.setupConfigJsonDictionary()
json.write()
#"""