from statist.currency import currency 
from statist.debt import nation 
from statist.debt import family
from statist.house import  house
from flask import Flask, jsonify as JsonResponse

# def index() : 
# 	return render(, 'stock/index.html')

# Create your views here.
# def render_statist():
#     template_data = {
#         'day': [1,2,3],
#         'temperature': [29,27,33]
#     }
#     if .method == 'GET':
#         print("get...")

#     return render(, 'stock/stock.html',template_data)

# def getStock() :
# 	s = StockProgress()
# 	resultData = s.grumble()

# 	print(resultData)

# 	return JsonResponse(resultData)

def getStock() :
	return JsonResponse( {} )

def getCurrency() :
	resultData = currency.get()

	print(resultData)

	return JsonResponse({ 'result' : resultData })

def getDebt() :
	resultData = nation.get()

	print(resultData)

	return JsonResponse({ 'result' : resultData })

def getDebtFamily() :
	resultData = family.get()

	print(resultData)

	return JsonResponse({ 'result' : resultData })

def getTrade() :
	resultData = house.getTrade()
	print(resultData)
	return JsonResponse({ 'result' : resultData })

def getCharter() :
	resultData = house.getCharter()
	print(resultData)
	return JsonResponse({ 'result' : resultData })
