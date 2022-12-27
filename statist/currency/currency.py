from toobuk.tb import Toobuk

class Currency(Toobuk):
	def __init__(self) :
		self._walker = Toobuk('statist/currency/currency')

	def grumble(self) :
		return self._walker.get('nation')


__walker__ = Currency()
def get() :
	return __walker__.grumble()