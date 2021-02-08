# 가구 추천 시스템 딥러닝 프로젝트
<img src="https://user-images.githubusercontent.com/71831714/106569428-d8569a80-6577-11eb-8dfa-b49ab0f7a36a.png" width='500'></img>

## Intro

### Topic
- 소비자가 마음에 드는 가구를 발견하면 취향에 가장 맞는 제품 추천
- 이미지 처리 기술과 추천 알고리즘을 결합

### Process
1. 객체 탐지 및 추출 (Object Detection and Extraction)
2. 특징 추출 (Feature Extraction)
3. 유사도 측정 (Similarity Measure) 후 추천 시스템 (Recommendation System) 구축
4. 가중치 조정 (Fine Tuning)으로 정확도 향상

### Timeline
기간 : 21/1/25 ~ 21/2/19

1주차(1/25 ~ 1/31) - Detectron2로 객체 탐지 및 추출, Tensorflow로 특징 추출 및 코사인 유사도 측정

2주차(2/1 ~ 2/7) - RoboFlow로 Lamp 라벨링 작업 후 사전 학습 모델에 새로운 클래스로 학습

3~4주차(2/8 ~ 2/19) - 

### Goal
- 인테리어 사진을 넣으면 사진 속 가구들을 탐지하여 종류별로 비슷한 가구를 추천해주는 웹사이트 개발

### Roles
김성준 - Detectron2로 객체 탐지, Tensorflow로 특징 추출 및 코사인 유사도를 활용한 가구 추천, Lamp Fine Tuning

유승균 - Detectron2로 객체 탐지, YOLO를 활용한 모델링

이정려

정하윤 - Detectron2 조사 및 활용 제시, 라벨링 사이트 조사 및 작업

전예나

## Details

### 1. Detectron2를 사용하여 객체 탐지
- 간단한 코드 작업으로 모델링 가능
- 다양한 사전 학습 모델 보유
- 연산량이 많은 부분을 python이 아닌 CUDA와 C로 구현하여 속도가 빠름

### 2. 사전 학습 모델인 Faster R-CNN을 활용
- **[Faster R-CNN](https://alltimeno1.github.io/2021/02/05/faster_rcnn.html "blog link")**
- 영상이 아닌 이미지 처리에 비교적 정확도가 높은 모델
- YOLO보다는 처리 속도가 느리지만 데이터 작기 때문에 정확도를 우선으로 선정

### 3. 객체 특징 추출 및 유사도 측정
- 유사도를 측정하기 위해 Tensorflow를 활용하여 객체에서 특징 추출
- 코사인 유사도를 활용하여 데이터베이스에서 가장 유사한 사진 탐색

### 4. Fine Tuning
- 사전 학습 모델로는 Lamp를 탐지할 수 없음
- RoboFlow.com에서 1000장 이상의 Lamp 이미지를 직접 라벨링 작업
- Detectron2의 사전 학습 모델에 추가 학습
- 최초 학습 결과 정확도가 높지 않았음
