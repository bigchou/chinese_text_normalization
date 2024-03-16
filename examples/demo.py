
from zhtn.python.api import init_chinese_tn

if __name__ == "__main__":
    # set cc_mode to 's2t' for evaluation on zh-TW
    # set cc_mode to 't2s' for evaluation on zh-CN
    normalizer = init_chinese_tn(cc_mode='s2t', to_lower=True)
    print(normalizer)
    input_str_list = [
        ' 　斯　特凡·维 逊斯~基～ApPle为？波兰罗!马天主?教　教「长」 \n',
        '決勝21點',
        '打戲特效100分',
        '2.5平方电线',
        '人口\t約佔0.4%',
        '成交單價為每坪60-98萬元',
        '140.112',
        '我在2018年',
        '15日李元君进子龙门',
        '2018年登进式第三甲第47名'
    ]
    for input_str in input_str_list:
        print('input: |%s|'%(input_str))
        print('output: |%s|'%(normalizer(input_str)))
        print('------------------')
