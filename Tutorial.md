## Rozwiązywnaie konfltów w życiu nie jest proste, jednak w przypadku towrzenia oprogramowania jest wręcz przeciwnie ! 

W poniższym artykule odwzorujemy bardzo częsty przypadek konfliktu występującego w pracy zespołu nad jednym repozytorium w github. Nie będę zaczynał tego poradnika od wykładu czym jest konflik, komenda git rebase czy git merge. Nie sądze że to jest najlpsze podejście aby każdy tutorial zaczynać od tego samego, tym bardziej zostało to już wiele razy świetnie opisane prze innych autorów co możecznie znaleźć min tutaj (link). Ewentualnie wyjaśniania będą umieszczał przy krokach w których roziwązujemy problem.

Masz już kubek ulubionej kawy ? 
Nie ? 
To przygotuj, ją i zaczymany 

## Przedstawienie przypadku 

Naszym ćwiczebnym przykładem będzie a jakże orginalnie... kalkulator. Załużmy że mamy w zespole trzy osoby Bob'a, Anne i Bogdana (dzisiaj będziemy Bogdanem ). Bob jest naszym przełożonym i na planowaniu sprinu w poniedziałek wyznacza nam zadanie naprawienia buga dzielenia przez zero w funkcji `divide()` oraz pierwiastkowania licz ujemnych w funkcji `square_root()`. Zadaniem Anny natomiast jest refaktoryzacja kodu, dodanie brakujących docstringów itp. 

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

## Konflikt

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

Jak widać Anna wykonała powieżone jej zadanie i na pierwszy rzut oka można nie zauważyć potęcjalnego konfliktu. Bogdan bieże się za prace i poprawia wskazene funkcje. Poprawiliśmy kod, commitujemy nasze zmiany, pushujemy je do github'a i tworzymy Pull Request. Jednak naszym oczą ukazjuje się poniższy komunikat.

zdjęcie PR

```python
# calculator.py na branchu bogdan_calculator_bug_fix po wprowadzeniu zmian przez Bogdana
import math

def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """
    Divide two numbers a by b.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    result = a / b
    return result


def power(a: float, b: float) -> float:
    """Raise the first number to the power of the second."""
    return a**b


def square_root(a: float) -> float:
    """
    Return the square root of a non-negative number,
    or an error message for negative input.
    """
    if a < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(a)
```

Mamy konflikt z branchem `main`. Jest on spowodoany tym że zarówno w gałęzi `main` jak i w gałęzi `bogdan_calculator_bug_fix`, zmiany dotyczą tego samego fragmentu kodu i nasz branch nie zawiera commit'a Anny (Dokładniej zostanie to opisane w sekcji "Co kryje się pod komendą git rebase"). Git nie jest w stanie automatycznie połączyć tych zmian, ponieważ nie wie, które zmiany zachować, gdyż się wzajemnie wykluczają. Konieczne jest rozwiązanie konfliktu, aby zdecydować, które zmiany zostaną zachowane.

Więc, bierzemy się do pracy.


Skorzystamy z komendy git rebase ponieważ moim zdaniem bardziej pasuje do tej sytuacji. Jak mówi nam definicja `git rebase` jest zalecane, gdy chcesz utrzymać czystą i liniową historię zmian. Zamiast tworzyć nowy commit łączący, git rebase "przenosi" Twoje zmiany na szczyt gałęzi źródłowej, co sprawia, że historia jest bardziej spójna i klarowna. Jest to przydatne w przypadku prywatnych gałęzi, gdzie nie jest tak ważne śledzenie dokładnych źródeł zmian, ale chcesz utrzymać historię w przejrzysty sposób.

# Rozwiązywanie konfliktu

Przechodzimy do terminala gdzie znajduje sie nasze loklane repozytroium na branch `main` i aktualizujemy go.

```bash
git switch main && git pull origin main
```

Następnie przechodzimy na nasz branch 

```bash
git switch bogdan_calculator_bug_fix

```
I wykonujemy poniższą komennde.

```bash
git rebase main
```
Rezultat komendy:
```bash
Auto-merging src/calculator/calculator.py
CONFLICT (content): Merge conflict in src/calculator/calculator.py
error: could not apply 5c58f0b... 🐛 Fixed bugs in `calculator.py`
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply 5c58f0b... 🐛 Fixed bugs in `calculator.py`
```
Upss dalej mamy problem. Pomimo tego iż zastosowaliśmy git rebase, git dalej chce od nas jakiegoś złączenia konfliktów. O co chodzi przecież rebase miał rozwiązać problemu ? Cóż nie zawsze sie to uda, ponieważ w tym przypadku mamy zmiany dokładnie w tym samym miejscu co Anna. Zobaczymy to po otworzeniu pliku `src/calculator/calculator.py` w dowolnym edytorze tekstowym. Możecie użyć w zasadzie każdego np. vscode, vim'a (tylko musisz wiedzieć jak z niego później wyjść ;p), itp. Zawrtość pliku będzie wyglądać tak:

```python
# calculator.py po wykonaniu komendy git rebase
# Jak widać mamy pokazane różnice między branchami i musimy którąś wybrać lub je zmieszać

def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


<<<<<<< bogdan_calculator_bug_fix
def divide(a, b):
    """
    Divide two numbers a by b.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    result = a / b
    return result
=======
def divide(a: float, b: float) -> float:
    """Divide the first number by the second. Returns an error message if the second number is zero."""
    return a / b
>>>>>>> main


def power(a: float, b: float) -> float:
    """Raise the first number to the power of the second."""
    return a**b


def square_root(a: float) -> float:
<<<<<<< bogdan_calculator_bug_fix
    """
    Return the square root of a non-negative number,
    or an error message for negative input.
    """
    if a < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(a)
=======
    """Calculate the square root of a number."""
    return a**0.5
>>>>>>> main

```

Przed rozwiązaniem konfliktu ważne jest to aby sie skonsultować z autorem commitu w którym mamy problem. Może czegoś nie wiemy, może autor miał jakiś powód dlaczego dokonał zmiany w ten sposób, warto zawsze porozmawiać. Załóżmy że porozmawialiśmy z Anną i doszliśmy do wniosku że zachowany naszą część kodu lecz pozostawimy sposób obliczania pierwiastka wymyślony przez Anne. 

Otwieramy w dowolnym edytorze tekstowym plik `src/calculator/calculator.py` i dokonujemy w nim zmian.

```python
# calculator.py Po konsultacji z Anna 

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
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b


def power(a: float, b: float) -> float:
    """Raise the first number to the power of the second."""
    return a**b


def square_root(a: float) -> float:
    """
    Return the square root of a non-negative number,
    or an error message for negative input.
    """
    if a < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return a**0.5
```

Uruchamiamiy komende `git status` aby sprawdzić nasze zmiany.

```bash
interactive rebase in progress; onto 7e57dbb
Last command done (1 command done):
   pick 5c58f0b 🐛 Fixed bugs in `calculator.py`
No commands remaining.
You are currently rebasing branch 'bogdan_calculator_bug_fix' on '7e57dbb'.
  (fix conflicts and then run "git rebase --continue")
  (use "git rebase --skip" to skip this patch)
  (use "git rebase --abort" to check out the original branch)

Unmerged paths:
  (use "git restore --staged <file>..." to unstage)
  (use "git add <file>..." to mark resolution)
        both modified:   src/calculator/calculator.py

no changes added to commit (use "git add" and/or "git commit -a")
```

Jak widać w kategorii `Unmerged paths:` znajduje się nasz plik `calculator.py` więc dodajemy go do stagingu komendą `git add src/calculator/calculator.py` i uruchamiamy komende `git rebase --continue`. Wyskoczy nam okno podczas wykonywania komendy aby dodać dodaktową wiadomość ale możemy ja pominąć naciskająć `ctr+x`.

tsa dam mamy poprawnie wykonany rebase !
```bash
[detached HEAD 705c6b4] 🐛 Fixed bugs in `calculator.py`
 1 file changed, 10 insertions(+), 2 deletions(-)
Successfully rebased and updated refs/heads/bogdan_calculator_bug_fix.
```
No to co ? Pozsotąło nam zrboić `git push` i możmey iśc do domu ?
Nooo niestety nie :D

Spróbujmy wkonać komnde `git push` z branch'a `bogdan_calculator_bug_fix`
```bash
To https://github.com/bogdan/rebase_tutorial.git
 ! [rejected]        bogdan_calculator_bug_fix -> bogdan_calculator_bug_fix (non-fast-forward)
error: failed to push some refs to 'https://github.com/bogdan/rebase_tutorial.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```
Pojawia sie typowy problem po wykonaniu `git rebase`. Ponieważ histora zmian na lokalnym branchu `bogdan_calculator_bug_fix` różni się od histori zmian na branchu `bogdan_calculator_bug_fix` w githubie. To co ? Znowu musimy rozwiązywać konflikt ? Drugi raz ? 

Na szczęście nie, mamy do wyboru dwa poniższe najpopularniejsze rozwiązania. 

1. Użycie komendy `git push --force`: Po jej użyciu historia gałęzi na zdalnym repozytorium zostaje całkowicie zastąpiona historią z lokalnej gałęzi. Jest to operacja potencjalnie niebezpieczna, ponieważ może prowadzić do utraty danych na zdalnym repozytorium i wprowadzenia dezorganizacji, szczególnie w przypadku współpracy z innymi osobami. Dlatego `git push --force` powinno się stosować ostrożnie i tylko wtedy, gdy jesteś pewny, że nikt inny nie pracuje na zdalnej gałęzi, lub po wcześniejszym poinformowaniu współpracowników. W naszym przypadku nikt inny poza Bogdanem nie pracuje na tej gałęzi oraz nie jest to główna gałąź więc możemy to zrobić.


2. Tworzenie Nowej Gałęzi i Merge: Zamiast nadpisywać historię gałęzi, możesz utworzyć nową gałąź na podstawie gałęzi po rebase. Następnie przeprowadź pull request tej nowej gałęzi do oryginalnej gałęzi. To zachowa historię i pozwoli innym na dostęp do poprzednich zmian. Na przykład:
```bash
git checkout bogdan_calculator_bug_fix
git checkout -b bogdan_calculator_bug_fix_after_rebase
git push --set-upstream origin bogdan_calculator_bug_fix_after_rebase
```

## zdjęcie PR po push -force

## zdjęcie PR po nowym branchu 

I vula la ! To by było na tyle jeśli chodzi o praktyczne rozwiązanie problemu. Jeśli nie skończyłeś jeszcze swoej kawy lub jeszcze jesteś głodny wiedzy zachęcam Cię do przeczytania ostatniej sekcji odnośnie działania komendy rebase. Uważam że dobrze jest wiedzieć co tak na prawde robią "pod spodem" komendy które wykonujem, ponieważ brak tej wiedzy w niektórych przypadkach może zaszkodzić naszemu repozytorium.  


# Co kryje się pod komendą rebase

Cofnijmy sie w czase do momentu konfliktu brancha Bogdan'a z branchem `main` na który została wysłana zmianna Anny. Poniżej mamy ukazaną historie commitów na branchu `main` którą możemy wyświetlić tą komendą.

```bash
git log --graph --date=short
```
wynik:
```bash
*   commit 7e57dbb616c729219cbb49beaba30d06c3346357 (HEAD -> main, origin/main, origin/HEAD)
|\  Merge: 6398b0a ee86445
| | Author: Anna
| | Date:   2023-10-28
| | 
| |     Merge pull request #8 from Anna/anna_code_refactoring
| |     
| |     ♻️ Refactored `calculator.py`
| | 
| * commit ee8644574aeb7163ca2389d5d438e55ebf0ab638 (origin/anna_code_refactoring)
|/  Author: Anna
|   Date:   2023-10-28
|   
|       ♻️ Refactored `calculator.py`
| 
* commit 6398b0aa3b7042ff5a26300cdbaa4d82b37c48df
| Author: Admin Bob
| Date:   2023-10-25
| 
|     ✨ Added `square_root()` function
| 
* commit 4abc1d16b85890cfb3d7c0a208f8f5143f6f2220
```
Czytając od dołu historia wygląda tak:
1. Dawna zminan wprowadzona przez Bob'a ✨ Added `square_root()` function
2. Dodanie commitu przez Anne ♻️ Refactored `calculator.py`
3. Zmergowanie pull request'u #8 Anna/anna_code_refactoring co jest ostanią zmianą.


Tak natomiast wyglądała historia zmian Bogdana przed zrobieniem rebase'u.

```bash
* commit 5c58f0bdca60dbb4db072d01260f3932e71c1623 (HEAD -> bogdan_calculator_bug_fix, origin/bogdan_calculator_bug_fix)
| Author: Bogdan
| Date:   2023-10-28
|
|     🐛 Fixed bugs in `calculator.py`
|
* commit 6398b0aa3b7042ff5a26300cdbaa4d82b37c48df
| Author: Admin Bob
| Date:   2023-10-28
|
|     ✨ Added `square_root()` function
|
```

 Widać od razu nieaktualność gałęzi ponieważ nie ma tutaj zmian Anny. Właśnie to że Anna wprowadizła zmiany w tym samym miejscu co my i nasza historia commitów jest o nie nieaktualna spowodowało że git wykrył konflikt. 
 
 Zobaczmy teraz jak wygląda historia commitów po wykoaniu `git rebase` na branch'u `bogdan_calculator_bug_fix`

 ```bash
 * commit 705c6b48a3c920882f253ca5edf9f49e437ebb2e (HEAD -> bogdan_calculator_bug_fix, origin/bogdan_calculator_bug_fix)
| Author: Bogdan
| Date:   2023-10-28
| 
|     🐛 Fixed bugs in `calculator.py`
|   
*   commit 7e57dbb616c729219cbb49beaba30d06c3346357
|\  Merge: 6398b0a ee86445
| | Author: Anna
| | Date:   2023-10-28
| | 
| |     Merge pull request #8 from Anna/anna_code_refactoring
| |     
| |     ♻️ Refactored `calculator.py`
| | 
| * commit ee8644574aeb7163ca2389d5d438e55ebf0ab638 (origin/anna_code_refactoring)
|/  Author: Anna
|   Date:   2023-10-28
|   
|       ♻️ Refactored `calculator.py`
| 
* commit 6398b0aa3b7042ff5a26300cdbaa4d82b37c48df
| Author: Admin Bob
| Date:   2023-10-28
| 
|     ✨ Added `square_root()` function
| 
 ```
 Jak widać zmiany Bogdana zostały przeniesione na szczyt historii commitów z zachowaniem kolejności poprzednich. To jest duża zaleta używania `git rebase`, dzięki tej komendzie mamy zachowaną spójną,linową,czystą historie commitów. Poniżej można zobaczy historie po finalnym zmergowaniu zmian Bogdana

```bash
|  
|   Merge pull request #9 from Bogdan/bogdan_calculator_bug_fix
*   commit a0889f3959c2bd76e3bf9130a3a536db71fd519a (HEAD -> main, origin/main, origin/HEAD)
|\  Merge: 7de122a 705c6b4
| | Author: Bogdan
| | Date:   2023-10-29
| | 
| |     Merge pull request #9 from Bogdan/bogdan_calculator_bug_fix
| |     
| |     🐛 Fixed bugs in `calculator.py`
| | 
| * commit 705c6b48a3c920882f253ca5edf9f49e437ebb2e (origin/bogdan_calculator_bug_fix, bogdan_calculator_bug_fix)
|/   Author: Bogdan
|    Date:   2023-10-28
|    
|    🐛 Fixed bugs in `calculator.py`
|   
*   commit 7e57dbb616c729219cbb49beaba30d06c3346357
|\  Merge: 6398b0a ee86445
| | Author: Anna
| | Date:   2023-10-28
| | 
| |     Merge pull request #8 from Anna/anna_code_refactoring
| |     
| |     ♻️ Refactored `calculator.py`
| | 
| * commit ee8644574aeb7163ca2389d5d438e55ebf0ab638 (origin/anna_code_refactoring)
|/  Author: Anna
|   Date:   2023-10-28
|   
|       ♻️ Refactored `calculator.py`
| 
* commit 6398b0aa3b7042ff5a26300cdbaa4d82b37c48df
| Author: Admin Bob
| Date:   2023-10-28
| 
|     ✨ Added `square_root()` function
| 
```

Cóż to by było na tyle jeśli chodzi o walke z konfliktami. Mam nadzieje że ten tutorial lepiej pomógł Ci zrozumieć to zgadnienie. Byłbym bardzo wdzięczny za informacje zwrotną odnośnie tego tutoriala i dodanie mnie do obserwujących żeby być na bierząco z kolejnymi. Dzięki i do zobaczenia ! 