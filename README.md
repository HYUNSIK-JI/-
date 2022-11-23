# 키보드워리어

> 키보드 중고 거래, 사용자 맞춤형 키보드 추천 서비스, 검색 서비스, 키보드 후기 제공 해주는 사이트



## 프로젝트 소개

- 🗓**프로젝트 기간**
  - 2022.11.09 (수) ~ 2022.11.21 (월)
- 💻**사용 기술**
  - Python, Django, HTML, CSS, Javascript, Bootstrap5, Selenium, Beautifulsoup4
- ⭐**개발 역할 분담**
  - 팀장: 하승찬, 발표자: 유순일, PPT 제작자: 박선영, 문재윤, 지현식
  - **백엔드**: 지현식, 하승찬, 유순일
  - **프론트엔드**: 박선영, 문재윤



## 🚩목적

Django를 통해 

내가 이 기능에 어떻게 접근, 그 과정에서 이슈들을 해결
ex) 무한스크롤, 레디스 소켓 사용



## 모델 구조, ERD 작성

![키보드워리어 최종 ERD](readme_media\키보드워리어 최종 ERD.png)



## 기능

### 제품 정보 수집

- 크롤링 



### Articles/main
- 메세지 알림 
- 전체 방문자 수, 오늘 방문자 수 표시
![articles_main(알림,방문자수)-min](https://user-images.githubusercontent.com/108650777/203498719-73da91bd-bc40-40d6-8747-ae6ee5819746.gif)

- 사용자 맞춤형 키보드 추천
  - 사용자가 회원가입시 입력한 정보를 기반으로 키보드를 추천하는 기능
![키보드추천](https://user-images.githubusercontent.com/108650777/203497876-23d077cb-d4da-4428-8814-a0ae4e15485f.gif)


### Articles/all

- 비동기 무한 스크롤
- 비동기 키보드 필터링
- 비동기 키보드 검색 기능
![aritcles_all](https://user-images.githubusercontent.com/108650777/203497932-65b5749c-9ee2-4e11-8106-1d6f6586f04f.gif)



### Articles/detail 

- 키보드 후기 평균 별점을 보여줌
- 댓글 욕설 필터링
![articles_detail (1)](https://user-images.githubusercontent.com/108650777/203498069-165cb150-b14a-46d0-bfe3-1b82496fff57.gif)


### Trade/index

- 키보드 이름, 리뷰 제목 검색 기능
- 라디오 버튼을 통해 판매글만, 구매글만 선택 가능
- 키보드, 판매글 검색
![trade_index-min](https://user-images.githubusercontent.com/108650777/203499220-65e889b3-aa1b-4c54-8c31-dbc849b8a0ab.gif)



### Trade/detail

- 비동기 게시글 찜하기
- 비동기 댓글 생성 및 삭제
- 게시글 사진 여러 장
- 채팅 (비동기 채팅, DB저장)
![trade_detail](https://user-images.githubusercontent.com/108650777/203499830-7b8cb0f3-20e4-4aae-9756-c8e91599d9c8.gif)



### Trade/create

키보드모델명 쉽게검색
사진 여러장 추가 
![trade_create](https://user-images.githubusercontent.com/108650777/203498331-c31b9a0c-4e5a-4d5b-abf2-80b8263b2067.gif)



### Reviews/index


### Reviews/detail

비공기 글 좋아요
비동기 댓글 삭제, 생성
비동기 댓글 좋아요
닷글 욕설 필터링
![reviews_detail-min](https://user-images.githubusercontent.com/108650777/203500064-3c043c2a-af19-4d2b-83e8-d30cc648d101.gif)





### Reviews/create

키보드 모델명 쉽게 검색
별점선택 
![reviews_create](https://user-images.githubusercontent.com/108650777/203500675-05282a42-8cf0-4a32-84ea-f3f28fdf5eaf.gif)



### Accounts/detail

10. 어카운트
    소셜계정로그인
    로그인시 선호 키보드정보 가져오기 

11. 마이페이지
    라디오버튼 메뉴
    비동기 팔로우
    ![accounts_detail](https://user-images.githubusercontent.com/108650777/203498275-89efa132-36ab-44e0-bc30-99fe4c86685e.gif)


### Chat


12. 채팅 

배포시 반실시간 채팅구현
로컬시 채팅기능구현 
![chat](https://user-images.githubusercontent.com/108650777/203498212-d7c228ae-2e7c-451d-827a-1697f541c8b7.gif)

13. 기타 중요기능
알림기능
