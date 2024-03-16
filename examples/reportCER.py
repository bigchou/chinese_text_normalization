
from zhtn.python.api import init_chinese_tn
from zhtn.python.api import testtime_norm
from evaluate import load
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose',action='store_true')
    args = parser.parse_args()
    # set cc_mode to 's2t' for evaluation on zh-TW
    # set cc_mode to 't2s' for evaluation on zh-CN
    normalizer = init_chinese_tn(cc_mode='s2t', to_lower=True)
    hyp_list = ['妳是妳，她是她', '在108年上線']
    ref_list = ['妳是你，他是她', '在一百零八年上線']
    hyp_list_norm, ref_list_norm = [], []
    verbose = True
    # Sanitze the prediction and groundtruth
    for hyp, ref in zip(hyp_list, ref_list):
        hyp_norm = normalizer(hyp)
        hyp_norm_norm = testtime_norm(hyp_norm, ref)
        ref_norm = normalizer(ref)
        hyp_list_norm.append(hyp_norm_norm)
        ref_list_norm.append(ref_norm)
        if args.verbose:
            print('prediction: |%s|'%(hyp))
            print('[AFTER CHINESE_NORM] prediction: |%s|'%(hyp_norm))
            print('[AFTER TESTTIME_NORM] prediction: |%s|'%(hyp_norm_norm))
            print("V.S.")
            print('groundtruth: |%s|'%(ref))
            print('[AFTER CHINESE_NORM] groundtruth: |%s|'%(ref_norm))
            print("-------------------------------")
    # report CER
    cer_metric = load('cer')
    huggingface_cer = cer_metric.compute(references=ref_list_norm, predictions=hyp_list_norm)
    print("CER: %.4f"%(huggingface_cer))
