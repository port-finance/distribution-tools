#!/usr/bin/env bash

# amount 180,833
python3   tools/proportional_distributor/proportional_distributor.py \
  transfer -a tools/proportional_distributor/investor-distributions/private_larger.txt \
  --fund-recipient --allow-unfunded-recipient