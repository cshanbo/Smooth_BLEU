#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
sent bleu using nltk
'''

import nltk
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Arguments for calculating BLEU')
    parser.add_argument('-r', '--reference', type=str, required=True, 
                         help="reference file")
    parser.add_argument('-t', '--translation', type=str, required=True, 
                         help="translation file")
    parser.add_argument('-sl', '--sentence-level', action='store_true',
                         help="print segment level BLEU score (default: %(default)s)")
    parser.add_argument('-o', '--output', type=str, default='', required=False, 
                        help="output BLEU score to this file in segment level 
                              scenario (default: %(default)s)")

    args = parser.parse_args()
    if args.sentence_level:
        with open(args.translation, 'r') as trans, open(args.reference, 'r') as ref:
            if args.output == '':
                for tl in trans:
                    rl = ref.readline()
                    tran_list = tl.strip().split(' ')
                    ref_list = rl.strip().split(' ')
                    print(nltk.translate.bleu_score.sentence_bleu([ref_list], tran_list))
            else:
                with open(args.output, 'w') as outputfile:
                    for tl in trans:
                        rl = ref.readline()
                        tran_list = tl.strip().split(' ')
                        ref_list = rl.strip().split(' ')
                        outputfile.write('%s\n' % nltk.translate.bleu_score.sentence_bleu([ref_list], tran_list))
    else:
        with open(args.translation, 'r') as trans, open(args.reference, 'r') as ref:
            tran_list, ref_list = [], []
            for tl in trans:
                rl = ref.readline()
                tran_list.append(tl.strip().split(' '))
                ref_list.append(rl.strip().split(' '))
        print(nltk.translate.bleu_score.corpus_bleu(ref_list, tran_list))
