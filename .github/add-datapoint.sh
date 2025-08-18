#!/bin/bash
set -euxo pipefail

cd $(git rev-parse --show-toplevel)

TODAY=$(date +%Y-%m-%d)
python3 util/get.py > "data/$TODAY.json"

ln -sf "$TODAY.json" data/latest.json

git config --local user.email "41898282+github-actions[bot]@users.noreply.github.com"
git config --local user.name "github-actions[bot]"

git add .
git commit -m "bot: update data for $TODAY"
git push
