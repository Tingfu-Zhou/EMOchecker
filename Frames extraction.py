import cv2
import os

# 获取桌面路径（根据操作系统选择合适的代码）
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')  # Windows
# 如果是macOS或Linux，使用下面这行代码：
# desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# 指定视频文件夹的路径
video_folder = r'D:\迅雷下载\archive\MELD-RAW\MELD.Raw\train\train_splits'

# 获取文件夹中的所有视频文件（假设视频文件的扩展名是 .mp4，可以根据需要修改扩展名）
video_files = [os.path.join(video_folder, f) for f in os.listdir(video_folder) if f.endswith('.mp4')]

# 创建一个保存图片的文件夹
output_folder = os.path.join(desktop_path, 'extracted_middle_frames')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 设置最大提取数量
max_images = 200
extracted_count = 0

# 循环处理每个视频文件
for video_path in video_files:
    if extracted_count >= max_images:
        break  # 达到max张后停止

    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    
    # 获取视频的总帧数
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 计算中间帧的位置
    middle_frame = total_frames // 2

    # 设置视频捕获到中间帧
    cap.set(cv2.CAP_PROP_POS_FRAMES, middle_frame)

    # 读取该帧
    ret, frame = cap.read()
    
    if ret:
        # 构造保存的文件路径（保存到桌面的文件夹中）
        video_name = os.path.basename(video_path).split('.')[0]  # 获取视频文件的名称（不带扩展名）
        frame_filename = f'{video_name}_middle_frame.jpg'
        frame_path = os.path.join(output_folder, frame_filename)
        
        # 保存该帧为图片
        cv2.imwrite(frame_path, frame)
        extracted_count += 1  # 计数加一

        print(f'Successfully saved middle frame of {video_name} to {frame_path}')
        
        if extracted_count >= max_images:
            print("Reached the limit of 1000 images. Stopping.")
            break  # 达到max张后停止
    else:
        print(f"Failed to retrieve middle frame for {video_path}")

    # 释放视频捕获对象
    cap.release()

# 释放所有资源
cv2.destroyAllWindows()

print(f"Batch processing completed! Total extracted images: {extracted_count}")

