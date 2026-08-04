import os
import shutil

# 정리할 대상 폴더 (현재 스크립트가 있는 폴더)
TARGET_DIR = os.path.dirname(os.path.abspath(__file__))

# 폴더 정리 중 건드리면 안 되는 것들 (스크립트 자기 자신)
SCRIPT_NAME = os.path.basename(__file__)


def organize_files(target_dir: str) -> None:
    # 대상 폴더 안의 항목들을 하나씩 확인
    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)

        # 폴더는 건너뛴다 (이미 정리된 하위 폴더 포함)
        if os.path.isdir(file_path):
            continue

        # 스크립트 자기 자신은 건너뛴다
        if filename == SCRIPT_NAME:
            continue

        # 확장자 추출 (예: "image.jpg" -> "jpg")
        ext = os.path.splitext(filename)[1].lstrip(".").lower()

        # 확장자가 없는 파일은 "no_extension" 폴더로 분류
        folder_name = ext if ext else "no_extension"

        # 확장자별 하위 폴더 경로 생성
        dest_folder = os.path.join(target_dir, folder_name)
        os.makedirs(dest_folder, exist_ok=True)

        # 파일을 해당 확장자 폴더로 이동
        dest_path = os.path.join(dest_folder, filename)
        shutil.move(file_path, dest_path)
        print(f"이동: {filename} -> {folder_name}/")


if __name__ == "__main__":
    organize_files(TARGET_DIR)
    print("파일 정리가 완료되었습니다.")
