import os
from ultralytics import YOLO
import cv2

model = YOLO('best.pt')

# 절대 경로 설정
folder_path = 'C:/Users/soen/Desktop/Trafffic'

# 폴더 내의 파일 목록 가져오기
try:
    file_names = os.listdir(folder_path)

    for file_name in file_names:
        if file_name.lower().endswith('.jpg'):
            # .jpg 확장자 제거
            name_without_extension = os.path.splitext(file_name)[0]
            # 이미지 파일의 전체 경로 설정
            image_path = os.path.join(folder_path, file_name)
            image = cv2.imread(image_path)
            
            if image is None:
                print(f"Error: Unable to read image {image_path}")
                continue

            height, width, _ = image.shape

            # 객체 감지 수행
            results = model.predict(image)

            # 결과를 파일에 저장
            output_file = os.path.join(folder_path, name_without_extension + '.txt')

            with open(output_file, 'w') as file:
                for result in results:
                    boxes = result.boxes.xyxy  # x1, y1, x2, y2 좌표
                    classes = result.names  # 클래스 이름

                    for box, cls in zip(boxes, result.boxes.cls):
                        x1, y1, x2, y2 = map(int, box)
                        class_id = int(cls)
                        
                        # 좌표를 비율로 변환
                        x_center = (x1 + x2) / 2 / width
                        y_center = (y1 + y2) / 2 / height
                        w = (x2 - x1) / width
                        h = (y2 - y1) / height

                        # 파일에 YOLO 형식으로 저장
                        file.write(f"{class_id} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}\n")

except FileNotFoundError as e:
    print(f"Error: {e}")
