#!/usr/bin/env bash

old="${1:-HEAD~1}"
new="${2:-HEAD}"

./git-latexdiff "$old" "$new" \
  --main ma_hannah_lappe.tex \
  --latexopt '-shell-escape -interaction=nonstopmode -output-directory=./out' \
  --build-dir out \
  --prepare 'mkdir out' \
  --preamble diffpreamble.tex \
  --run-biber
