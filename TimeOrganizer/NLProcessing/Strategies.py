import abc
from typing import List
from typing import Tuple

class StrategyClass(abc.ABC):

    # Task
    @abc.abstractmethod
    def pos_tag_specific(self, text:str) -> List[Tuple[str,str]]:
        pass

    def classification(self, text: str) -> str:
        return self.pos_tags_simple(text)

    def pos_tags_simple(self, text: str) -> str:
        specPosList = self.pos_tag_specific(text)
        textClassfication = ""
        for specPos in specPosList:
            textClassfication += self.get_simple_tag(specPos[1]) + " "
        textClassfication = textClassfication[0:len(textClassfication)-1]
        return textClassfication

    # To simplify the model outuput for matching with wordnet library
    def get_simple_tag(self,specificTag: str) -> str:
        if specificTag.startswith('J'):
            return 'a'
        elif specificTag.startswith('V'):
            return 'v'
        elif specificTag.startswith('N'):
            return 'n'
        elif specificTag.startswith('R'):
            return 'r'
        else:
            return 'n'

# Context, which will be using nlp
class NLPClassification():
    def __init__(self, strategy: StrategyClass):
        self.__strategy:StrategyClass = strategy

    def setStrategy(self,strategy: StrategyClass):
        self.__strategy = strategy

    def getClassification(self,text:str) -> str:
        return self.__strategy.classification(text)




