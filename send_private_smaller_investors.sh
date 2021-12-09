#!/usr/bin/env bash

# amount 74667
python3   tools/proportional_distributor/proportional_distributor.py \
  transfer -a tools/proportional_distributor/investor-distributions/private_smaller.txt \
  --fund-recipient --allow-unfunded-recipient