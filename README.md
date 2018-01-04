# HEVEN_AutonomousCar_2018
2018 International Student Car Competition: Autonomous Car SKKU Team. HEVEN

[위키 작성법(마크다운 문서)](https://gist.github.com/ihoneymon/652be052a0727ad59601)

팀원 11명

## 역할 미정
* 김원혁
* 김효경

## 알고리즘
1. Vision 데이터 처리
	1. 차선 인식
	2. 표지판 인식
  
2. LiDAR 데이터 처리
	1. 장애물 인식
  
3. 경로 설정
	1. 목표점 설정
	2. 장애물과 차선 회피 경로 설정
  
4. 제어
	1. 조향
	2. 속도
	3. 미션 별 제어
  
## 비전 데이터 파싱 및 처리
### 팀원
* 이중구
* 이용호
### 담당
* 차선 인식
* 표지판 인식
* 비전 머신러닝

## 주행 알고리즘
### 팀원
* 김홍빈
* 박준혁
* 김성우
### 담당
* 경로 탐색 알고리즘
* 제어 알고리즘
* 미션 별 알고리즘: `주차, 유턴, 동적 장애물, 횡단보도 등`

## 분산처리 및 GPU연산
### 팀원
* 김인엽
* 이민영
* 유성룡
### 담당
* 연산 속도 상승
* CUDA for python