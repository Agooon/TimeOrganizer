import abc

class StrategyClass(abc.ABC):
    @abc.abstractmethod
    def task(text:str) -> str:
        pass

    def get_simple_tag(specificTag: str) -> str:
        if specificTag.startswith('J'):
            return 'a'
        elif specificTag.startswith('V'):
            return 'v'
        elif specificTag.startswith('N'):
            return 'n'
        elif specificTag.startswith('R'):
            return 'r'
        else:
            return '-'

# Context, whcich will be using nlp
class NLPClassification():
    def __init__(self, strategy: Strategy):
        self.__strategy = strategy

    def setStrategy(self,strategy: Strategy):
        self.__strategy = strategy

    def getClassification(self,text:str) -> str:
        return self.__strategy(text)




