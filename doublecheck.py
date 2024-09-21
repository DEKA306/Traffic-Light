#print("DoubleCheck(a, b, c)")
def DoubleCheck(a, b, c):
    # 텍스트 파일 읽기
    with open(b, 'r') as f:
        lines = f.readlines()

    class_coords = {0: None, 1: None, 2: None}  # 클래스별 좌표 저장

    # YOLO 형식 좌표 처리
    for line in lines:
        data = line.split()
        class_id = int(data[0])
        center_y = float(data[2])
        height = float(data[4])

        # 좌상단 및 우하단 y 좌표 계산
        ymin = center_y - (height / 2)
        ymax = center_y + (height / 2)
        middle_y = (ymin + ymax) / 2  # 중간점 y 좌표

        # 필요한 클래스에 따라 좌표 저장
        if class_id in class_coords:
            class_coords[class_id] = (ymin, ymax, middle_y)

    # Class 0 또는 Class 1과 Class 2의 좌표 비교
    if c == "r" and class_coords[1] and class_coords[2]:
        return class_coords[1][1] < class_coords[2][2]  # Class 1의 ymax와 Class 2의 중간점 비교

    if c == "g" and class_coords[0] and class_coords[2]:
        return class_coords[0][0] > class_coords[2][2]  # Class 0의 ymin과 Class 2의 중간점 비교

    return None  # 필요한 클래스가 없으면 None 반환

# 함수 사용 예시
#result = compare_y_coordinates('C:/Users/soen/Desktop/img/20240914_135620.jpg', 'C:/Users/soen/Desktop/img/20240914_135620.txt', 'g')
#print(result)
