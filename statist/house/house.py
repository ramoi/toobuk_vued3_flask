from toobuk.tb import Toobuk
from pathlib import Path

THIS_FOLDER = Path(__file__).parent.resolve()

htb = Toobuk(THIS_FOLDER / 'statist/house/house')

def getTrade() :
	return htb.get('trade/date&loc&changeRate')THIS_FOLDER / 

def getCharter() :
	return htb.get('charter/changeRate')


