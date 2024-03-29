#!/bin/bash

declare -r retentionInDays="3"
for L in $(aws logs describe-log-groups \
    --query 'logGroups[?!not_null(retention)] | [].logGroupName' \
    --output text --profile anninet)
do
   aws logs  put-retention-policy --log-group-name ${L} \
   --retention-in-days ${retentionInDays} --profile anninet
done