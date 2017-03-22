inp="i love machine translation"
ref="i like machine translation"

echo "input string directly"
python bleu.py -t "$inp" -r "$ref" --segment-level

echo "input file, with segment-level and corpus-level BLEU"
sleep 1

python bleu.py -t data/hypo -r data/ref --segment-level
