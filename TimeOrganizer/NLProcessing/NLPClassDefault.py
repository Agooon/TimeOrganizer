from nltk import pos_tag
from NLProcessing.Strategies import StrategyClass, NLPClassification
from typing import List
from typing import Tuple

class NLPClassDefault(StrategyClass):

	# Task
	def pos_tag_specific(self, text:str) -> List[Tuple[str,str]]:
		return pos_tag(text.split())



def testing():
	checkEngine = NLPClassification(NLPClassDefault())

	print(checkEngine.getClassification("The quick brown fox jumps over the lazy dog"))
	