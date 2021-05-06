import spacy

nlp1 = spacy.load(".\output\model-last")  # load the best model
doc = nlp1(
    "5 Perfect Movies:  \nThe Black Stallion  \nThe Sound of Music  \nPride &amp; Prejudice  \nPrincess Mononoke  \nSeven Samurai"
)  # input sample text

for entity in doc.ents:
    print(entity.label_, " | ", entity.text)
