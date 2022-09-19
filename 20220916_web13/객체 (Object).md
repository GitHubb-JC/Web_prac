# ECMA Script -----

---

---

---

# Introduction

## 코딩 스타일 가이드

- 코딩 스타일의 핵심은 합의된 원칙과 일관성
  - 절대적인 하나의 정답은 없으며, 상황에 맞게 원칙을 정하고 일관성 있게 사용하는 것이 중요
- 코딩 스타일은 코드의 품질에 직결되는 중요한 요소
  - 코드의 가독성, 유지보수 또는 팀원과의 커뮤니케이션 등 개발 과정 전체에 영향을 끼침
- (참고) 다양한 자바스크립트 코딩 스타일 가이드
  - Airbnb Javascript Style Guide
  - Google Javascript Style Guide
  - standardjs



# 변수와 식별자

- 식별자 (identifier) 는 변수를 구분할 수 있는 변수명을 말함

- 식별자는 반드시 문자, 달러($) 또는 밑줄(_)로 시작

- 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작

- 예약어* 사용 불가능

  - ex) for, if ,function

- (참고) 선언, 할당, 초기화

  <img src="객체 (Object).assets/선언_할당_초기화.jpg" alt="선언_할당_초기화" style="max-height:80%; max-width:60%;" align="left" />

  - 선언(Declaration)
    - 변수를 생성하는 행위 또는 시점
  - 할당(Assignment)
    - 선언된 변수에 값을 저장하는 행위 또는 시점
  - 초기화(initialization)
    - 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점



## let, const

- 재할당 : let(O), const(X)

<img src="객체 (Object).assets/let_재할당.jpg" alt="let_재할당" style="zoom: 71%;" align="left" />

<img src="객체 (Object).assets/const_재할당.jpg" alt="const_재할당" style="zoom:72%;" align="left"/>

- 재선언 : let(X), const(X)

<img src="객체 (Object).assets/let_재선언.png" alt="let_재선언" style="zoom: 71%;" align="left" />

<img src="객체 (Object).assets/const_재선언.jpg" alt="const_재선언" style="zoom:71%;" align="left"/>

- 블록 스코프* (block scope)

  <img src="객체 (Object).assets/블록 스코프-166330857673621.jpg" alt="블록 스코프" style="zoom:71%;" align="left"/>

  - if, for, 함수 등의 중괄호 내부를 가리킴
  - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능



## var

- var 로 선언한 변수는 재선언 및 재할당 모두 가능

- ES6 이전에 변수를 선언할 때 사용되던 키워드

- 호이스팅* 되는 특성으로 인해 예기치 못한 문제 발생 가능

  - 호이스팅(hoisting) : 함수 안에 있는 선언들을 모두 끌어올려서 해당 함수 유효 범위의 최상단에 선어하는 것을 말한다.
    - 변수를 선언 이전에 참조할 수 있는 현상
    - 변수 선언 이전의 위치에서 접근시 undefined를 반환
    - 자바스크립트는 모든 선언을 호이스팅한다.
    - 즉 var, let, const 모두 호이스팅이 발생하지만, var는 선언과 초기화가 동시에 발생하여 일시적 사각지대가 존재하지 않는다.

- 재선언, 재할당 모두 가능

  <img src="객체 (Object).assets/var_재선언재할당.jpg" alt="var_재선언재할당" style="zoom:71%;" align="left"/>

- 함수 스코프* (function scope)

  <img src="객체 (Object).assets/함수 스코프.jpg" alt="함수 스코프" style="zoom:72%;" align='left'/>

  - 함수의 중괄호 내부를 가리킴
  - 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능



## let, const, var 비교

![let_const_var](객체 (Object).assets/let_const_var.jpg)



# 데이터 타입

- 자바스크립트의 모든 값은 특정한 데이터 타입을 가짐

- 크게 원시 타입* (Primitive type)과 참조 타입* (Reference type)으로 분류됨

  <img src="객체 (Object).assets/원시타입_참조타입.jpg" alt="원시타입_참조타입" style="zoom:71%;" align='left'/>



## 원시 타입 (Primaitive type)

<img src="객체 (Object).assets/원시타입.jpg" alt="원시타입" style="zoom:72%;" align='left'/>

- 객체(Object)가 아닌 기본 타입
- 변수에 해당 타입의 **'값'**이 담김
- 다른 변수에 복사할 때 **'실제 값'**이 복사됨



## 참조 타입(Reference type)

<img src="객체 (Object).assets/참조타입.jpg" alt="참조타입" style="zoom:72%;" align='left'/>

- 객체(Object) 타입의 자료형
- 변수에 해당 객체의 **'참조 값'**이 담김
- 다른 변수에 복사할 때 **'참조 값'**이 복사됨



## 숫자(Number) 타입

<img src="객체 (Object).assets/숫자타입.jpg" alt="숫자타입" style="zoom:80%;" align='left'/>

- 정수, 실수 구분 없는 하나의 숫자 타입
- 부동소수점 형식을 따름
- (참고) NaN(Not-a-Number)
  - 계산 불가능한 경우 반환되는 값
    - ex) 'Angel' / 1004 => NaN



## 문자열(String) 타입

<img src="객체 (Object).assets/문자열타입.jpg" alt="문자열타입" style="zoom:80%;" align='left'/>

- 텍스트 데이터를 나타내는 타입
- 16비트 유니코드 문자의 집합
- 작은, 큰 따옴표 모두 가능
- 템플릿 리터럴(Template Literal)
  - ES6  부터 지원
  - 따옴표 대신 backtick(\` `)으로 표현
  - ${ expression } 형태로 표현식 삽입 가능



## undefined

<img src="객체 (Object).assets/image-20220916164852061.png" alt="image-20220916164852061" style="zoom:80%;" align='left'/>

- 변수의 값이 없음을 나타내는 데이터 타입
- 변수 선언 이후 직접 값을 할당하지 않으면, 자동으로 undefined가 할당됨



## null

<img src="객체 (Object).assets/image-20220916165250351.png" alt="image-20220916165250351" style="zoom:80%;" align='left'/>

- 변수의 값이 없음을 의도적으로 표현할 때 사용하는 데이터 타입
- (참고) null 타입과 typeof 연산자*
  - typeof 연산자* : 자료형 평가를 위한 연산자
  - null 타입은 ECMA 명세의 원시 타입의 정의에 따라 원시 타입에 속하지만, typeof 연산자의 결과는 객체(object)로 표현됨



## Boolean 타입

<img src="객체 (Object).assets/image-20220916165650229.png" alt="image-20220916165650229" style="zoom:80%;" align='left'/>

- 논리적 참 또는 거짓을 나타내는 타입

- true 또는 false로 표현

- 조건문 또는 반복문* 에서 유용하게 사용

  - (참고) 조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 ToBoolean Conversions(자동 형변환) 규칙에 따라 true 또는 false로 변환됨

    <img src="객체 (Object).assets/image-20220916165946981.png" alt="image-20220916165946981" style="zoom:80%;" align='left'/>



# 연산자

## 할당 연산자

<img src="객체 (Object).assets/image-20220916170201949.png" alt="image-20220916170201949" style="zoom:71%;" align='left'/>

- 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
- 다양한 연산에 대한 단축 연산자 지원
- (참고) Increment 및 Decrement 연산자*
  - Increment(++) : 피연산자의 값을 1 증가시키는 연산자
  - Decrement(--) : 피연산자의 값을 1 감소시키는 연산자
  - Airbnb Style Guide 에서는 '+=' 또는 ' -=' 와 같이 더 분명한 표현으로 적을 것을 권장



## 비교 연산자

<img src="객체 (Object).assets/image-20220916172857595.png" alt="image-20220916172857595" style="zoom:80%;" align='left'/>

- 피연산자를 비교하고 결과값을 boolean으로 반환하는 연산자
- 문자열은 유니코드 값을 사용하며 표준 사전 순서를 기반으로 비교
  - ex) 알파벳끼리 비교할 경우
    - 알파벳 순서상 후순위가 더 크다
    - 소문자가 대문자보다 더 크다









# 객체 (Object) -----

---

---

---

# 객체 (Object)

## 객체 정의와 특징

'메서드로 arrow function 사용 노높'