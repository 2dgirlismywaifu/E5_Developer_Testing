# -*- coding: UTF-8 -*-
import argparse
import requests as req
import json
import sys
from logger import configure_logging, get_logger

from const import (
    AZURE_API_LIST,
    AZURE_OAUTH_TOKEN_URL,
    JSON_HEADER,
    REDIRECT_URI,
    URL_ENCODED_HEADER,
)
# Please register your Azure Application first, and grant it with the mandatory permissions below:
# files:	Files.Read.All、Files.ReadWrite.All、Sites.Read.All、Sites.ReadWrite.All
# user:	    User.Read.All、User.ReadWrite.All、Directory.Read.All、Directory.ReadWrite.All
# mail:     Mail.Read、Mail.ReadWrite、MailboxSettings.Read、MailboxSettings.ReadWrite
# Remember to Click "Grant admin consent for <your tenant>" in the "API Permissions" page.

session = req.session()
path = sys.path[0] + r"/refresh_token.txt"
call_count = 0
api_list = AZURE_API_LIST
logger = get_logger(__name__)


# Get the access token from microsoft graph api and write the new refresh token to the file.
def gettoken(id, secret, refresh_token):
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": id,
        "client_secret": secret,
        "redirect_uri": REDIRECT_URI,
    }
    html = session.post(
        AZURE_OAUTH_TOKEN_URL,
        data=data,
        headers=URL_ENCODED_HEADER,
    )
    jsontxt = json.loads(html.text)
    refresh_token = jsontxt["refresh_token"]
    access_token = jsontxt["access_token"]
    with open(path, "w+") as f:
        f.write(refresh_token)
    return access_token


def main():
    parser = argparse.ArgumentParser(
        description="Generate the access token from the refresh token to call the Microsoft Graph API."
    )
    parser.add_argument(
        "-i", "--id", type=str, help="Application Client ID", required=True
    )
    parser.add_argument("-s", "--secret", type=str, help="Client Secret", required=True)
    parser.add_argument(
        "-r", "--refresh", type=str, help="Refresh Token", required=True
    )
    args = parser.parse_args()

    global call_count
    access_token = gettoken(args.id, args.secret, args.refresh)
    headers = {"Authorization": access_token, **JSON_HEADER}

    for api in api_list:
        try:
            resp = session.get(api, headers=headers)
            if resp.status_code == 200:
                call_count += 1
                logger.info("Call %s successfully", api)
        except Exception:
            logger.exception("Call %s failed", api)

    logger.info(
        "End of the test, the total number of successful calls is: %s", call_count
    )


if __name__ == "__main__":
    configure_logging()
    for _ in range(5):
        main()
