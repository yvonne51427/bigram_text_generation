import random
import pickle

# 從文件中讀取 bigram 模型
with open('bigram_model.pkl', 'rb') as f:
    bigram = pickle.load(f)

generate = str()
curr_ch = "<BOS>"
while curr_ch != "<EOS>":
    generate += curr_ch
    prob = bigram[curr_ch]
    elements = [k for k in prob]
    weights = [prob[k] for k in prob]
    curr_ch = random.choices(elements, weights=weights, k=1)[0]
print(generate + curr_ch)
