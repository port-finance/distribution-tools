# bitquery
import requests
from datetime import datetime

result = requests.get('https://intense-temple-44991.herokuapp.com/collaterals/mSOL').json()
date = datetime.today().strftime('%Y-%m-%d')

with open("%s.txt" % date, "w") as f:
  for merDeposit in result:
    f.writelines("%s,%s\n" % (merDeposit["owner"], merDeposit["balanceInLamport"]))