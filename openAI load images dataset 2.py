import os
import csv
from openai import OpenAI

# 初始化OpenAI客户端
client = OpenAI()

# 图片文件夹路径
folder_path = "D:\\迅雷下载\\archive2\\memotion_dataset_7k\\images"

file_num = 100

# 获取文件夹中的所有图片文件路径并进行排序，然后选择前100个文件
file_paths = sorted(
    [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(('.jpg', '.png', '.jpeg'))],
    key=lambda x: int(os.path.basename(x).split('_')[1].split('.')[0])  # 按文件名中的数字部分进行排序
)[:file_num]  # 选择排序后的前100个文件

# 保存上传文件的ID
file_ids = []

# 批量上传图片文件
for file_path in file_paths:
    with open(file_path, "rb") as file:
        response = client.files.create(file=file, purpose='vision')
        file_id = response.id
        file_ids.append(file_id)  # 将文件ID保存到列表中
        print(f"Uploaded {file_path} with ID {file_id}")

# 打印所有上传的文件ID
print("All uploaded file IDs:", file_ids)

# 保存到桌面的 CSV 文件
desktop_path = "C:\\Users\\tingf\\Desktop\\uploaded_file_ids.csv"
with open(desktop_path, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["File ID"])  # 写入表头
    for file_id in file_ids:
        writer.writerow([file_id])

print("File IDs have been saved to uploaded_file_ids.csv")
