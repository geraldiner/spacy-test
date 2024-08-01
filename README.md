# Spacy Test

Building off the [textual analysis from before](https://github.com/geraldiner/textual-analysis), I decided to look into other ways to process text to find what I'm looking for. I came across [this thread on Reddit](https://www.reddit.com/r/datascience/comments/dhchq2/extracting_movie_titles_from_text_source/), which was exactly what I needed to do!

However it didn't look like the original poster got anywhere with it. So I followed the suggestions from the commenters and I came to a [simple walkthrough for entity recognition](https://towardsdatascience.com/using-spacy-3-0-to-build-a-custom-ner-model-c9256bea098) using [Spacy](https://spacy.io/). There was another tutorial I'd started following based on a previous version of Spacy, but apparently the new version broke a lot of things.

The tutorial walked me through converting my training set data to the new `.spacy` format. The text below are from real comments from the original thread I plan to work with.

```
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
```

Then we got to train and test the new model. TBH, I didn't understand the output too much because I have virtually no knowledge of machine learning. I do understand that it tried its best and it can only be as good as the size of the training set (in my case 4 items).

![Training pipeline for my model](https://cdn.discordapp.com/attachments/377363002619461633/839063854398046248/unknown.png)

So it's no surprise that after testing the model on new, foreign text, it didn't do so well. On the first run, I input a comment that was part of the training set, so it caught it. In the second run, I input a foreign text with two movies, *The Jungle Book* and *Clerks*. It only caught part of someone's name from the text.

![Results of predictions with model](https://cdn.discordapp.com/attachments/377363002619461633/839057962768662549/unknown.png)

In an earlier reading, I remember reading about pre-built models, the most popular seeming to be `en_core_web_sm`. And while it caught some significant text, it wasn't what I was looking for.

![Results of prediction with pre-built model](https://cdn.discordapp.com/attachments/377363002619461633/839058092956057630/unknown.png)

## Next Steps
I think the most obvious next step is to add more to the training set. The older tutorial had mentioned having a smaller training set meant looping multiple times on it in any various shuffled order. This was deprecated with the new version of Spacy. In the new tutorial, there were 11 items, which means I'd have to have at least that much to get a better result with predictions. I'll go with a relatively safer number (eg. 20) and try again tomorrow















## Other Projects

Check out other stuff I've worked on:

**Secret Santa App**: https://github.com/geraldiner/secret-santa-app

**Minute To Win It Games API & Wiki**: https://github.com/geraldiner/min-to-win

## Currently I'm:

- Working full-time at <a target="_blank" href="https://nomnomnow.com">Nom Nom</a>, migrating JavaScript to TypeScript
- Building my brand, <a target="_blank" href="https://happiandco.com">Happi & Co. Studio LLC</a>

But I'm always open to hearing about your next big thing!

## Let's get to know each other!

Connect with me:

**Twitter**: [@GeraldineDesu](https://twitter.com/geraldinedesu)

**LinkedIn**: [in/GeraldineR](https://linkedin.com/in/geraldiner)

**Email**: hello [at] geraldiner [dot] com
