import os
import shutil

# 텍스트 파일 경로 및 지정 경로
source_list_path = '/DB/DB_single_ch/validation/validation_file_destination.txt'  # 파일 경로가 적힌 텍스트 파일
destination_dir = '/DB/DB_single_ch/validation'  # 파일을 옮길 목적지 디렉토리

# 목적지 디렉토리가 존재하지 않으면 생성
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# 텍스트 파일 열기
with open(source_list_path, 'r') as file:
    lines = file.readlines()

# 파일 경로를 한 줄씩 읽어서 옮기기
for line in lines:
    source_path = line.strip()  # 줄 끝의 공백 제거

    # 파일 존재 여부 확인
    if os.path.exists(source_path):
        try:
            # 파일명 추출
            file_name = os.path.basename(source_path)
            
            # 새로운 파일 경로 생성
            destination_path = os.path.join(destination_dir, file_name)
            
            # 파일 이동
            shutil.move(source_path, destination_path)
            print(f'Successfully moved {source_path} to {destination_path}')
        except Exception as e:
            print(f'Error moving {source_path} to {destination_path}: {e}')
    else:
        print(f'File does not exist: {source_path}')

