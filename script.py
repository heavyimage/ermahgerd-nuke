import re

class ermagerd:
    """ https://gist.github.com/brianseitel/3267351 """
    def __init__(self, arg1):
        self.result = self.gherd(arg1)

    def grab(self):
        return self.result

    def translate(self, word):

        # Don't translate short words
        if len(word) == 1:
            return word

        # Handle specific words
        if word == 'AWESOME':
            return 'ERSUM'
        elif word == 'BANANA':
            return 'BERNERNER'
        elif word == 'BAYOU':
            return 'BERU'
        elif word == 'FAVORITE' or word == 'FAVOURITE':
            return 'FRAVRIT'
        elif word == 'GOOSEBUMPS':
            return 'GERSBERMS'
        elif word == 'LONG':
            return 'LERNG'
        elif word == 'MY':
            return 'MAH'
        elif word == 'THE':
            return 'DA'
        elif word == 'THEY':
            return 'DEY'
        elif word == "WE'RE":
            return 'WER'
        elif word == 'YOU':
            return 'U'
        elif word == "YOU'RE":
            return 'YER'

        # Before translating, keep a reference of the original word
        original = word

        # Drop vowel from the end of words
        if len(original) > 2: # Keep it at the end of short words like WE
            word = re.sub('[AEIOUY]$', '', word)

        # Reduce duplicate letters
        word = re.sub('[^\w\s]|(.)(?=\1)', '', word)

        # Reduce adjacent vowels to one
        word = re.sub('[AEIOUY]{2,}', 'E', word)

        # DOWN => DERN
        word = re.sub('OW', 'ER', word)

        # Replace vowels with ER
        word = re.sub('[AEIOUY]+', 'ER', word)

        # OH -> ER
        word = re.sub('ERH', 'ER', word)

        # MY -> MAH
        word = re.sub('MER', 'MAH', word)

        # FALLING -> FERLIN
        word = re.sub('ERNG', 'IN', word)

        # POOPED -> PERPERED -> PERPED
        word = re.sub('ERPERD', 'ERPED', word)

        # MEME -> MAHM -> MERM
        word = re.sub('MAHM', 'MERM', word)

        # Keep Y as first character
        # YES -> ERS -> YERS
        if original[0] == 'Y':
            word = 'Y' + word

        # reduce duplicate letters
        word = re.sub('[^\w\s]|(.)(?=\1)', '', word)

        # YELLOW -> YERLER -> YERLO
        if original[:3] == 'LOW' and word[:3] == 'LER':
            word = word[0:3] + 'LO'

        return word

    def gherd (self, text):

        if len(text) == 0:
            return

        text = text.upper()

        words = text.split(' ')

        translated = []

        for word in words:
            prefix = re.match('/^\W+/', word)
            suffix = re.match('/\W+$/', word)

            if word:
                # Is translateable
                new_word = ''
                if prefix:
                    new_word = prefix
                new_word += self.translate(word)

                if suffix:
                    new_word += suffix
                translated.append(new_word)
            else:
                # Is punctuation
                translated.append(word)


        return ' '.join(translated)


def enumerate_menu(menu):

    # If menu, run this method on items
    if type(menu).__name__ == "Menu":
        for item in menu.items():
            enumerate_menu(item)

    # ermagerd the title
    try:
        name = menu.action().text().strip()
        if name != "":
            newname = ermagerd(name).grab()
            menu.action().setText(newname)
    except:
        pass

enumerate_menu(nuke.menu("Nuke"))
