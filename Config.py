import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "16073023"))
    API_HASH = os.environ.get("API_HASH", "92ad3cbe7ddf64a702d5caeaf42357fc")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6061208032:AAFwL5p0Mzh4ShsJaNz5LVyEgBkQxm_20JE")
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOGcBu5zQJ0WK8EbgQwIGK9OBvKVTKMrZOvytUZN-ekLUOGzTC69psmpMtl9NPwnXqao5IIv5a0NTgud5nydyL87oX3tQf4WX970CL-rB3w8DhsQEsNjyHJdSsthg0DsHW2Jj-egtvGVhbvLBhz0a75n9E_lBgKss0MnOwWxZE2sKbrqAlYPzErPqMsG-cUVC7nZFKR5XLXCqPuy7jzQFoduMBCaAvDJk0JTNGcDXGsEiZoqA2dGmijMHsL7L2k6j9rxQmnG1Hqt-0oVmC5-wPPkM4rcjxpc8LBpOBw8NMJbKl7IeSnlcYzZyn0RabGpUViQgyIgOcVxTkXQmsUd0Pldf8kI=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
