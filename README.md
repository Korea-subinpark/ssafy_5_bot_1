# Chat-bot

## 1. 스펙(Specification)
<hr>

### 구현된 어플리케이션의 주요 기능
1. 사용자가 원하는 브랜드의 카페를 입력하면 카페의 이벤트 페이지를 크롤링하여 보여준다.
2. 메뉴를 추천해 준다.

## 2. 회고(Retrospective)
<hr>

### 어플리케이션 구현 과정에서의 어려움과 문제점
1. 시스템 구성상 응답시간이 오래걸려 요청이 반복되고 중복된 응답이 뒤늦게 여러번 출력되는 현상
- 요청을 Queue에 넣고 곧바로 응답을 보낸 뒤에 차례로 처리한다.
2. 크롤링한 데이터를 가공
- replace 함수와 strip 함수 사용

## 3. 보완 계획(Feedback)
<hr>

### 현재 미완성이지만 추가로 구현할 기능 및 기존 문제점 보완 계획
1. 여러가지 브랜드 추가
2. 브랜드별 메뉴판 출력
3. 현재 위치와 가까운 카페의 이벤트 출력
