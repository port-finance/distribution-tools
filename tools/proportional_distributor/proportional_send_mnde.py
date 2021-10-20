import re
import subprocess
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
  "RETRY_ON_429": False,
  "RPC_URL": "https://api.mainnet-beta.solana.com",
}

total_amount = 88000

result = subprocess.run(['spl-token', 'account-info',  env['TOKEN_MINT']], stdout=subprocess.PIPE)
token_amount = re.search(r"(?<=Balance: )\d+\.\d *", result.stdout.decode('utf-8')).group(0)
if float(token_amount) < total_amount:
  print(f'Not enough token: {token_amount} required: {total_amount}')
  exit(1)

transfer(
  input_path=file_name,
  interactive=False,
  drop_amount=total_amount,
  fund_recipient=True,
  allow_unfunded_recipient=False,
  env=env
)