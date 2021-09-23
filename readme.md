# 1. 메인 페이지 빌드
https://kyuhyuk.kr/article/python/2020/08/14/Django-Board-Write-Post 따라함

# 2. 로그인 빌드
https://wikidocs.net/71259 따라함

# 3. 실행방법
1. cd project/Board #프로젝트 경로이동
2. source /workspaces/AI_PersonalAIAdjutant_Posung/venv/bin/activate #가상환경 실행
3. python manage.py runserver #웹페이지 실행

# 4. Azure web service deploy
1. https://azure-demo-app.azurewebsites.net/ #웹사이트 링크
2. no module named 'django' azure 버그 - https://stackoverflow.com/questions/58449933/modulenotfounderror-no-module-named-django-when-trying-to-deploy-django-ser #requiremenets.txt 적용해서 해결
3. 템플릿 미적용 버그 - https://stackoverflow.com/questions/65431326/django-app-on-azure-not-getting-static-files #코드구조 변경

# 5. Schedule Calender
1. table 생성 (name: Schedule) 경로: board_app/models
2. input test data (name, date, time, todo)
3. create simple html template - table 연동

# 6. todo (working)
1. navbar 메뉴 추가: 예정사항, 실시사항 - 1. https://freehoon.tistory.com/125 2. https://getbootstrap.com/docs/4.3/examples/navbars/
2. https://ninetynine-2026.tistory.com/518 따라해보기
3. 스케줄 페이지 생성, model 내 table과 연동 필요