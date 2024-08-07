from zhtn.python.whisper_normalizers import EnglishTextNormalizer
from zhtn.python.api import init_chinese_tn

if __name__ == "__main__":
    # set cc_mode to 's2t' for evaluation on zh-TW
    # set cc_mode to 't2s' for evaluation on zh-CN
    zh_normalizer = init_chinese_tn(cc_mode='s2t', to_lower=True)
    en_normalizer = EnglishTextNormalizer()

    input_str_list = [
        "八月七日　斯　特she's been like 100 10km 10mm RC232凡·I'd like to play 维 逊斯~基～ApPle为？波65%兰?罗!马天;主?教　教「长」\t",
        "決勝21點"
    ]
    for input_str in input_str_list:
        print('input: |%s|'%(input_str))
        print('zh_tn(input): |%s|'%(zh_normalizer(input_str)))
        print('zh_tn(en_tn(input)): |%s|'%(zh_normalizer(en_normalizer(input_str))))
        print('------------------')

"""
input: |八月七日　斯　特she's been like 10km 10mm RC232凡·I'd like to play 维 逊斯~基～ApPle为？波65%兰?罗!马天;主?教　教「长」 |
zh_tn(input): |八月七日斯特she s been like十km十mm rc兩百三十二凡i d like to play維遜斯基apple爲波百分之六十五蘭羅馬天主教教長|
zh_tn(en_tn(input)): |八月七日斯特she has been like十km十mm rc兩百三十二凡i would like to play維遜斯基apple爲波百分之六十五蘭羅馬天主教教長|
------------------
input: |決勝21點|
zh_tn(input): |決勝二十一點|
zh_tn(en_tn(input)): |決勝二十一點|
------------------
"""