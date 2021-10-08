import requests
from datetime import datetime
from proportional_distributor import transfer

asset_name = "mSOL"
print("Retrieving mSOL deposit")
result = requests.get('https://intense-temple-44991.herokuapp.com/collaterals/%s' % asset_name).json()
date = datetime.today().strftime('%Y-%m-%d')

file_name = "%s-%s.txt" % (asset_name, date)

with open(file_name, "w") as f:
  for merDeposit in result:
    f.writelines("%s,%s\n" % (merDeposit["owner"], merDeposit["balanceInLamport"]))

print("Sending transfer out")

env = {
  "TOKEN_MINT": "MNDEFzGvMt87ueuHvVU9VcTqsAP5b3fTGPsHuuPA5ey",
  "TOKEN_DECIMALS": 9,
  "LOG_FOLDER_PREFIX": "logs-",
  "FULL_LOGS": "detailed.log",
  "SUCCESS_LOGS": "success.log",
  "FAILED_LOGS": "failed.log",
  "CANCELED_LOGS": "cancelled.log",
  "UNCONFIRMED_LOGS": "unconfirmed.log",
  "RETRY_ON_429": True,
  "RPC_URL": "https://port-finance.rpcpool.com",
}


transfer(
  file_name=file_name,
  interactive=False,
  drop_amount=13736,
  fund_recipient=True,
  allow_unfunded_recipient=False,
  env=env
)