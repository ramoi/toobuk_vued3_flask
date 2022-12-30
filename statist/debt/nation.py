from toobuk.tb import Toobuk
from pathlib import Path

THIS_FOLDER = Path(__file__).parent.resolve()

__walker__ = Toobuk(THIS_FOLDER / 'statist/debt/nation')

def get() :
	return __walker__.get('debtInfo/date&debtCp')

# def deptClass() :
# 	return __result__.get('deptClass')

# def debtCp() :
# 	return __result__.get('debtCp')

