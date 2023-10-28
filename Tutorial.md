## Rozwiązywnaie konfltów w życiu nie jest proste, jednak w przypadku towrzenia oprogramowania jest wręcz przeciwnie ! 

W poniższym artykule odwzorujemy bardzo częsty przypadek konfliktu występującego w pracy zespołu nad jednym repozytorium w github. Nie będę zaczynał tego poradnika od wykładu czym jest konflik, komenda git rebase czy git merge. Nie sądze że to jest najlpsze podejście aby każdy tutorial zaczynać od tego samego, tym bardziej zostało to już wiele razy świetnie opisane prze innych autorów co możecznie znaleźć min tutaj (link). Ewentualnie wyjaśniania będą umieszczał przy krokach w których roziwązujemy problem.

Masz już kubek ulubionej kawy ? 
Nie ? 
To przygotuj, ją i zaczymany 

## Przedstawienie repozytorium

Naszym ćwiczebnym przykładem będzie a jakże orginalnie... kalkulator. Załużmy że mamy w zespole trzy osoby Dave'a, Anne i Bogdana (dzisiaj będziemy Bogdanem ). Dave jest naszym przełożonym i na planowaniu sprinu w poniedziałek wyznacza nam zadanie naprawienia buga dzielenia przez zero w funkcji `divide()` oraz pierwiastkowania licz ujemnych w funkcji `square_root()`. Zadaniem Anny natomiast jest refaktoryzacja kodu, dodanie brakujących docstringów itp. 

```python
# calculator.py przed rozpoczęciem pracy przez Anne i Bogdana
import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def power(a, b):
    return a**b


def square_root(a):
    return math.sqrt(a)
```

Niestety w poniedziałek wieczorem zaczeliśmy czuć objawy prziębienia i we wtorek nie moglismy przyjść do pracy. Wracamy w środe pełni sił i zabieramy się za powieżone nam zadanie. W między czasie Anna wykonała swoje zadanie, utworzyła Pull Request i po code review Pull request został zmergowany do brancha `main`.

```python
# calculator.py na branchu main po wprowadzeniu zmian przez Anne

def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide the first number by the second. Returns an error message if the second number is zero."""
    return a / b


def power(a: float, b: float) -> float:
    """Raise the first number to the power of the second."""
    return a**b


def square_root(a: float) -> float:
    """Calculate the square root of a number."""
    return a**0.5
```

Jak widać Anna wykonała powieżone jej zadanie i na pierwszy rzut oka można nie zauważyć potęcjalnego konfliktu. Bogdan bieże się za prace i poprawia wskazene funkcje.
