import pandas as pd
import os

# CSV 파일 경로
csv_file_path = 'metadata.csv'

# CSV 파일 읽기
df = pd.read_csv(csv_file_path)
new_path = open('./new_path.txt', 'w')

# 파일명 변경 작업
for index, row in df.iterrows():
    old_file_path = row['file_name']
    new_file_name = row['audio_id']
    new_file_name += '.wav'
    
    # 파일의 디렉토리 경로와 기존 파일명을 분리
    dir_path, old_file_name = os.path.split(old_file_path)
    
    # 새로운 파일 경로 생성
    new_file_path = os.path.join(dir_path, new_file_name)
    print(new_file_path)
    new_path.write(new_file_path+'\n')

    try:
        # 파일명 변경
        os.rename(old_file_path, new_file_path)
        print(f'Successfully renamed {old_file_path} to {new_file_path}')
    except Exception as e:
        print(f'Error renaming {old_file_path} to {new_file_path}: {e}')

