# Ojbect Oriented Programming(OOP)
- 데이터(data)를 추상화시켜 상태(속성)와 행위(methods)를 가진 객체(object)로 만들고 그 객체들 간의 유기적인 상호작용을 통해 로직(흐름)을 구성하는 프로그래밍 방법
- 프로그램을 실제 세상에 가깝게 모델링하는 기법

# class
- 어떤 문제를 해결하기 위한 데이터를 만들기 위해 OOP 원칙에 따라 집단(현실 세계)에 속하는 속성과 행위(methods)를 변수와 메서드로 정의한 것
- 특별한 데이터와 메서드의 집합
- 설계도라고 할 수 있다.

# instance (object)
- class 에서 정의한 것(설계도)을 토대로 실제 메모리상에 할당된 것(실제 사물, object)으로 실제 프로그램에서 사용되는 데이터이다.
- 하나의 class로 만들어진 여러 instance(object)는 각각 독립적이다.
- "실제 로봇"
- 객체가 소프트웨어에 실체화될 때 즉, 메모리에 할당되어 사용될 때 해당 객체를 인스턴스라고 한다.
- 객체는 인스턴스의 상위 개념이지만, 일반적으로 인스턴스와 같은 의미로 사용
- 하나의 클래스로 만들어진 여러 인스턴스들은 각각 독립적이다.

# OOP 원칙
- 캡슐화: encapsulation
    - 객체(object)의 **속성과 행위(methods)**를 하나로 묶고, 구현된 일부를 외부에 감추어 은닉한다.
- 추상화: abstraction
    - 불필요한 정보는 숨기고 중요한(필요한) 정보만을 표현함으로써 공통의 속성이나 행위(methods)를 하나로 묶어 이름을 붙이는 것.
- 상속: Inheritance
    - 부모 class의 속성과 행위(methods)을 그대로 상속 받고 행위(methods)의 일부분을 수정해야 할 경우 상속받은 자식 class에서 해당 행위(methods)만 다시 수정하여 사용할 수 있도록 한다. 또한 자식 class에서 추가적으로 속성이나 행위(methods)를 정의할 수 있게 한다.

- 다형성: Polymorphism
    - 여러 형태를 가질 수 있도록 한다. 즉, 객체를 부품화할 수 있도록 한다.
    