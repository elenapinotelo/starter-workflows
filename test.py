from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

import requests

def is_stream_online(username):
    """
    Returns True if the Twitch stream is online, False otherwise.
    Uses the public frontend Client-ID (no OAuth).
    """
    url = f"https://www.twitch.tv/{username}"
    headers = {
        "Client-ID": "kimne78kx3ncx6brgo4mv6wki5h1ko",  # Publicly known Client-ID
    }
    resp = requests.get(url, headers=headers)
    return "isLiveBroadcast" in resp.text

with SB(uc=True, test=True) as sb:

    if True:
        url = "https://kick.com/brutalles"
        sb.uc_open_with_reconnect(url, 5)
        sb.uc_gui_click_captcha()
        sb.sleep(1)
        sb.uc_gui_handle_captcha()
        sb.sleep(1)
        if sb.is_element_present('button:contains("Accept")'):
            sb.uc_click('button:contains("Accept")', reconnect_time=4)
        if sb.is_element_visible('#injected-channel-player'):
            masooe = sb.get_new_driver(undetectable=True)
            masooe.uc_open_with_reconnect(url, 5)
            masooe.uc_gui_click_captcha()
            masooe.uc_gui_handle_captcha()
            sb.sleep(10)
            if masooe.is_element_present('button:contains("Accept")'):
                masooe.uc_click('button:contains("Accept")', reconnect_time=4)
            while sb.is_element_visible('#injected-channel-player'):
                sb.sleep(10)
            sb.quit_extra_driver()
    sb.sleep(1)


