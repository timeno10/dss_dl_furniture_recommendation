# 가구 추천 시스템 딥러닝 프로젝트
<img src="https://user-images.githubusercontent.com/71831714/108008504-d692d980-7043-11eb-8977-4537bbfcaf97.png" width='500'></img>

## Intro

### Topic
- 소비자가 마음에 드는 가구를 발견하면 취향에 가장 맞는 제품 추천
- 이미지 처리 기술과 추천 알고리즘을 결합

### Process
1. 사전 학습 모델을 활용하여 객체 탐지 및 추출
2. 특징 추출 후 유사도 측정
3. 6가지 카테고리로 직접 라벨링한 custom 데이터셋으로 모델링
4. 다양한 모델 성능 비교 후 최적의 모델 선정
5. 모듈화 및 Flask를 활용하여 웹에 추천 시스템 구축

### Timeline
**기간** : 21/1/25 ~ 21/2/19

**1주차(1/25 ~ 1/31)** - Detectron2로 객체 탐지 및 추출, Tensorflow로 특징 추출 및 코사인 유사도 측정

**2주차(2/1 ~ 2/7)** - RoboFlow로 Lamp 라벨링 작업 후 사전 학습 모델에 학습

**3~4주차(2/8 ~ 2/19)** - 6가지 카테고리로 라벨링한 이미지로 학습한 custom 모델 만들기, 모듈화, 웹 구현 

### Goal
- 인테리어 사진을 넣으면 사진 속 가구들을 탐지하여 종류별로 비슷한 가구를 추천해주는 웹사이트 개발

### Roles
김성준

유승균

이정려

정하윤

전예나

## Details

### 1. Detectron2를 사용하여 객체 탐지
- 간단한 코드 작업으로 모델링 가능
- 다양한 사전 학습 모델 보유
- 연산량이 많은 부분을 python이 아닌 CUDA와 C로 구현하여 속도가 빠름

### 2. R-CNN 계열 사전 학습 모델 활용<sup>[1](#footnote_1)</sup>
- **[R-CNN 정리](https://alltimeno1.github.io/archive.html?tag=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D%2F%EB%94%A5%EB%9F%AC%EB%8B%9D "blog link")**
- 영상이 아닌 이미지 처리에 비교적 정확도가 높은 1-Stage Detector 모델 활용
- YOLO보다는 처리 속도가 느리지만 데이터 작기 때문에 정확도를 우선으로 선정

### 3. 객체 특징 추출 및 유사도 측정<sup>[2](#footnote_2)</sup>
- Tensorflow Hub에서 ImageNet으로 학습한 ResNet을 활용하여 객체 특징 추출
- 다양한 방식으로 유사도 측정 후 최적의 방식 선정
```
 1. 최근접 이웃(Annoy 라이브러리)
 2. 코사인 유사도
 3. 맨하탄 거리 
 4. 유클리드 거리
 ```
 
### 4. Transfer Learning
- 사전 학습 모델로는 Lamp를 탐지할 수 없음
- RoboFlow.com에서 1000장 이상의 Lamp 이미지를 직접 라벨링 작업

### 5. Modeling
- 사전 학습 모델이 아닌 직접 라벨링과 학습시키고 미세 조정한 모델 구현으로 프로젝트 방향성 변경
- 인테리어 사진들을 크롤링한 후 6가지 카테고리(테이블, 의자, 시계, 쇼파, 화분, 조명)로 라벨링 작업
- 샘플 학습에 사용될 모델들을 조사하고 전이 학습을 돌린 다음 AP와 직접 Test 이미지들을 보면서 성능 비교 및 최종 모델 선정
```
  Test-set AP scores
  |     Model     |   AP   |  AP50  |  AP75  |  APs   |  APm   |  APl   |
  |:-------------:|:------:|:------:|:------:|:------:|:------:|:------:|
  | Cascade R-CNN | 43.362 | 70.160 | 49.969 | 14.598 | 42.164 | 54.229 |
  | Faster R-CNN  | 45.106 | 74.764 | 48.086 | 17.499 | 44.489 | 53.974 |
  | Mask R-CNN    | 43.566 | 73.468 | 47.526 | 15.102 | 45.112 | 52.546 |
  | EfficientNet  | 43.362 | 70.160 | 49.969 | 14.598 | 42.164 | 54.229 |
  | YOLOv3        | 43.362 | 70.160 | 49.969 | 14.598 | 42.164 | 54.229 |  
  | DenseNet      | 43.362 | 70.160 | 49.969 | 14.598 | 42.164 | 54.229 |
```

### 6. Web
- 코드 모듈화 및 데이터베이스 구축
- Flask를 활용하여 웹사이트에 서비스 구현

### 7. Reference
<a name="footnote_1">[1]</a> Kaiming He, Georgia Gkioxari, Piotr Dollar, Ross Girshick. 2018. "Mask R-CNN". Facebook AI Research (FAIR)<br>
<a name="footnote_2">[2]</a> Dengsheng Zhang, Guojun Lu. 2003. "EVALUATION OF SIMILARITY MEASUREMENT FOR IMAGE RETRIEVAL". International Conference on Neural Networks and Signal Processing
