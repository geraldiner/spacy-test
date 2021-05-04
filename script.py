# import spacy

# nlp = spacy.load("en_core_web_sm")
# doc = nlp(
#     u"#bbuzz 2016: Rafał Kuć - Running High Performance And Fault Tolerant Elasticsearch"
# )
# for entity in doc.ents:
#     print(entity.label_, " | ", entity.text)

text = [
    "Mhh.. I have to think abt this one\n\n\n\nIdk but as a child I really loved this one movie called SpiderWic, I was obsessed with it",
    "Mars Attacks is awesome! :D",
    "I really like Home Alone.",
    "Jurassic Park is awesome",
]

search = ["SpiderWic", "Mars Attacks", "Home Alone", "Jurassic Park"]

for i in range(0, len(text)):
    start = text[i].index(search[i])
    wordLength = len(search[i])
    # print(start, start + wordLength)

longText = "I have three.\n\n#Tron: Legacy\n\nThat movie's visuals and music blew my mind, simple as. When \"The Game Has Changed\" plays and the riders turn on their light-cycles energy trails as the build up rises for the first time. It's a scene forever burned into my mind.\n\n#Transformers\n\nImagine being me, an elementary school-aged kid and seeing Optimus Prime transform for the first time. I want to bottle that feeling up and drink it everyday. I became a Transformers fan on the spot because of that film, and I'm so glad I did, 14 years later.\n\n#Wall-E \n\nBest PIXAR movie **EVER**, fight me. The sense of wonder I felt when Wall-E and EVE were traversing the stars in dance was incredible. One of the best romantic scenes I've ever seen in a movie."

searchText = ["Tron: Legacy", "Transformers", "Wall-E"]

for s in searchText:
    start = longText.index(s)
    end = len(s)
    # print(s, start, start + end)


wat = [
    ("The F15 aircraft uses a lot of fuel", {"entities": [(4, 7, "aircraft")]}),
    ("did you see the F16 landing?", {"entities": [(16, 19, "aircraft")]}),
    ("how many missiles can a F35 carry", {"entities": [(24, 27, "aircraft")]}),
    ("is the F15 outdated", {"entities": [(7, 10, "aircraft")]}),
    (
        "does the US still train pilots to dog fight?",
        {"entities": [(0, 0, "aircraft")]},
    ),
    (
        "how long does it take to train a F16 pilot",
        {"entities": [(33, 36, "aircraft")]},
    ),
    ("how much does a F35 cost", {"entities": [(16, 19, "aircraft")]}),
    ("would it be possible to steal a F15", {"entities": [(32, 35, "aircraft")]}),
    ("who manufactures the F16", {"entities": [(21, 24, "aircraft")]}),
    ("how many countries have bought the F35", {"entities": [(35, 38, "aircraft")]}),
    ("is the F35 a waste of money", {"entities": [(7, 10, "aircraft")]}),
]
print(len(wat))
