from collections import Counter, defaultdict

# 得到每個詞的下個詞的權重分佈比例
# \u3000 為全形空白
skip_symbols = ["\u3000", "\r", "\t", "\n"]
bigram = defaultdict(Counter)

# 從文件中讀取 corpus
with open('corpus.txt', 'r', encoding='utf-8') as f:
    corpus = f.readlines()

for data in corpus:
    # 只有中文所以將空白字元移除
    # 減少語言模型學到過於偏頗的機率分佈
    for sym in skip_symbols:
        data = data.replace(sym, "")

    # 以 <BOS> 代表文本開頭，開始統計整份文本
    prev_char = "<BOS>"
    for ch in data:
        bigram[prev_char][ch] += 1
        prev_char = ch

    # 以 <EOS> 代表文本結尾
    ch = "<EOS>"
    bigram[prev_char][ch] += 1

# 將 bigram 模型保存到文件中
import pickle
with open('bigram_model.pkl', 'wb') as f:
    pickle.dump(bigram, f)
