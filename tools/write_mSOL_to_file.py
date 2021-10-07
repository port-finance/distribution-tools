import requests
from datetime import datetime

asset_name = "mSOL"
result = requests.get('https://intense-temple-44991.herokuapp.com/collaterals/%s' % asset_name).json()
date = datetime.today().strftime('%Y-%m-%d')

with open("%s-%s.txt" % (asset_name, date), "w") as f:
  for merDeposit in result:
    f.writelines("%s,%s\n" % (merDeposit["owner"], merDeposit["balanceInLamport"]))