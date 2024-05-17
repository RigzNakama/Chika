class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 27776767
    API_HASH = "e7b0d8f7b037df9ff8b300816e90080b"

    CASH_API_KEY = "OO98UW99PV92AL9W"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgresql://chikabot:robotchika@localhost:5432/chikabot"  # A sql database url from elephantsql.com

    EVENT_LOGS = -1002053024172  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://maticnemanja:kucingkawin@cluster0.qhwwh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/0198c42d3a8fb53b55385.jpg"

    SUPPORT_CHAT = "isekaiproject"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6787075419:AAEqfq6BCCY_8XYMCQpjoYJXfaaazfWi5d0"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = ""  # Get this value from https://timezonedb.com/api

    OWNER_ID = 1937217898  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
