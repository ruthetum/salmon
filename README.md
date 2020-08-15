# 자연어 처리를 활용한 온라인 강의 학습 보조 서비스 개발
## 2020-1 성균관대학교 Co-Deep Learning 출품작

- **프로젝트 설명**: 자연어 처리를 활용한 온라인 강의 학습 보조 서비스 개발
- **공모전 일자**: 2020.05 ~ 2020.07
- **주관**: 성균관대학교 대학혁신과공유센터

https://skku-tnt.github.io/2020/08/01/%EC%BD%94%EB%94%A5%EB%9F%AC%EB%8B%9D-1%ED%95%99%EA%B8%B0-%EC%9E%90%EC%97%B0%EC%96%B4%EC%B2%98%EB%A6%AC.html

## 🔔 기능 설명
- **강의 스크립트 추출** : Google Cloud의 STT(Speeech to Text) API를 활용해 스크립트 추출
- **강의 내용에 대한 워드 클라우드 제공** : 스크립트 분석을 통해 핵심 단어 추출 후 워드 클라우드 제공 
- **강의 내용에 대한 퀴즈 생성** -> 핵심 단어가 등장하는 지점에 Ko-GPT2를 이용해 퀴즈 생성 후 제공
![image](https://user-images.githubusercontent.com/59307414/89879275-a6cec900-dbfd-11ea-9588-af9dc7314ef1.png)
- **강의 내용 필기 및 저장/추출 환경 제공** : 코넬식 노트를 온라인 상에서 작성/수정하고 해당 내용을 PDF파일로 저장


## 🔔 프로토타입
- 플레이어
![image](https://user-images.githubusercontent.com/59307414/89881299-4b520a80-dc00-11ea-8707-cfb4d3e1c735.png)

- 코넬식 노트 작성
![image](https://user-images.githubusercontent.com/59307414/89880075-c1ee0880-dbfe-11ea-9981-a97c316d7ce6.png)

- PDF 파일 저장
![image](https://user-images.githubusercontent.com/59307414/89880405-2a3cea00-dbff-11ea-94ca-885fef0c48f3.png)
