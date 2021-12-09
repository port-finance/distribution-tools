#!/usr/bin/env bash

python3 tools/proportional_distributor/proportional_distributor.py \
  transfer -a tools/proportional_distributor/investor-distributions/seed_smaller.txt \
  --fund-recipient --allow-unfunded-recipient
