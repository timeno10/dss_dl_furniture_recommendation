# 가구 추천 시스템 딥러닝 프로젝트
<img src="https://user-images.githubusercontent.com/71831714/108008504-d692d980-7043-11eb-8977-4537bbfcaf97.png" width='500'></img>

## Intro

### Topic
- 소비자가 마음에 드는 가구를 발견하면 취향에 가장 맞는 제품 추천
- 이미지 처리 기술과 추천 알고리즘을 결합

### Process
1. 사전 학습 모델을 활용하여 객체 탐지 및 크로핑
2. 특징 추출 후 유사도 측정
3. 6가지 카테고리로 직접 라벨링한 custom 데이터셋으로 전이 학습
4. 다양한 모델 성능 비교 후 최적의 모델 선정
5. 모듈화를 통한 추천 시스템 구축

### Timeline
**기간** : 21/1/25 ~ 21/2/19

**1주차(1/25 ~ 1/31)** - Detectron2로 객체 탐지 및 추출, 특징 추출 및 유사도 측정

**2주차(2/1 ~ 2/7)** - RoboFlow로 6가지 가구 카테고리 라벨링 작업 후 사전 학습 모델에 전이 학습

**3~4주차(2/8 ~ 2/19)** - 모델 간 성능 비교, 최적의 추천 알고리즘 비교, 모듈화 

### Goal
- 인테리어 사진을 넣으면 사진 속 가구들을 탐지하여 종류별로 비슷한 가구를 추천

### Roles
김성준 - 사전 학습 모델로 객체 탐지 및 크로핑, R-CNN계열 모델들 학습 및 테스트, 3가지 방식으로 유사도 측정, 특정 상품에 대한 추천 가중치 설정, 크로핑과 특징 추출 파트 모듈화, Readme 작성

유승균 - 

이정려 - 

정하윤 - 

전예나 - 

## Details

### 1. Detectron2를 사용하여 객체 탐지 및 크로핑
- 간단한 코드 작업으로 모델링 가능
- 다양한 사전 학습 모델 보유
- 연산량이 많은 부분을 python이 아닌 CUDA와 C로 구현하여 속도가 빠름

### 2. R-CNN 계열 사전 학습 모델 활용<sup>[1](#footnote_1)</sup>
- **[R-CNN 정리](https://alltimeno1.github.io/archive.html?tag=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D%2F%EB%94%A5%EB%9F%AC%EB%8B%9D "blog link")**
- 이미지 처리에서 비교적 정확도가 높은 1-Stage Detector 모델 활용
- YOLO보다 처리 속도는 느리지만 데이터가 작기 때문에 정확도를 우선으로 선정

### 3. 객체 특징 추출 및 유사도 측정<sup>[2](#footnote_2)</sup>
- Tensorflow Hub에서 ImageNet으로 학습한 ResNet을 활용하여 객체 특징 추출
- Annoy와 Faiss 라이브러리를 활용하여 유사도 측정 후 최적의 방식 선정
```
 1. 최근접 이웃
 2. 코사인 유사도
 3. 맨하탄 거리 
 4. 유클리드 거리
 ```
 - 특정 상품에 추천 가중치 부여(가격, 제품 등록일 활용)
 
### 4. 전이 학습
- 사전 학습 모델로는 Lamp를 탐지할 수 없음
- 필요한 카테고리를 직접 라벨링하고 전이 학습시키는 쪽으로 프로젝트 계획 수정
- 인테리어 사진들을 크롤링한 후 6가지 카테고리(테이블, 의자, 시계, 쇼파, 화분, 조명)로 라벨링 작업
- 샘플 학습에 사용될 모델들을 조사하고 전이 학습을 돌린 다음 AP와 직접 Test 이미지들을 보면서 성능 비교 및 최종 모델 선정
```
  Test-set AP scores
  |     Model     |   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
  |:-------------:|:------:|:------:|:------:|:------:|:------:|:------:|
  | Cascade R-CNN | 43.362 | 70.160 | 49.969 | 14.598 | 42.164 | 54.229 |
  | Faster R-CNN  | 45.106 | 74.764 | 48.086 | 17.499 | 44.489 | 53.974 |
  | Mask R-CNN    | 43.566 | 73.468 | 47.526 | 15.102 | 45.112 | 52.546 |
  | EfficientNet  |
  | YOLOv3        | 
  | DenseNet      | 
```

### 5. 추천 시스템 구축
- 전이 학습으로 나온 weight 파일 저장
- 추천해줄 아이템 이미지들을 사전에 특징 추출하여 csv 파일로 저장
- 코드 모듈화를 통해 빠르고 간편하게 실행 가능하도록 정리
- 모듈 파일 사용법
```
1. !git clone https://github.com/alltimeno1/dss_dl_furniture_recommendation.git
2. SungJun/module/pics/input.jpg을 원하는 인테리어 사진으로 대체
3. cropping.py, feature_extraction.py 실행
- test.ipynb 참조
```

## Reference

<a name="footnote_1">[1]</a> Kaiming He, Georgia Gkioxari, Piotr Dollar, Ross Girshick. 2018. "Mask R-CNN". Facebook AI Research (FAIR)<br>
<a name="footnote_2">[2]</a> Dengsheng Zhang, Guojun Lu. 2003. "EVALUATION OF SIMILARITY MEASUREMENT FOR IMAGE RETRIEVAL". International Conference on Neural Networks and Signal Processing
