#!/usr/bin/env bash

# amount 162500
python3   tools/proportional_distributor/proportional_distributor.py \
  transfer -a tools/proportional_distributor/investor-distributions/seed_larger.txt \
  --fund-recipient --allow-unfunded-recipient