# import spacy

# nlp = spacy.load("en_core_web_sm")
# doc = nlp(
#     u"#bbuzz 2016: Rafał Kuć - Running High Performance And Fault Tolerant Elasticsearch"
# )
# for entity in doc.ents:
#     print(entity.label_, " | ", entity.text)

sample = [
    {
        "author": "Thatweebthatsimps",
        "body": "Shape of water",
        "id": "gvl9fsn",
        "permalink": "/r/AskReddit/comments/mx0pwd/what_movie_is_simply_magical_to_you_no_matter_how/gvl9fsn/",
        "score": 17,
    },
    {
        "author": "Brenvt19",
        "body": "Children of men \n\nLast of the Mohicans \n\nMars Attacks",
        "id": "gvl9iqh",
        "permalink": "/r/AskReddit/comments/mx0pwd/what_movie_is_simply_magical_to_you_no_matter_how/gvl9iqh/",
        "score": 118,
    },
    {
        "author": "Feelingofsunday",
        "body": "I haven't seen that one! I'll have to check it out!",
        "id": "gvl9k00",
        "permalink": "/r/AskReddit/comments/mx0pwd/what_movie_is_simply_magical_to_you_no_matter_how/gvl9k00/",
        "score": 1,
    },
    {
        "author": "Feelingofsunday",
        "body": "Mars Attacks is awesome! :D",
        "id": "gvl9liq",
        "permalink": "/r/AskReddit/comments/mx0pwd/what_movie_is_simply_magical_to_you_no_matter_how/gvl9liq/",
        "score": 45,
    },
    {
        "author": "redpatchedsox",
        "body": "The Secret Life of Walter Mitty",
        "id": "gvl9uj9",
        "permalink": "/r/AskReddit/comments/mx0pwd/what_movie_is_simply_magical_to_you_no_matter_how/gvl9uj9/",
        "score": 362,
    },
    {
        "author": "domicilecc",
        "body": "The Dark Knight Returns pt 1/2 (it's really one movie)\n\nThe best comic adaptation ever made, live action or animated.  It's pitch perfect.",
        "id": "gvl9vxs",
        "permalink": "/r/AskReddit/comments/mx0pwd/what_movie_is_simply_magical_to_you_no_matter_how/gvl9vxs/",
        "score": 9,
    },
    {
        "author": "Feelingofsunday",
        "body": "That movie has been on my list of movies I want to watch, but I haven't gotten around to it yet!",
        "id": "gvl9ylf",
        "permalink": "/r/AskReddit/comments/mx0pwd/what_movie_is_simply_magical_to_you_no_matter_how/gvl9ylf/",
        "score": 33,
    },
    {
        "author": "NomadSVP",
        "body": "Dragonheart",
        "id": "gvla0kj",
        "permalink": "/r/AskReddit/comments/mx0pwd/what_movie_is_simply_magical_to_you_no_matter_how/gvla0kj/",
        "score": 160,
    },
    {
        "author": "bob-weeaboo",
        "body": "That the one where a lady floods her house for some fish dick?",
        "id": "gvla27e",
        "permalink": "/r/AskReddit/comments/mx0pwd/what_movie_is_simply_magical_to_you_no_matter_how/gvla27e/",
        "score": 16,
    },
    {
        "author": "HilpoWuXing",
        "body": "Chicken Run (2000)",
        "id": "gvla38q",
        "permalink": "/r/AskReddit/comments/mx0pwd/what_movie_is_simply_magical_to_you_no_matter_how/gvla38q/",
        "score": 909,
    },
    {
        "author": "Feelingofsunday",
        "body": "My god I haven't read that title since forever! Lovely movie! :D",
        "id": "gvla7df",
        "permalink": "/r/AskReddit/comments/mx0pwd/what_movie_is_simply_magical_to_you_no_matter_how/gvla7df/",
        "score": 91,
    },
    {
        "author": "HOWDY__YALL",
        "body": "Ugh I HATED that movie, I was so disappointed by what I imagined was supposed to be the big *Of Course!* moment.\n\nKudos to you for standing up for it.",
        "id": "gvlabkj",
        "permalink": "/r/AskReddit/comments/mx0pwd/what_movie_is_simply_magical_to_you_no_matter_how/gvlabkj/",
        "score": -12,
    },
    {
        "author": "Dude_Uncool_80s",
        "body": "Swades",
        "id": "gvlanza",
        "permalink": "/r/AskReddit/comments/mx0pwd/what_movie_is_simply_magical_to_you_no_matter_how/gvlanza/",
        "score": 2,
    },
    {
        "author": "Feelingofsunday",
        "body": "I like the 90's adaption! (I think it's the 90's adaption anyway, it's animated.)",
        "id": "gvlb0za",
        "permalink": "/r/AskReddit/comments/mx0pwd/what_movie_is_simply_magical_to_you_no_matter_how/gvlb0za/",
        "score": 1,
    },
    {
        "author": "_Goose_",
        "body": "Willow \n\nShits the tits",
        "id": "gvlbetr",
        "permalink": "/r/AskReddit/comments/mx0pwd/what_movie_is_simply_magical_to_you_no_matter_how/gvlbetr/",
        "score": 804,
    },
    {
        "author": "Thatweebthatsimps",
        "body": "Brief nudity warning",
        "id": "gvlbjg9",
        "permalink": "/r/AskReddit/comments/mx0pwd/what_movie_is_simply_magical_to_you_no_matter_how/gvlbjg9/",
        "score": 1,
    },
    {
        "author": "lornstar7",
        "body": "Fuck yes. Have me nightmares as a kid but I love it so much",
        "id": "gvlbk9s",
        "permalink": "/r/AskReddit/comments/mx0pwd/what_movie_is_simply_magical_to_you_no_matter_how/gvlbk9s/",
        "score": 55,
    },
    {
        "author": "MooneySuzuki36",
        "body": 'Kung Pow: Enter the Fist\n\n*Grabs shoulders and shakes violently*\n\n"I implore you to reconsider"',
        "id": "gvlbkey",
        "permalink": "/r/AskReddit/comments/mx0pwd/what_movie_is_simply_magical_to_you_no_matter_how/gvlbkey/",
        "score": 4,
    },
    {
        "author": "Thatweebthatsimps",
        "body": "Yes",
        "id": "gvlbkkk",
        "permalink": "/r/AskReddit/comments/mx0pwd/what_movie_is_simply_magical_to_you_no_matter_how/gvlbkkk/",
        "score": 3,
    },
    {
        "author": "releserious",
        "body": "Airline safety demonstration videos",
        "id": "gvlblqe",
        "permalink": "/r/AskReddit/comments/mx0pwd/what_movie_is_simply_magical_to_you_no_matter_how/gvlblqe/",
        "score": 8,
    },
]

search = [
    ["Shape of water"],
    ["Children of men", "Last of the Mohicans", "Mars Attacks"],
    [],
    ["Mars Attacks"],
    ["The Secret Life of Walter Mitty"],
    ["The Dark Knight"],
    [],
    ["Dragonheart"],
    [],
    ["Chicken Run (2000)"],
    [],
    [],
    ["Swades"],
    [],
    ["Willow"],
    [],
    [],
    ["Kung Pow: Enter the Fist"],
    [],
    [],
]

DATA = []

for i in range(0, len(sample)):
    text = sample[i]["body"]
    searchText = search[i]
    value = {"entities": []}
    for x in searchText:
        start = text.index(x)
        wordLength = len(x)
        value["entities"].append((start, start + wordLength, "movie"))
    DATA.append((text, value))


# print(DATA)
outputFile = open("training_data.py", "a", encoding="utf-8")
outputFile.write(str(DATA))
outputFile.close()
