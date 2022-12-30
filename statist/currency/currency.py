from toobuk.tb import Toobuk
from pathlib import Path

THIS_FOLDER = Path(__file__).parent.resolve()

class Currency(Toobuk):
	def __init__(self) :
		self._walker = Toobuk(THIS_FOLDER / 'statist/currency/currency')

	def grumble(self) :
		return self._walker.get('nation')


__walker__ = Currency()
def get() :
	return __walker__.grumble()