# 자바스크립트, DOM

---

---

---

# JavaSctript Intro

## 브라우저(browser)

- URL로 웹(WWW)을 탐색하고 서버와 통신하고, HTML 문서나 파일을 출력하는 GUI 기반의 소프트웨어
- 인터넷의 컨텐츠를 검색 및 열람하도록 함
- "웹 브라우저" 라고도 함
- 주요 브라우저
  - 구글 크롬, 모질라 파이어폭스, 마소 엣지, 오페라, 사파리 등등



## JavaScript의 필요성

- 브라우저 화면을 **'동적'**으로 만들기 위함
- 브라우저를 조작할 수 있는 유일한 언어



## Most Popular Programming Language in 2021 survey

- stackoverflow 에서 1위
- jetbrain 에서도 1위



# History of JavaScript

## JavaScript의 탄생

- 1994년 당시 '넷스케이프 커뮤니케이션스' 사 의 Netscape Navigator(NN) 브라우저가 전 세계 점유율을 80% 이상 독점하며 브라우저의 표준 역할을 함
- 당시 넷스케이프에 재직 중이던 브랜던 아이크가 HTML를 동적으로 동작하게 하기 위한 회사 내부 프로젝트를 진행하던 중 JS를 개발
- JavaScript 이름 변천사
  - Mocha -> LiveScript -> JavaScript (1995)

- 그러나 1995년 경쟁사 마이트로소프트에서 이를 채택하여 커스터마이징한 JScript를 만듦
- 이를 IE 1.0에 탑재 -> 1차 브라우저 전쟁의 시작



## 제 1차 브라우저 전쟁

- 넷스케이프 vs 마이크로소프트 (이하 마소)
- 빌 게이츠 주도하에 마소는 1997년 IE 4 를 발표하면서 시장을 장악하기 시작
  - 당시 윈도우 OS의 시장 점유율은 90%
  - 글로벌 기업 마소의 공격적인 마케팅
- 마소의 승리로 끝나며 2001년부터 IE의 점유율은 90%를 상회
- 1998년 넷스케이프에서 나온 브랜던 아이크 외 후계자들은 모질라 재단을 설립
  - 파이어폭스를 통해 IE에 대항하며 꾸준히 점유율을 올려 나감



## 제 2차 브라우저 전쟁

- MS vs GOOGLE

- 2008년 Google의 Chrome(크롬) 브라우저 발표

- 2011년 3년 만에 파이어폭스의 점유율을 돌파 후 2012년부터 전 세계 점유율 1위 등록

- 크롬의 승리 요인

  - 압도적 속도

  - 강력한 개발자 도구

  - 웹 표준



## 파편화와 표준화

- 제 1차 브라우저 전쟁 이후 수많은 브라우저에서 자체 자바스크립트 언어를 사용하게 됨
- 결국 서로 다른 자바스크립트가 만들어지면서 크로스 브라우징 이슈가 발생하여 웹 표준의 필요성이 제기
- 크로스 브라우징(Cross Browsing)
  - W3C에서 채택된 표준 웹 기술을 채용하여 각각의 브라우저마다 다르게 구현되는 기술을 비슷하게 만들되, 어느 한쪽에 치우치지 않도록 웹 페이지를 제작하는 방법론 (동일성이 아닌 동등성)
  - 브라우저마다 렌더링에 사용하는 엔진이 다르기 때문
- 1996년 부터 넷스케이프는 표준 제정의 필요성을 주장
  - ECMA 인터네셔널(정보와 통신 시스템을 위한 국제적 표준화 기구)에 표준 제정 요청

- 1997년 ECMAScript 1 (ES1) 탄생
- 제 1차 브라우저 전쟁 이후 제기된 언어의 파편화를 해결하기 위해 각 브라우저 회사와 재단은 표준화에 더욱 적극적으로 힘을 모으기 시작



## JavaScript ES6+

- 2015년 ES2015 (ES6) 탄생
  - 'Next-gen of JS'
  - JavaScript의 고질적인 문제들을 해결
  - JavaScript의 다음 시대라고 불릴 정도로 많은 혁신과 변화를 맞이한 버전
  - 이때부터 버전 순서가 아닌 출시 연도를 붙이는 것이 공식 명칭으로 사용되어졌으나, 통상적으로 ES6라 부름
  - 현재는 표준 대부분이 ES6+로 넘어옴



## Vanilla JavaScript

- 크로스 브라우징, 간편한 활용 등을 위해 많은 라이브러리 등장 (jQuery 등)
- ES6 이후, 다양한 도구의 등장으로 순수 자바스크립트 활용의 증대



---
---
---
# DOM
---
---
---

# DOM(Document Object Model)

## 브라우저에서 할 수 있는 일

- DOM 조작
  - 문서(HTML) 조작
- BOM 조작
  - navigator, screen, location, frames, history, XHR
- JavaScript Core (ECMAScript)
  - Data Structure(Object, Array), Conditional Expression, Iteration



## DOM 이란?

- HTML, XML 과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스
- 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델
- 문서가 구조화되어 있으며 각 요소는 객체(object)로 취급
- 단순한 속성 접근, 메서드 활용뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
- 주요 객체
  - window : DOM을 표현하는 창, 가장 최상위 객체 (작성 시 생략 가능)
  - document : 페이지 컨텐츠의 Entry Point 역할을 하며, \<body> 등과 같은 수많은 다른 요소들을 포함
  - navigator, location, history, screen 



## DOM - 해석

- 파싱 (Parsing)
  - 구문 분석, 해석
  - 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정



## BOM 이란?

- Browser Object Model
- 자바스크립트가 브라우저와 소통하기 위한 모델
- 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단
  - 버튼, URL 입력창, 타이틀 바 등 브라우저 윈도우 및 웹 페이지 일부분을 제어 가능
- window 객체는 모든 브라우저로부터 지원 받으며 브라우저의 창(window)를 지칭



## BOM 조작



## JavaScript Core



---

---

---

# DOM 조작

---

---

---

# DOM조작

## DOM조작 - 개념

- Document는 문서 한 장(HTML)에 해당하고 이를 조작
- DOM 조작 순서
  1. 선택(Select)
  2. 변경(Manipulation)



## DOM 조작 - Document 위치



## DOM 객체의 상속 구조

- EventTarget
  - Event Listener 를 가질 수 있는 객체가 구현하는 DOM 인터페이스

- Node
  - 여러 가지 DOM 타입들이 상속하는 인터페이스

- Element
  -  Document 안의 모든 객체가 상속하는 가장 범용적인 인터페이스
  - 부모인 Node와 그 부모인 EventTarget 의 속성을 상속
- Document
  - 브라우저가 불러온 웹 페이지를 나타냄
  - DOM 트리의 진입점(entry point) 역할을 수행

- HTMLElement
  - 모든 종류의 HTML 요소
  - 부모 element 의 속성 상속