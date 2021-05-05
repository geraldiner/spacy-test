import spacy

nlp1 = spacy.load(".\output\model-last")  # load the best model
doc = nlp1(
    "The Imaginarium of Doctor Parnassus \n\nSomething about Tom Waits as the devil really does it for me."
)  # input sample text

for entity in doc.ents:
    print(entity.label_, " | ", entity.text)
