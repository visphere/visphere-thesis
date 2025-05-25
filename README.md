![](.github/banner.png)

# Projekt inżynierski

Komunikator internetowy oparty o technologie Websockets i Apache Kafka.

## Streszczenie

Projekt ma na celu przedstawienie możliwości wymiany danych między aplikacjami w środowisku rozproszonym przy użyciu
Apache Kafka oraz komunikacji z klientem z wykorzystaniem protokołu Websocket na przykładzie prostej aplikacji wymiany
wiadomości w czasie rzeczywistym. Wykonanie pracy polegało na stworzeniu dwóch osobnych warstw: wizualnej oraz
serwerowej. Architektura serwerowa została rozdzielona na kilka mikrousług odpowiadających za konkretne cele biznesowe
aplikacji (uwierzytelnianie, obsługa czatu, przetwarzanie plików itp.). Każdy mikroserwis stanowi osobny serwer
aplikacji z własną bazą danych. Komunikacja między mikroserwisami została zapewniona przez architekturę sterowaną
zdarzeniami i system Apache Kafka. Sama komunikacja z aplikacją klienta została zrealizowana przy użyciu interfejsu
REST, protokołu Websocket oraz zaimplementowanego serwera brzegowego. Wykonany system umożliwia kilka operacji. Są to
m.in. utworzenie konta, zarządzanie pokojami do rozmów, kanałów tekstowych oraz wysyłanie wiadomości z opcjonalnymi
załącznikami w formie plików. Stworzony system mimo swojej zewnętrznej prostoty zawiera wiele zaawansowanych konceptów z
zakresu architektury mikrousługowej. Rozwiązują one problemy aplikacji projektowanych na systemy rozproszone które nie
występują (lub występują w nieznacznym stopniu) w aplikacjach monolitycznych.

## Słowa kluczowe

* system czatu,
* mikroserwisy,
* architektura sterowana zdarzeniami,
* apache kafka,
* websockety,
* apache cassandra,
* kontenery docker.

## Kompilacja

W celu poprawnej kompilacji dokumentów LaTeX oraz kodów źródłowych niezbędne jest następujące oprogramowanie i pakiety:

* **[LaTeX](https://www.latex-project.org)** (preferowany pakiet [TeX Live](https://www.tug.org/texlive), wymagany
  kompilator **LuaTeX**),
* **[Inkscape](https://inkscape.org/release)** (do konwersji grafik SVG na PDF - musi być dostępny z poziomu linii
  komend),
* **[Python](https://www.python.org/downloads)** (jedynie dla kompilacji z poziomu linii komend).

### Klonowanie repozytorium

Klonowanie repozytorium:

```bash
$ git clone https://github.com/visphere/visphere-thesis
$ cd visphere-thesis
```

### Kompilacja z poziomu linii komend

W celu kompilacji z poziomu linii komend należy uruchomić skrypt `run.py` w głównym folderze projektu.

```bash
$ python run.py
```

Komenda przyjmuje następujące argumenty:

```
--quiet       (opcjonalny)    jeśli ustawiony, nie generuje żadnych logów z podczas kompilacji LaTeX
```

Wynikowy plik .pdf po etapie kompilacji będzie znajdować się w folderze `build`.

### Kompilacja z poziomu programu Visual Studio Code

W folderze `.vscode` przygotowane są konfiguracje umożliwiające kompilację w programie Visual Studio Code. Minimalnie
należy mieć zainstalowanego Inkscape'a (dostępnego z poziomu linii komend) wraz z rekomendowanymi rozszerzeniami,
(między innymi LaTeX Workshop) znajdującymi się w katalogu `.vscode/extensions.json`.

Domyślna komenda `latexmk` jest ustawiona na kompilator `LuaTeX` oraz umożliwa kompilację obrazków z wykorzystaniem
Inkscape. W celu kompilacji należy zawsze uruchamiać budowanie przy użyciu komendy `latexmk`, nie `latexmk (lualatex)`!

---

Politechnika Śląska, Wydział Elektryczny, 2024.
