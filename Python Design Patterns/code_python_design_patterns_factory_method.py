# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 09:17:26 2021

@author: anshu
"""

# without factory method
# language translation

class FrenchTranslator:
    def __init__(self):
        self.dict = {'car':'voiture','cycle':'cyclette',
                     'bike':'bicyclette'}
    def translate(self,word):
        return self.dict[word]
    

class SpanishTranslator:
    def __init__(self):
        self.dict = {'car':'coche','cycle':'ciclo',
                     'bike':'bicicleta'}
    def translate(self,word):
        return self.dict[word]

french = FrenchTranslator()
spanish = SpanishTranslator()

french.translate("car")
spanish.translate("car")

###################################################

class FrenchTranslator:
    def __init__(self):
        self.dict = {'car':'voiture','cycle':'cyclette',
                     'bike':'bicyclette'}
    def translate(self,word):
        return self.dict[word]
    

class SpanishTranslator:
    def __init__(self):
        self.dict = {'car':'coche','cycle':'ciclo',
                     'bike':'bicicleta'}
    def translate(self,word):
        return self.dict[word]

def Factory(language='French'):
    "factory Method"
    translators = {"French":FrenchTranslator,
                   "Spanish":SpanishTranslator}
    return translators[language]()


french = Factory("French")
french.translate("car")    
spanish = Factory("Spanish")
spanish.translate("car")

###################################################
