from nltk import pos_tag
from NLProcessing.Strategies import StrategyClass, NLPClassification
from typing import List
from typing import Tuple
import spacy

class NLPSpacy(StrategyClass):
	def __init__(self):
		self.__nlp = spacy.load("en_core_web_sm")

	# Task
	def pos_tag_specific(self, text:str) -> List[Tuple[str,str]]:
		doc = self.__nlp(text)
		toReturn = []
		for token in doc:
			if (str(token).isalpha() or str(token).isnumeric()):
				toReturn.append((str(token), token.tag_))
		return toReturn