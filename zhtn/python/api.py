from .cn_tn import TextNorm
import jiwer
from itertools import product
import opencc

class ZhNormalizer():
    def __init__(self, tn, cc_mode):
        self.tn = tn
        self.converter = opencc.OpenCC(cc_mode)
    
    def __call__(self, text):
        return self.converter.convert(self.tn(text))

def init_chinese_tn(
    cc_mode='s2t',
    to_banjiao=False,
    to_upper=False,
    to_lower=False,
    remove_fillers=False,
    remove_erhua=False,
    check_chars=False,
    remove_space=True,
):
    assert cc_mode in ['s2t', 't2s'], "please choose the valid cc_mode"
    #to_banjiao = False # 好像跟全形半形有關
    #to_upper = False # 全部變大寫
    #to_lower = False # 全部變小寫
    #remove_fillers = False # remove filler chars such as "呃, 啊"
    #remove_erhua = False # remove erhua chars such as "他女儿在那边儿 -> 他女儿在那边"
    #check_chars = False # skip sentences containing illegal chars
    #remove_space = True # remove whitespace
    #cc_mode = '' # convert between traditional to simplified <--- openCC
    #cc_mode = 's2t'
    tn = TextNorm(
        to_banjiao = to_banjiao,
        to_upper = to_upper,
        to_lower = to_lower,
        remove_fillers = remove_fillers,
        remove_erhua = remove_erhua,
        check_chars = check_chars,
        remove_space = remove_space,
        cc_mode = cc_mode,
    )
    return ZhNormalizer(tn, cc_mode)

def it_normalize(text):
    # https://www.douban.com/group/topic/43100368/?_i=0215783iSOIfEY
    #roi_text = ['她', '它', '他'] if test_option == 0 else ['她', '它','他']
    #基本解释：妳、你
    # 簡體、繁體的 你、妳  字相同
    # 簡體、繁體的 她、它、他 字相同
    roi_text1 = ['妳', '你']
    roi_text2 = ['她', '它', '他']
    roi_text = roi_text1 + roi_text2

    pos_list = []
    for i, v in enumerate(text):
        if v in roi_text:
            pos_list.append(i)
    if len(pos_list) == 0:
        return [text]
    else:
        input_string = ''.join(roi_text)
        output_combinations = [''.join(p) for p in product(input_string, repeat=len(input_string))]
        hyp_cand = [list(text) for i in output_combinations]
        for i, cand_text in enumerate(output_combinations):
            for pos, char in zip(pos_list, cand_text):
                if hyp_cand[i][pos] in roi_text1 and char in roi_text1:
                    hyp_cand[i][pos] = char
                elif hyp_cand[i][pos] in roi_text2 and char in roi_text2:
                    hyp_cand[i][pos] = char
        return list(set([''.join(i) for i in hyp_cand]))

def testtime_norm(hyp, ref):
    hyp_cand_list = it_normalize(hyp)
    tmp_list = []
    cer_list = []
    for hyp in hyp_cand_list:
        tmp = jiwer.process_characters(ref,hyp)
        tmp_list.append(tmp)
        cer_list.append(tmp.cer)
    min_idx = cer_list.index(min(cer_list))
    tmp = tmp_list[min_idx]
    hyp = hyp_cand_list[min_idx]
    return hyp