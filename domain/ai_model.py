from random import Random

from domain.entity import InferenceEntity


# 모델 선언
class AIModel:
    def __init__(self):
        """
        인공지능 모델
        :param None:
        :return None:
        """
        self.model = Random()
        self.model_object_name = ["사과", "바나나", "포도", "딸기"]
        self.model_param = [i for i in range(2000)]

    # 이미지를 받아서 처리하는 함수
    def process_image(self, img):
        """
        이미지 를 받아서 처리하는 함수
        :param img:
        :return InferenceEntity:
        """
        print("이미지 처리 시작")

        name = self.model.sample(self.model_object_name, 1)
        coordinate = self.model.sample(self.model_param, 4)

        print("이미지 처리 중")

        result = InferenceEntity(image=img, object=name, coordinate=coordinate)

        print("이미지 처리 완료")
        return result
