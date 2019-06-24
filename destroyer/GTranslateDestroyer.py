"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

"""
This program translates a string into a defined number of languages up to a maximum of 99 then back to the text's original language
using Google Translate.
Thanks to mouuff (https://github.com/mouuff) for his mtranslate Google Translate library (https://github.com/mouuff/mtranslate)

Author: Matan Davidi
Version: 28 December 2018
"""
from .mtranslate.mtranslate import translate


class GTranslateDestroyer:
    MAX_LANGUAGES_NUMBER = 99

    LANGS = ["af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca", "ceb", "ny", "zh", "co", "hr",
             "cs", "da", "nl", "en", "eo", "et", "fil", "fi", "fr", "fy", "gl", "ka", "de", "el", "gu", "ht", "ha",
             "he", "hi", "hu", "is", "ig", "id", "ga", "it", "ja", "jv", "kn", "kk", "km", "ko", "ku", "ky", "lo",
             "la", "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "my", "ne", "no", "ps", "fa",
             "pl", "pt", "pa", "ro", "ru", "sm", "gd", "sr", "st", "sn", "sd", "si", "sk", "sl", "so", "es", "su",
             "sw", "sv", "tg", "ta", "te", "th", "tr", "uk", "ur", "uz", "vi", "cy", "xh", "yi", "yo", "zu"]

    def __init__(self, *args):

        if len(args) == 1:
            self.init_only_text(args[0])
        elif len(args) == 2:
            self.init_text_lang(args[0], args[1])
        elif len(args) >= 3:
            self.init_text_num_lang(args[0], int(args[1]), args[2])

    def init_only_text(self, text_to_destroy: str):
        self.to_translate = text_to_destroy
        self.initial_language = "en"
        self.languages_number = self.MAX_LANGUAGES_NUMBER

    def init_text_lang(self, text_to_destroy: str, initial_language: str):
        self.to_translate = text_to_destroy
        self.initial_language = initial_language
        self.languages_number = self.MAX_LANGUAGES_NUMBER

    def init_text_num_lang(self, text_to_destroy: str, number_of_languages: int, initial_language: str):
        self.to_translate = text_to_destroy
        self.initial_language = initial_language

        if self.MAX_LANGUAGES_NUMBER >= number_of_languages > 0:
            self.languages_number = number_of_languages
        else:
            self.languages_number = self.MAX_LANGUAGES_NUMBER

    def destroy(self):
        result = self.to_translate

        for i in range(int(self.languages_number)):
            result = translate(result, self.LANGS[i])
            print(translate(result, self.initial_language))

        return translate(result, self.initial_language)


def main():
    destroyer = GTranslateDestroyer(
        #         """
        #         ’Twas brillig, and the slithy toves
        # Did gyre and gimble in the wabe;
        # All mimsy were the borogoves,
        # And the mome raths outgrabe.
        #
        # “Beware the Jabberwock, my son!
        # The jaws that bite, the claws that catch!
        # Beware the Jubjub bird, and shun
        # The frumious Bandersnatch!”
        #
        # He took his vorpal sword in hand:
        # Long time the manxome foe he sought—
        # So rested he by the Tumtum tree,
        # And stood awhile in thought.
        #
        # And as in uffish thought he stood,
        # The Jabberwock, with eyes of flame,
        # Came whiffling through the tulgey wood,
        # And burbled as it came!
        #
        # One, two! One, two! And through and through
        # The vorpal blade went snicker-snack!
        # He left it dead, and with its head
        # He went galumphing back.
        #
        # “And hast thou slain the Jabberwock?
        # Come to my arms, my beamish boy!
        # O frabjous day! Callooh! Callay!”
        # He chortled in his joy.
        #
        # ’Twas brillig, and the slithy toves
        # Did gyre and gimble in the wabe;
        # All mimsy were the borogoves,
        # And the mome raths outgrabe.
        #         """, "en")
        "Hello, world!", "en")

    print(destroyer.destroy())


if __name__ == '__main__':
    main()
