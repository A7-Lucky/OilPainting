from datetime import datetime
import cv2
import numpy as np


def inference(img_input, style):
    # 이미지 불러오기
    npimg = np.fromstring(img_input, np.uint8)
    input_img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    style = cv2.dnn.readNetFromTorch(f"articles/models/{style}")

    # 전처리 코드
    h, w, c = input_img.shape
    input_img = cv2.resize(input_img, dsize=(500, int(h / w * 500)))
    MEAN_VALUE = [103.939, 116.779, 123.680]
    blob = cv2.dnn.blobFromImage(input_img, mean=MEAN_VALUE)

    # 결과 추론하기
    style.setInput(blob)
    output = style.forward()
    # 전처리한 이미지(blob)를 모델에 넣고 추론, output 변수에 추론한 결과 저장(forward)

    # 결과 후처리
    output = output.squeeze().transpose((1, 2, 0))
    output += MEAN_VALUE
    output = np.clip(output, 0, 255)
    output = output.astype("uint8")

    # 생성시간을 이름으로 저장
    time = datetime.now().strftime("%y%m%d%H%M%S")
    cv2.imwrite(f"media/article/{time}.jpeg", output)
    result = f"media/article/{time}.jpeg"

    return result
