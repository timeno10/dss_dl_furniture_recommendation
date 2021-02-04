# 가구 추천 시스템 딥러닝 프로젝트
<img src="https://user-images.githubusercontent.com/71831714/106569428-d8569a80-6577-11eb-8dfa-b49ab0f7a36a.png" width='500'></img>

## 개요 

### 주제
- 소비자가 마음에 드는 가구를 발견하면 취향에 가장 맞는 제품 추천
- 이미지 처리 기술과 추천 알고리즘을 결합

### 진행 순서
1. 객체 탐지 및 추출 (Object Detection and Extraction)
2. 특징 추출 (Feature Extraction)
3. 유사도 측정 (Similarity Measure) 후 추천 시스템 (Recommendation System) 구축
4. 가중치 조정 (Fine Tuning)으로 정확도 향상
5. 웹에서 구현

### 일정
기간 : 21/1/25 ~ 21/2/19

1주차(1/25 ~ 1/31) - Detectron2를 활용하여 객체 탐지 및 추출, Tensorflow를 활용하여 특징 추출

2주차(2/1 ~ 2/7) - 유사도 측정, RoboFlow를 활용한 라벨링 작업, 추가 학습을 통한 모델 정확도 향상

3~4주차(2/8 ~ 2/19) - 플라스크를 활용해 웹사이트 개발, 최종 발표 및 PPT 작성, Github 정리

### 목표 설정
- 인테리어 사진을 넣으면 사진 속 가구들을 탐지하여 종류별로 비슷한 가구를 추천해주는 웹사이트 개발

### 역할
김성준 - Detectron2로 Object Detection and Extraction, Tensorflow로 Feature Extraction, Cosine Similarity로 가구 추천, Fine Tuning을 위한 라벨링

유승균 - Detectron2로 Object Detection and Extraction, Docker로 라벨링 협업 시도, Fine Tuning을 위한 라벨링

이정려 - Fine Tuning을 위한 라벨링

전예나 - Faiss, Annoy로 유사도 측정, Fine Tuning을 위한 라벨링

정하윤 - Detectron2 조사, Fine Tuning을 위한 라벨링 툴 조사 및 작업
