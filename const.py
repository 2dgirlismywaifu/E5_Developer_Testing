AZURE_OAUTH_TOKEN_URL = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
AZURE_API_LIST = [
    "https://graph.microsoft.com/v1.0/me/drive/root",
    "https://graph.microsoft.com/v1.0/me/drive",
    "https://graph.microsoft.com/v1.0/drive/root",
    "https://graph.microsoft.com/v1.0/users",
    "https://graph.microsoft.com/v1.0/me/messages",
    "https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules",
    "https://graph.microsoft.com/v1.0/me/mailFolders/Inbox/messages/delta",
    "https://graph.microsoft.com/v1.0/me/drive/root/children",
    "https://api.powerbi.com/v1.0/myorg/apps",
    "https://graph.microsoft.com/v1.0/me/mailFolders",
    "https://graph.microsoft.com/v1.0/me/outlook/masterCategories",
]
URL_ENCODED_HEADER = {"Content-Type": "application/x-www-form-urlencoded"}
JSON_HEADER = {"Content-Type": "application/json"}
REDIRECT_URI = "http://localhost:53682/"
