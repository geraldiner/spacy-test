import pandas as pd
from tqdm import tqdm
import spacy
from spacy.tokens import DocBin
import training_data

nlp = spacy.blank("en")  # load a new spacy model
db = DocBin()  # create a DocBin object

DATA = training_data.TRAINING_DATA

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
