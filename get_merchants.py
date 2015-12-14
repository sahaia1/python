import json
import urllib2

CMS_URL = 'http://config.app.bloomreach.com/api/merchants'


def get_merchants():
	request = urllib2.Request(CMS_URL)
	data = json.load(urllib2.urlopen(request))
	merchants = [item['value'] for item in data["merchants"][0]["merchant"]]
	merchant_ids = [item['id'] for item in data["merchants"][0]["merchant"]]
	return merchants, merchant_ids

if __name__ == "__main__":
	merchants, merchant_ids = get_merchants()
	print merchants
	print merchant_ids
	merch = "pumalksa"
	print merch in merchants
