from ast import Continue
import os
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

while True :
    a = input('팀 또는 나라를 입력하세요 :')
    
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(3)
    
    #맨시티
    if a == "맨시티":
        driver.get("https://www.livesport.com/kr/team/manchester-city/Wtn9Stg0/")

    #리버풀
    if a == "리버풀":
        driver.get("https://www.livesport.com/kr/team/liverpool/lId4TMwf/")
    
    #첼시
    if a == "첼시":
        driver.get("https://www.livesport.com/kr/team/chelsea/4fGZN2oK/")
    
    #토트넘
    if a == "토트넘":
        driver.get("https://www.livesport.com/kr/team/tottenham/UDg08Ohm/")

    #아스날
    if a == "아스날":
        driver.get("https://www.livesport.com/kr/team/arsenal/hA1Zm19f/")

    #맨체스터 유나이티드
    if a == "맨체스터 유나이티드":
        driver.get("https://www.livesport.com/kr/team/manchester-united/ppjDR086/")
    if a == "맨유":
        driver.get("https://www.livesport.com/kr/team/manchester-united/ppjDR086/")
        
    #웨스트햄
    if a == "웨스트햄":
        driver.get("https://www.livesport.com/kr/team/west-ham/Cxq57r8g/")
        
    #울버햄튼
    if a == "울버햄튼":
        driver.get("https://www.livesport.com/kr/team/wolves/j3Azpf5d/")
        
    #레스터
    if a == "레스터":
        driver.get("https://www.livesport.com/kr/team/leicester/KrrdAMyI/")
        
    #브라이튼
    if a == "브라이튼":
        driver.get("https://www.livesport.com/kr/team/brighton/2XrRecc3/")
        
    #브렌트퍼드
    if a == "브렌트퍼드":
        driver.get("https://www.livesport.com/kr/team/brentford/xYe7DwID/")
        
    #뉴캐슬 Utd
    if a == "뉴캐슬":
        driver.get("https://www.livesport.com/kr/team/newcastle-utd/p6ahwuwJ/")

    if a == "뉴캐슬 유나이티드":
        driver.get("https://www.livesport.com/kr/team/newcastle-utd/p6ahwuwJ/")

    #크리스탈팰리스
    if a == "크리스탈팰리스":
        driver.get("https://www.livesport.com/kr/team/crystal-palace/AovF1Mia/")
        
    #아스톤 빌라
    if a == "아스톤 빌라":
        driver.get("https://www.livesport.com/kr/team/aston-villa/W00wmLO0/")
        
    #사우샘프턴
    if a == "사우샘프턴":
        driver.get("https://www.livesport.com/kr/team/southampton/WdKOwxDM/")
        
    #에버튼
    if a == "에버튼":
        driver.get("https://www.livesport.com/kr/team/everton/KluSTr9s/")
        
    #리즈
    if a == "리즈":
        driver.get("https://www.livesport.com/kr/team/leeds/tUxUbLR2/")
        
    #번리
    if a == "번리":
        driver.get("https://www.livesport.com/kr/team/burnley/z3dmTMMO/")
        
    #왓포드
    if a == "왓포드":
        driver.get("https://www.livesport.com/kr/team/watford/UmMRoGzp/")
        
    #노르위치
    if a == "노르위치":
        driver.get("https://www.livesport.com/kr/team/norwich/Qo6off6p/")

    page = driver.page_source
    bs_obj = BeautifulSoup(page, "html.parser")

    win = bs_obj.find_all("div", {"class":"formIcon formIcon--w"}) #최근 10경기에서 승리
    tiewin = bs_obj.find_all("div", {"class":"formIcon formIcon--wo"}) #최근 10경기에서 정규 시간 외의 승리
    draw = bs_obj.find_all("div", {"class":"formIcon formIcon--d"}) #최근 10경기에서 비긴 경우
    lose = bs_obj.find_all("div", {"class":"formIcon formIcon--l"}) #최근 10경기에서 패한 경우
    tielose = bs_obj.find_all("div", {"class":"formIcon formIcon--lo"}) #최근 10경기에서 정규 시간 외의 승리패배
        
    n_win = len(win) + len(tiewin)
    n_draw = len(draw)
    n_lose = len(lose) + len(tielose)



    print(str(a)+"의 최근 10경기 중 승리를 "+str(n_win)+"번 했습니다.")
    print(str(a)+"의 최근 10경기 중 무승부를 "+str(n_draw)+"번 했습니다.")
    print(str(a)+"의 최근 10경기 중 패배를 "+str(n_lose)+"번 했습니다.")

    report1 = {'승리': n_win, '무승부': n_draw, '패배': n_lose}
    max_n = max(report1.values())
    for key in report1:
        if(report1[key]==max_n):
            print("위 결과에 따라 "+str(a)+"은/는 "+str(max_n)+"로 "+str(key)+"가 제일 많습니다.")

    report2 = {'승리': n_win, '무승부': n_draw, '패배': n_lose}
    min_n = min(report2.values())
    for key in report2:
        if(report2[key]==min_n):
            print("위 결과에 따라 "+str(a)+"은/는 "+str(min_n)+"로 "+str(key)+"가 제일 적습니다.")