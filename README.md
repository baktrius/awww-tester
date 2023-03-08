# Tester projektu z AWWW
## Wymagania
- Firefox
- Python3
- Nodejs
(Spełnione na students)
## Instalacja

1. Pobierz kod projektu
   Można pobrać paczkę `.zip` bezpośrednio z github'a lub sklonować repozytorium (jeśli chcemy projekt rozwijać). W celu sklonowania repozytorium można użyć komendy `git clone https://github.com/baktrius/awww-tester.git` (klonowanie do bieżącego katalogu - cały projekt będzie w folderze `awww-tester`). Należy dalej przejść do katalogu projektu
2. Należy utworzyć środowisko wirtualne pythona3 i je aktywować (w katalogu projektu)
    ```
    python3 -m virtualenv .venv
    source .venv/bin/activate
    ```
3. Należy zainstalować wymagane biblioteki pythonowe
    ```
    pip install -r requirements.txt
    ```
4. Należy zainstalować wymagane zależności nodejs za pomocą
   ```
   npm install
   ```

## Uruchomienie testów (linux)
Zmienna środowiskowa `PROJECT_PATH` powinna zawierać ścieżkę do testowanego projektu (domyślna wartość `../moje1`). Wykonanie z domyślną ścieżką
```
./test.sh
```
Wykonanie z inną ścieżką
```
PROJECT_PATH="../projekt" ./test.sh
```
(po ewentualnym uprzednim nadaniu plikowi `test.sh` odpowiednich praw do wykonania)

## Rozwijanie
Elastycznie: testy można dodawać albo jako testy pytest, albo bezpośrednio do pliku `test.sh`

## Cel
Finalnie ma pomagać oceniać projekt, może to być proces częściowo interaktywny np. można generować screeny do późniejszego przejrzenia itp. 