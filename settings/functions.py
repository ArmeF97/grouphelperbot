import settings

def getStr(string, args=None):
    import importlib
    locale = importlib.import_module("settings.lang_"+settings.settings.Bot.language)
    if string in locale.dict:
        if args is None:
            return locale.dict[string]
        else:
            return locale.dict[string].format(*args)
    else:
        return "Not found"
