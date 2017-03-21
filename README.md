# BLEU

Sentence level and corpus level BLEU calculation

See [this gist](https://gist.github.com/alvations/838cb021712ad66e7768)

# Usage

`python bleu.py -h` to see the help information

1. input FILES
    * `python bleu.py --translation translation.file --reference reference.file`

2. input Strings
```
    `python bleu.py --translation "test bleu calculation" --reference "test blue calculation"`
    
    BLEU = 90.36,  66.7/0.0/0.0/0.0 (BP=1.0,  ratio=1.0,  hyp_len=3,  ref_len=3)
```
