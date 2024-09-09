import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "29771787"))
    API_HASH = os.environ.get("API_HASH", "ada9503721914aae513dabc6ddb2d73c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 7520023680:AAFYmdAY9HE26myKzchNQ0fCNgn0UX7TiWkNone)
    STRING_SESSION = os.environ.get("STRING_SESSION", BQHGSAsASkWlhnmueqJqitO379zsKFJBn_UHNJw81sdO5AKUSTErt7I0byvqVlukmejVF15R-GEGiQemsSZekdfzLWEQgbra80MLj6AQ9WWvpskuQmKZtI2LSjFxzVGNKx9ucYL2UM_i9edqT3HUgj5g4m9I9R9Ymd5i9AMOSLjT5fr9vNAlVC1AH2o9Hqzrq2-hTw4LIqBJ3gR-7-df1ikXO7L5FDum117mwVHWFtigsRbcf8mD6ZXsNnIA5v4_MPOZr8-huAZd5E2kMYqkJ1FmZ4j3pMc5X9HJSDWdZI6geWjX2o77Zoz5z1guusQUKiWXv4ZnReeUtvW5TS2AU6MHJPJ5pwAAAAGwNAX0AANone)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Shizukaxsnbot")
    SUPPORT = os.environ.get("SUPPORT", "https://t.me/+NmIsWkl7ikRlMDFl") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "https://t.me/KDramaDGGhindidub") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
