import spacy

nlp1 = spacy.load("en_core_web_sm")  # load the best model
doc = nlp1(
    "The original Disney *Jungle Book*\n\nThe hand-drawn animations still look amazing, the musical numbers are great, Kaa and Shere-Kahn are both still terrifying. I want to be adopted by Baloo and Bagheera.\n\nOh and *Clerks* is perfect."
)  # input sample text

for entity in doc.ents:
    print(entity.label_, " | ", entity.text)
