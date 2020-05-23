"# crmrevo-api" 

# Generate Access Token
curl -X POST 'http://crmrevo-api-testrepo.devops-app.apthai.com/api/v1/eqn/oauth/token' \
-H 'Content-Type: application/json' \
-d '{
	"applicationKey": "64125cbdf0ece98622d38c94a7ee7a8013",
	"applicationSecret": "c0714d778c3598de8d29fa09d7667db7"
}'

# Submit Transaction
curl -X POST 'http://crmrevo-api-testrepo.devops-app.apthai.com/api/v1/eqn/submit/1009' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODk1ODEwNDcsIm5iZiI6MTU4OTU4MTA0NywianRpIjoiN2IwNTc5MTQtMDIwNS00NjY1LWIxOTgtY2U3YzhiNjNjZGU2IiwiZXhwIjoxNTg5NTgxOTQ3LCJpZGVudGl0eSI6IjY0MTI1Y2JkZjBlY2U5ODYyMmQzOGM5NGE3ZWU3YTgwMTMiLCJmcmVzaCI6dHJ1ZSwidHlwZSI6ImFjY2VzcyJ9.BfKcj1g_6i6zsJRHqjHtYRN0e0sXgp6XcSIHSLNyaE4' \
-d '{
    "projectid": "10077",
    "project_name": "The Centro วัชรพล",
    "title_name": "mrs.",
    "first_name": "suchat_s",
    "last_name": "sujalarnlap",
    "email": "suchat_s@apthai.com",
    "mobile_no": "0830824173",
    "consent_flag": "Y",
    "channel_convenient": "E",
    "csseen_media": "ป้ายบิลบอร์ด",
    "csbudget": "2 ล้านบาท",
    "csincome": "300,000 บาทต่อเดือน",
    "family_income": "500,000 - 700,000 บาท",
    "proj_compare": "แสนสิริ",
    "products_interest": "",
    "cspersona": "เป็นคนละเอียด",
    "total_visit": "2 คน",
    "reason_visit": "สนใจหาซื้อบ้านใหม่",
    "decision_maker": "ภริยา",
    "probability": "medium",
    "contradiction": "ข้อโต้แย้ง",
    "buyornot": "สนใจซื้อหรือไม่",
    "other": "อื่นๆ",
    "comment": "ไม่ค่อยพูด",
    "total_answer": 7,
    "total_question": 10,
    "submit_dttm": "20200515201338",
    "createdby": "test1",
    "updatedby": "test2"
}'


git2docker.sh "modified fields" APCRMRevoAPI

