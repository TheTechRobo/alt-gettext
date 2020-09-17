class TranslationNotFoundError(Exception):
    pass

class Database:
    """
    Here put any language you want in a dictionary with syntax `key: value'.
    It's highly recommended to instead of editing the original strings, to edit the ones inside `en' so you dont have to change the keys later
    """
    en = {'Sorry, but you're dumb.': 'Sorry, but you cannot speak.', 'baby': 'young person'}
    fr = {'Sorry, but you're dumb.': 'Desole, mais tu ne peux pas parler.', 'bebe': 'personne jeune'}

class presetStaticData:
    """static data that wont change at runtime"""
    languages = ['en', 'fr', 'add more here!']

class runtimeDynamicData:
    """data that changes at runtime"""
    currentlang = "NONE"

class Translation(object):
    def __init__(self, language):
        assert language in presetStaticData.languages, "unable to find language `%s'" % language
        runtimeDynamicData.currentlang = language
        def _(string):
            exec("database = Database.%s" % runtimeDynamicData.currentlang)
            try:
                return database[string]
            except KeyError:
                raise TranslationNotFoundError(string)
        return _
