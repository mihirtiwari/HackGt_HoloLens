import requests
import datetime

api_key = "a2765a956823c74d3c23e9ed8547dfb8"
customer_id = "59e19c93ceb8abe24251c390"
merchant_id = "59e1a355ceb8abe24251c392"
account_id = "59e1a633ceb8abe24251c393"

base_url = "http://api.reimaginebanking.com/"

def getTotalBalance():
	url = base_url + "customers/" + customer_id + "/accounts?key=" + api_key
	r = requests.get(url)
	accounts = r.json()
	
	totalBalance = 0
	
	for account in accounts:
		totalBalance += account["balance"]
	
	return totalBalance

def calculateNewBalance(itemCost, currentBalance):
	return currentBalance - itemCost

def buyProduct(item, cost, currentBalance):
	now = datetime.datetime.now()
	purchase = { "merchant_id": merchant_id, "medium": "balance", "purchase_date": "" + str(now.year) + "-" + str(now.month) + "-" + str(now.day), "amount": cost, "description": item }
	url = base_url + "accounts/" + account_id + "/purchases?key=" + api_key
	r = requests.post(url, json=purchase)

	return calculateNewBalance(cost, currentBalance)
