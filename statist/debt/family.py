from toobuk.tb import Toobuk
from pathlib import Path

THIS_FOLDER = Path(__file__).parent.resolve()

__walker__ = Toobuk(THIS_FOLDER / 'statist/debt/family')
def get() :
	return __walker__.get('family')

