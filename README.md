# BLEU

Out-of-the-box Python script for sentence level and corpus level BLEU calculation
We recommend users to use `nltk-based` BLEU calculation script by installing [nltk](http://www.nltk.org/) first.

Run `python bleu.py -h` or `python nltk_bleu.py -h` to see the help information

# Usage

`python bleu.py -h` to see the help information

1. input FILES
    * `python bleu.py -t translation.file -t reference.file`
    * Set the parameter `--segment-level` and other related parameters, such as `--smooth-epsilon`, `--smooth` to print sentence-level BLEU score.

2. input Strings
```
    python bleu.py -t "test bleu calculation" -r "test blue calculation"
    
    BLEU = 90.36,  66.7/0.0/0.0/0.0 (BP=1.0,  ratio=1.0,  hyp_len=3,  ref_len=3)
```

The `bleu.py` is updated from [this gist](https://gist.github.com/alvations/838cb021712ad66e7768).

# nltk-based
Instead of using `bleu.py`, one can use `nltk_bleu.py` based on [nltk](http://www.nltk.org/).

for example:
    ```
    python nltk_bleu.py -r reference.file -t translation.file
    ```

Similarly, one can use `--sentence-level` or `-sl` to print sentence-level BLEU score.

# TODO
1. `bleu.py` correctness check
2. better wrapper for `nltk_bleu.py`
3. NLTK installation included? 
