import requests
from bs4 import BeautifulSoup as BS
from tqdm import tqdm
import time
import random

corpus = list()
 #三國演義 120 回的 ID 分佈在 67 ~ 186 之間
for iid in tqdm(range(67, 186 + 1)):
    data = {"bid": 12, "id": iid}
    try:
        res = requests.post("http://open-lit.com/GETbook.php", data=data)
        res.raise_for_status()  # 檢查請求是否成功
        soup = BS(res.text, 'html.parser')
        corpus.append(soup.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed for id {iid}: {e}")
    time.sleep(random.uniform(0.5, 1.5))  # 隨機延遲 0.5 到 1.5 秒

print("Data collection complete.")

# 將 corpus 保存到文件中，以便在後續腳本中使用
with open('corpus.txt', 'w', encoding='utf-8') as f:
    for text in corpus:
        f.write(text + '\n')
