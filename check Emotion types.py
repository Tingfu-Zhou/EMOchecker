import pandas as pd

# 读取 CSV 文件
train_sent_emo_path = "D:\\迅雷下载\\archive2\\memotion_dataset_7k\\labels.csv"

# 加载 CSV 数据
texts_df = pd.read_csv(train_sent_emo_path)

# 获取 'Sentiment' 列中的唯一元素种类
unique_sentiments = texts_df['overall_sentiment'].unique()

# 统计种类数量
num_unique_sentiments = len(unique_sentiments)

# 显示种类数量及具体类别
print(num_unique_sentiments, unique_sentiments)
