# Tester projektu z AWWW
## Instalacja

1. Pobierz kod projektu
2. Należy utworzyć środowisko wirtualne pythona3 i je aktywować (w katalogu projektu)
    ```
    python3 -m virtualenv .venv
    source .venv/bin/activate
    ```
3. Należy zainstalować wymagane biblioteki pythonowe
    ```
    pip install -r requirements.txt
    ```
4. Należy zainstalować globalnie narzędzie [html-validator](https://www.npmjs.com/package/html-validate) (wymaga nodejs)
5. Należy mieć zainstalowanego Firefox'a

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