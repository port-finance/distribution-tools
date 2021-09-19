# bitquery
import requests
from datetime import datetime

response = requests.get('https://intense-temple-44991.herokuapp.com/collaterals/mer')

result = response.json()
date = datetime.today().strftime('%Y-%m-%d')

with open("%s.txt" % date, "w") as f:
  for merDeposit in result:
    f.writelines(merDeposit["owner"])
    f.writelines(',')
    f.writelines(merDeposit["balanceInLamport"])
    f.writelines('\n')