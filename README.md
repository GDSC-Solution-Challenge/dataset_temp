![image](https://user-images.githubusercontent.com/84952598/218294009-6baa5c9e-e651-4c65-b685-08873247da4e.png)


AI HUB_ 생활폐기물 데이터 입니다
Validation 기준 37기가, Train set 기준 280 기가 정도 되어서 일단은 validation set 및 train set에서의 '헷갈리는 친구들' 위주로 데이터셋 가져와서 학습시키려고 합니다.

Kaggle에 비슷한 task가 많아서 일단은 캐글 공부해가면서 비슷하게 모델링 진행해볼까 합니다(비전쪽 지식이 많진 않아서)

하나의 instance에 대해 5번의 구도로서 촬영된 것인데, 그냥 용량 문제로 5장 중 1장씩만 떼왔습니다.
차피 data auguemntation시키면 되어서, 굳이 필요없을거 같기도 해서 그렇게 처리했습니다.

데이터 중간에 다운로드가 끊겨서, 원본데이터는 15기가 정도 될 것 같고, 단순 나누기 5하면 올라갈 데이터는 3기가 정도 됩니다.
이미 json file(라벨링 bounding box) 있긴 한데, json_catcher.py 써서 해당 json 파일들에 대해서만 붙여 놓으면 될것 같습니다.

아마 yolov4를 쓸 것 같고,
ai hub 상에 이미 객체탐지 모델은 5기가 정도로 되어서 탑재는 되어있습니다.

일단 당장은 recycleable 여부만 판단하는 형식으로 1차 모델 design 진행해서 실제 앱에 탑재해서 성능 검증 해보고,
괜찮으면 recyclable 여부 및 객체 탐지 자체까지 진행해볼 예정입니다. 2월20일 정도까지 모델까지 연구실에서 학습 빡세게 시켜서 진행해볼 것 같습니다:)
