import contextlib
from random import randint

from camoufox import AsyncCamoufox

from services.models import Proxy

# from browserforge.fingerprints import Screen
# CONSTRAINS = Screen(
#     max_width=1920,
#     max_height=1080,
#     min_width=1920,
#     min_height=1080,
# )

FIREFOX_USER_PREFS = {
    "media.peerconnection.enabled": False,
    "media.peerconnection.ice.default_address_only": True,
    "media.peerconnection.ice.no_host": True,
    "media.peerconnection.ice.proxy_only_if_behind_proxy": True,
    "media.peerconnection.turn.disable": True,
    "media.peerconnection.use_document_iceservers": False,
    "media.peerconnection.identity.enabled": False,
    "media.getusermedia.screensharing.enabled": False,
    "media.getusermedia.browser.enabled": False,
    "media.getusermedia.audiocapture.enabled": False,
}


async def main(proxy: Proxy):
    async with AsyncCamoufox(
        os=["macos", "windows", "linux"],
        geoip=True,
        # locale="en-US",
        locale="en-US",
        humanize=True,
        headless=False,
        # screen=CONSTRAINS,
        enable_cache=False,
        # proxy=proxy,
        config={
            # "timezone": "Europe/Paris",
            # "geolocation:latitude": 48.8566,
            # "locale:language": "fr",
            # "locale:region": "FR",
            # "geolocation:longitude": 2.3522,
        },
        # proxy={"server": "http://64.226.55.92:8000"},
        proxy={
            "server": "http://23.230.8.106:64580",
            "username": "i92ShttG",
            "password": "Y749jzwr",
        },
        # proxy={"server": "http://89.207.250.243:3128"},
        # proxy={"server": "http://168.81.237.12:8000"},
        # proxy={"server": "http://168.81.237.161:8000"},
        # proxy={
        #     "server": "http://dc.decodo.com:10000",
        #     "username": "user-sosouser-country-au",
        #     "password": "U93z5db+t5lmsxCCsB",
        # },
        persistent_context=False,
        # ignore_https_errors=True,
        firefox_user_prefs=FIREFOX_USER_PREFS,
        # user_data_dir=PROFILES_DIR / ctx.state.user.login.username,
        i_know_what_im_doing=True,
    ) as b:
        p = await b.new_page()
        with contextlib.suppress(Exception):
            await b.pages[0].close()  # type: ignore
        # await p.goto("https://www.wildsultan.com/")

        # await p.goto("https://www.browserscan.net")
        await p.goto("https://2ip.io")
        await p.wait_for_load_state("networkidle")
        await p.wait_for_timeout(randint(25000, 35000))
        input("Press Enter to continue...")
