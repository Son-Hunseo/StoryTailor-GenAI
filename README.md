# StoryTailor_GenAI
- 문화체육관광부에서 주관하는 메타버스 AI콘텐츠 페스티벌 출품작으로 사용된 AI 백엔드 코드 
- 최종성적 3위: 우수상, 상금 2000만원
- 메인 백엔드(Spring)과 요청을 주고받으며, GenAI API를 호출하는 기능
## Contributor
- 손훈서 (https://github.com/Son-Hunseo)
  - 한양대학교 산업공학과
## Stacks & Versions
### v0.0.0 (대회 출품 당시)
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"> <img src="https://img.shields.io/badge/LangChain-00B265?style=for-the-badge&logo=&logoColor=white">
### v0.0.1 (FastAPI로 마이그레이션, Data Validation, 비동기 처리, LangChain 업데이트)
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"> <img src="https://img.shields.io/badge/LangChain-00B265?style=for-the-badge&logo=&logoColor=white">
## Dependencies
- LangChain
  - 0.1.5
- FastAPI
  - 0.95.1
 ## Architecture
<img width="1000" alt="image" src="https://github.com/StoryTailor-KR/StoryTailor-GenAI/assets/66631831/a7650bd6-142b-4e9f-89d2-24f391e4b1bc">

## API 명세
| 기능 | METHOD | URL | request | response | 비고 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| AI 챗봇 | POST | /tailor/chat | {<br><br>"msgNum": "0",<br><br>"msgType": "human",<br><br>"sessionId": "0",<br><br>"history": {"userChat": ["start","공룡을 그렸구, 공룡이 뛰어다니는 생각을 했어!","초록색이야!","화산이 폭발하는 풍경이구 숲도 있어!"],"aiChat": ["오, 너의 그림에 대해 좀 더 알려줄래? 이 그림을 그릴 때 무슨 생각을 했는지 궁금해!","그럼 공룡이 뛰어다니는 그림이구나! 공룡이 어떤 색깔이야?","와, 초록색 공룡이라니! 그럼 공룡이 있는 곳은 어떤 모습인가요? 어떤 풍경일까요?","우와, 화산이 폭발하는 풍경이라니! 그럼, 공룡은 화산 폭발을 어떻게 대처하고 있어?"]},<br><br>"text": "화산으로부터 도망가고있어!"<br><br>} | {"msgNum":1,"sessionId":0,"msgType":"AI","text":"정말 흥미로운 그림이야! 다음에도 멋진 그림을 그려주렴!","status":"true","keyword":["공룡","뛰어다니는","초록색","화산 폭발","숲"],"recoKeyword":["위험","도전","도망","모험","용기"]} |  |
| 이야기 생성 및 이미지 프롬프트 생성 | POST | /tailor/makeStory | {<br><br>"keyword": [<br><br>"공룡",<br><br>"초록색",<br><br>"화산 폭발",<br><br>"숲",<br><br>"모험",<br><br>"위험",<br><br>"도전",<br><br>"용기"<br><br>]<br><br>} | {<br>    "story": [<br>        "공룡 데니의 초록 숲 모험",<br>        "옛날 옛적, 초록색 공룡 데니가 살고 있었어요. 데니는 숲 속에서 친구들과 즐겁게 놀았지요.",<br>        "어느 날, 멀리서 '펑!' 소리가 들렸어요. 화산이 폭발한 거예요! 데니와 친구들은 숲을 지키기로 결심했어요.",<br>        "공룡 데니는 위험을 무릅쓰고 화산 가까이 가서 돌멩이를 모아 왔어요. 그 돌멩이들로 화산의 흐르는 불을 막았지요.",<br>        "데니는 친구들과 함께 숲을 구했어요. 모두가 데니의 용기와 도전을 칭찬했답니다. 그리고 데니는 숲의 영웅이 되었어요."<br>    ],<br>    "imgPrompt": [<br>        "A green dinosaur playing joyfully with its friends in a forest. cartoon style. color pencil sketch.",<br>        "The sound of a distant 'boom!' echoes as a volcano erupts, with the dinosaur and its friends determined to protect their forest home. cartoon style. color pencil sketch.",<br>        "The brave dinosaur collecting stones near the erupting volcano to block the flowing lava. cartoon style. color pencil sketch.",<br>        "The dinosaur, celebrated by its friends for saving the forest, becomes the hero of the woods. cartoon style. color pencil sketch."<br>    ]<br>} |  |
| 번역 | POST | /tailor/translate | {<br><br>"story": ["어떤 원시인과 공룡이 살았어요.", "그 원시인과 공룡은 친구였답니다.", "공룡과 원시인은 힘을합쳐 마을을 구했어요"],<br><br>"lang": "zh"<br><br>} | {<br>    "story": [<br>        "有些原始人和恐龙曾经活过。",<br>        "那个原始人和恐龙是朋友。",<br>        "恐龙和原始人合力拯救了村庄。"<br>    ],<br>    "lang": "zh"<br>} |  |
| 퀴즈 생성 | POST | /tailor/quiz | {<br><br>"sentence": "어떤 원시인과 공룡이 살았어요."<br><br>} | {<br>    "sentence": "어떤 원시인과 공룡이 () 살았어요.",<br>    "options": [<br>        "함께",<br>        "따로",<br>        "조용히"<br>    ],<br>    "answer": "함께"<br>} | 현재 사용 X |
