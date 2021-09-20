# 1. 메인 페이지 빌드
https://kyuhyuk.kr/article/python/2020/08/15/Django-Board-Post-View 따라함

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

