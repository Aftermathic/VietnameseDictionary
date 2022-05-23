from browser import html, document
from words import nouns, verbs, adjectives, pronouns, phrases

nouns.sort()
verbs.sort()
adjectives.sort()
pronouns.sort()

string = ""

for n in range(len(nouns)):
    string += f"{nouns[n][0]} (Noun): {nouns[n][1:]}".translate({ord(letter): None for letter in "[']"}) + html.P()

document["nouns"] <= html.B("Nouns:") + html.P() + string

string = ""

for v in range(len(verbs)):
    string += f"{verbs[v][0]} (Verb): {verbs[v][1:]}".translate({ord(letter): None for letter in "[']"}) + html.P()

document["verbs"] <= html.P() + html.B("Verbs:") + html.P() + string

string = ""

for a in range(len(adjectives)):
    string += f"{adjectives[a][0]} (Verb): {adjectives[a][1:]}".translate({ord(letter): None for letter in "[']"}) + html.P()


document["adjectives"] <= html.P() + html.B("Adjectives:") + html.P() + string

string = ""

for p in range(len(pronouns)):
    string += f"{pronouns[p][0]} (Pronoun): {pronouns[p][1:]}".translate({ord(letter): None for letter in "[']"}) + html.P()

document["pronouns"] <= html.P() + html.B("Pronouns:") + html.P() + string

string = ""

for s in range(len(phrases)):
    string += f"{phrases[s][0]} (Phrase): {phrases[s][1:]}".translate({ord(letter): None for letter in "[']"}) + html.P()

document["phrases"] <= html.P() + html.B("Phrases:") + html.P() + string