# 숫자 야구

## 환경

* Mac OS Mojave
* Python - version 3.7.3
* IDE - Pycharm 2019.02 Professional

## 기능

1. 1~9 까지 서로 다른 수로 이루어진 3개의 숫자를 맞추는 게임이다.

2. 규칙은 다음과 같다.
* 스트라이크 - 숫자의 자리와 숫자를 맞춘 경우
* 볼 - 숫자를 맞춘 경우 (자리는 맞추지 않은 경우)
* 아웃 - 스트라이크와 볼이 하나도 없는 경우

3. 문제는 컴퓨터가 제출하고 사용자는 맞추는 역할이다.
* 컴퓨터는 1부터 9까지 임의의 서로 다른 수 3개를 선택한다.
* 플레이어는 3개의 숫자를 입력하여 컴퓨터가 만든 서로 다른 3개의 수를 맞춘다.
* 3 스트라이크의 경우 게임이 종료된다.

## 프로그램 실행시 (콘솔)
```
숫자 야구 게임을 시작합니다.
숫자를 입력해주세요 : 123
3 아웃
숫자를 입력해주세요 : 456
1 스트라이크 2 볼
숫자를 입력해주세요 : 465
3 스트라이크
축하합니다. 승리하였습니다.
```

## MVC 패턴

1. [위키피디아](https://ko.wikipedia.org/wiki/%EB%AA%A8%EB%8D%B8-%EB%B7%B0-%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC)
2. [생활코딩](https://opentutorials.org/course/697/3828)

## 객체 지향

1. [위키피디아](https://ko.wikipedia.org/wiki/%EA%B0%9D%EC%B2%B4_%EC%A7%80%ED%96%A5_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)
2. [생활코딩](https://opentutorials.org/course/743/6553)

## 보완해야 할 부분

1. 숫자 입력

- 적게 치면 ~~프로그램이 죽는다.~~
- 숫자가 아닌 문자를 입력했을 때 ~~프로그램이 죽는다.~~

- 똑같은 수를 입력해도 실행이 된다. ~~=> 프로그램이 죽는다.~~
- 3개 보다 많이 입력해도 실행이 된다. ~~=> 프로그램이 죽는다.~~
