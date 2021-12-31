# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 15:51:03 2021

@author: anshu
"""

import nltk
# pip install spacy
import spacy

from spacy import displacy

nltk.download("punkt")
nltk.download("wordnet")
nltk.download("tagsets")
nltk.download("averaged_perceptron_tagger")

# tokenization

data = "Berlin, Germany’s capital, dates to the 13th century. Reminders of the city's turbulent 20th-century history include its Holocaust memorial and the Berlin Wall's graffitied remains. Divided during the Cold War, its 18th-century Brandenburg Gate has become a symbol of reunification. The city's also known for its art scene and modern landmarks like the gold-colored, swoop-roofed Berliner Philharmonie, built in 1963."

# word tokenization

nltk.word_tokenize(data)

# sentence tokenization
nltk.sent_tokenize(data)

first_sent = nltk.sent_tokenize(data)[0]

print(first_sent)

# Pos tagging
nltk.pos_tag(nltk.word_tokenize(first_sent))

nltk.help.upenn_tagset("NNP")

#################################

# Entity recognition

# python -m spacy download en_core_web_sm
print(first_sent)

nlp = spacy.load("en_core_web_sm")
doc = nlp(first_sent)

for ent in doc.ents:
    print(ent.text, ent.label_)
    
data = "John met Jessica yesterday and asked her to join Boeing Inc next month with a salary of $4500 per month. He asked Jessica to meet him in London next day."
doc = nlp(data)
for ent in doc.ents:
    print(ent.text, ent.label_)

content = displacy.render(doc,style='ent')
print(content)
file = open("mydata.html",'w')
file.write(content)
file.close()