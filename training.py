import pandas as pd
from tqdm import tqdm
import spacy
from spacy.tokens import DocBin

nlp = spacy.blank("en")  # load a new spacy model
db = DocBin()  # create a DocBin object

DATA = [
    (u"I really like Home Alone.", {"entities": [(14, 24, "movie")]}),
    (
        u"Mars Attacks is awesome! :D",
        {"entities": [(0, 12, "movie")]},
    ),
    (u"Jurassic Park is awesome", {"entities": [(0, 13, "movie")]}),
    (
        u"Mhh.. I have to think abt this one\n\n\n\nIdk but as a child I really loved this one movie called SpiderWic, I was obsessed with it",
        {"entities": [(94, 103, "movie")]},
    ),
    (
        u"I have three.\n\n#Tron: Legacy\n\nThat movie's visuals and music blew my mind, simple as. When \"The Game Has Changed\" plays and the riders turn on their light-cycles energy trails as the build up rises for the first time. It's a scene forever burned into my mind.\n\n#Transformers\n\nImagine being me, an elementary school-aged kid and seeing Optimus Prime transform for the first time. I want to bottle that feeling up and drink it everyday. I became a Transformers fan on the spot because of that film, and I'm so glad I did, 14 years later.\n\n#Wall-E \n\nBest PIXAR movie **EVER**, fight me. The sense of wonder I felt when Wall�E and EVE were traversing the stars in dance was incredible. One of the best romantic scenes I've ever seen in a movie.",
        {"entities": [(16, 28, "movie"), (262, 274, "movie"), (538, 544, "movie")]},
    ),
]

for text, annot in tqdm(DATA):  # data in previous format
    doc = nlp.make_doc(text)  # create doc object from text
    ents = []
    for start, end, label in annot["entities"]:  # add character indexes
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents  # label the text with the ents
    db.add(doc)

db.to_disk("./train.spacy")  # save the docbin object

# import spacy

# nlp = spacy.blank("en")  # new empty model in English
# nlp.vocab.vectors.name = "magicmovies_model_training_test"  # name for list of vectors

# # add NER pipeline
# nlp.add_pipe("ner", last=True)  # add pipeline to model

# # add possible entity to the model
# # nlp.entity.add_label("MOVIE")

# # begin training
# optimizer = nlp.begin_training()

# # update model with training data
# nlp.update([text], [annotations], sgd=optimizer)

# # loop through training set in random order bc of so little training data
# for i in range(20):
#     random.shuffle(DATA)
#     for text, annotations in DATA:
#         nlp.update([text], [annotations], sgd=optimizer)
