# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 13:23:01 2021

@author: anshu
"""

# =============================================================================
# # Python Design Patterns - Factory Method
# 
#  - an approch for providing common interface to instantiate objects
# =============================================================================

# language translation

# Approach without factory method
class FrTranslator:
    def __init__(self):
        self.dict = {'car':'voiture','bike':'bicyclette',
                     'cycle':'cyclette'}
    def translate(self,word):
        return self.dict[word]
    
class SpTranslator:
    def __init__(self):
        self.dict = {'car':'coche','bike':'bicicleta',
                     'cycle':'ciclo'}
    def translate(self,word):
        return self.dict[word]

fr = FrTranslator()
fr.translate('car')
sp = SpTranslator()
sp.translate('car')

##############################################################
# with factory method


class FrTranslator:
    def __init__(self):
        self.dict = {'car':'voiture','bike':'bicyclette',
                     'cycle':'cyclette'}
    def translate(self,word):
        return self.dict[word]
    
class SpTranslator:
    def __init__(self):
        self.dict = {'car':'coche','bike':'bicicleta',
                     'cycle':'ciclo'}
    def translate(self,word):
        return self.dict[word]

def factory(language='French'):
    "this is a factory method"
    trans_dict = {'French':FrTranslator,
                  'Spanish':SpTranslator}
    return trans_dict[language]()

fr = factory('French')
fr.translate('car')
sp = factory('Spanish')
sp.translate('bike')
