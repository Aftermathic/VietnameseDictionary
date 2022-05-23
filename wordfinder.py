from browser import document, html
from words import nouns, verbs, adjectives, pronouns, phrases


def search(ev):
    document["foundwords"].text = ""

    string = document["searchbar"].value.lower()
    html_to_put = ""
    words_found = 0

    pronoun_words = ""
    for p in range(len(pronouns)):
        pronoun = pronouns[p][0]
        if pronoun in string:
            pronoun_words += f"{pronouns[p][0]} (Pronoun): {pronouns[p][1:]}"

            html_to_put += pronoun_words.translate({ord(letter): None for letter in "[']"}) + html.P()
            pronoun_words = ""
            words_found += 1

    noun_words = ""
    for n in range(len(nouns)):
        noun = nouns[n][0]
        if noun in string:
            noun_words += f"{nouns[n][0]} (Noun): {nouns[n][1:]}"

            html_to_put += noun_words.translate({ord(letter): None for letter in "[']"}) + html.P()
            noun_words = ""
            words_found += 1

    verb_words = ""
    for v in range(len(verbs)):
        verb = verbs[v][0]
        if verb in string:
            verb_words += f"{verbs[v][0]} (Verb): {verbs[v][1:]}"

            html_to_put += verb_words.translate({ord(letter): None for letter in "[']"}) + html.P()
            verb_words = ""
            words_found += 1

    adjectives_words = ""
    for a in range(len(adjectives)):
        adjective = adjectives[a][0]
        if adjective in string:
            adjectives_words += f"{adjectives[a][0]} (adjective): {adjectives[a][1:]}"

            html_to_put += adjectives_words.translate({ord(letter): None for letter in "[']"}) + html.P()
            adjectives_words = ""
            words_found += 1

    phrases_words = ""
    for s in range(len(phrases)):
        phrase = phrases[s][0]
        if phrase in string:
            phrases_words += f"{phrases[s][0]} (Phrase): {phrases[s][1:]}"

            html_to_put += phrases_words.translate({ord(letter): None for letter in "[']"}) + html.P()
            phrases_words = ""
            words_found += 1
    if words_found > 1:
        document["foundwords"] <= f"{words_found} words found!" + html.P() + html_to_put
    else:
        document["foundwords"] <= f"{words_found} word found!" + html.P() + html_to_put

document["searchbutton"].bind("click", search)