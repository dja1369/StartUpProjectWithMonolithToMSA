from random import Random

# 모델 선언
model = Random()
model.object_name = ["사과", "바나나", "포도", "딸기"]
model.param = [i for i in range(2000)]


# 이미지를 받아서 처리하는 함수
def process_image(img):
    print("이미지 처리 시작")

    name = model.sample(model.object_name, 1)
    coordinate = model.sample(model.param, 4)

    print("이미지 처리 중")

    result = {"object": name, "coordinate": coordinate}

    print("이미지 처리 완료")
    return result


if __name__ == '__main__':
    target_img = "어쩌구_저쩌구_이미지_경로"

    print(process_image(target_img))
