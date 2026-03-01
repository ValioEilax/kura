# Kura - Kurssien Rehelliset Arvostelut

**Kura** on verkkosovellus, jonka avulla opiskelijat voivat lisätä ja jakaa kurssiarvosteluja sekä etsiä muiden kokemuksia. Sovelluksen keskiössä on opiskelijoiden tuottama rehellinen tieto: vastaako kurssin työmäärä opintopisteitä, kuinka haastava kurssi todellisuudessa on ja mikä on sen yleinen arvosana muiden opiskelijoiden silmissä.

## Keskeiset toiminnot
* **Käyttäjähallinta:** Rekisteröityminen ja sisäänkirjautuminen. Salasanat tallennetaan tietokantaan turvallisesti `werkzeug.security`-hashauksella.
* **Kurssien hallinta (CRUD):**
    * Käyttäjä voi lisätä uusia kursseja (nimi, koodi, opintopisteet, arvosana).
    * Käyttäjä voi muokata omia lisäyksiään.
    * Käyttäjä voi poistaa omia lisäyksiään erillisen vahvistussivun kautta.

* **Datan validointi (Luokat):** Kursseille voidaan lisätä luokkia (esim. suoritustapa), joiden oikeellisuus tarkistetaan palvelimella "whitelist"-tekniikalla. Tämä varmistaa, että lomakkeelta tuleva tieto täsmää tietokannan sallittujen kategorioiden kanssa, mikä estää virheellisen datan tallentamisen.
  
* **Haku ja suodatus:** Kursseja voi etsiä hakusanalla kurssin nimen, koodin tai käyttäjätunnuksen (esim. "TKT10002" tai "pelaaja2") perusteella.

* **Aggregoidut tilastot:** Käyttäjän profiilissa näytetään SQL:llä laskettu kaikkien suoritettujen kurssien arvosanojen painotettu keskiarvo sekä opintopisteiden summa.

* **Arvostelut (toissijaiset tietokohteet):**
   * Käyttäjä voi jättää suorittamistaan kursseista arvosteluja, jotka sisältävät numeerisia arvioita (vaikeus, työmäärän    vastaavuus, yleisarvosana) ja sanallista       palautetta.
   * Kaikki CRUD ominaisuudet pätevät myös kurssien arvosteluihin.

* **Sosiaalinen syöte:** Käyttäjä voi nähdä myös muiden käyttäjien suorittamia kursseja sekä heidän arvosteluja omalla etusivullaan.

* **Keskustelu ja kommentointi:** Arvosteluihin on mahdollista lisätä kommentteja (toisen tason toissijainen kohde).
  
*  **Sivutus (Pagination):** Etusivulla näkyvät listaukset lisätyistä kursseista sekä arvosteluista ovat toteutettu sivutettuna suuren tietomäärän hallitsemiseksi.

* **Käyttäjäpalaute (Flash-viestit):** Sovellus käyttää Flash-viestejä antaakseen välittömän kuittauksen suoritetuista toiminnoista, kuten onnistuneesta kommentin lisäyksestä tai varoituksen virheellisestä syötteestä.

## Käyttöönotto-ohjeet

Näiden ohjeiden avulla voit testata sovellusta itse:

### 1. Kloonaa repositorio
```
git clone git@github.com:ValioEilax/kura.git
```
```
cd kura
```

### 2. Luo ja aktivoi virtuaaliympäristö
```
python3 -m venv venv
```
```
source venv/bin/activate
```

### 3. Asenna tarvittavat kirjastot
```
pip install -r requirements.txt
```

### 4. Tietokannan alustus
```
sqlite3 database.db < schema.sql
```
```
sqlite3 database.db < init.sql
```

### 5. Sovelluksen käynnistys
```
flask run
```

Sovellus on nyt käytettävissä osoitteessa: http://127.0.0.1:5000

## Jatkokehitysideoita
* **Sivutus:** Tällä hetkellä sivutus on toteutettu vain etusivulle. Jatkokehityksessä sivutus kehitetään Haku- ja käyttäjäprofiilisivuille sekä arvostelujen kommentteihin.
* **Paremmat testit suurella tietomäärällä:** Nykyisest testit lähinnä testaavat sovelluksen etusivun toimivuutta, kun tietomäärä on suuri. Tulevat testit kattaa myös haun ja kommenttiosion toimivuuden suurella tietomäärällä. 

## Tekniset tiedot
* **Ohjelmointikieli:** Python
* **Framework:** Flask
* **Tietokanta:** SQLite
* **Ulkoasu:** HTML ja CSS
* **Turvallisuus:** 
    * Salasanat tallennetaan käyttäen salt hashing -menetelmää.
    * CSRF-suojaus on käytössä kaikissa lomakkeissa.
    * SQL-injektiot on estetty käyttämällä parametrisoituja kyselyitä.
 
## Tietoturva

Sovellus on suojattu kriittisimpiä verkkohaavoittuvuuksia vastaan:
   *  **Käyttöoikeudet:** Käyttäjän omistajuus (user_id) tarkistetaan aina palvelimella ennen tietojen muokkausta tai poistoa.
   *  **SQL-injektio:** Estetty käyttämällä parametrisoituja kyselyitä, jolloin käyttäjän syöte käsitellään vain datana eikä suoritettavana koodina.
   *  **CSRF:** Kaikki lomakkeet on suojattu CSRF-tokeneilla.
   *  **XSS:** Suojattu XSS-estolla (Jinja2-moottorin automaattinen eskaappaus), joka estää haitallisten skriptien suorittamisen selaimessa.

## Kehitys

* **Projektin seuranta:** TODO -tiedosto näkyvillä, jos haluaa nähdä, miten sovelluksen kehitysvaiheet oli jaoteltu. [TODO.md-tiedostosta](https://github.com/ValioEilax/kura/blob/main/todo.md).
* **Koodin laatu (Pylint):** Sovelluksen lähdekoodi on analysoitu Pylint-työkalulla. Kattava raportti pisteytyksineen ja huomautusten selityksineen löytyy täältä: [pylint-report.md-tiedostosta](https://github.com/ValioEilax/kura/blob/main/pylint-report.md).


## Sovelluksen testaus suurella tietomäärällä
Sovellus on testattu dummy testiainestolla, jonka avulla saadaan selvitettyä sovelluksen suorituskyky, kun tietokannan rivimäärät kasvavat merkittävästi.

Tietokanta täytettiin `seed.py`-skriptillä seuraavilla määrillä:

| Entiteetti | Määrä |
| :--- | :--- |
| **Käyttäjät** | 1 000 |
| **Kurssit** | 100 000 |
| **Arvostelut** | 100 000 |
| **Kommentit** | 1 000 000 |

### Testitulokset ja havainnot

#### 1. Sivujen lataus (Sivutus) - NOPEA
Etusivun ja listausten lataaminen on erittäin nopeaa (alle 50ms). 
- **Tekniikka:** Sovelluksessa käytetään SQL-sivutusta (`LIMIT` ja `OFFSET`), jolloin kerrallaan ladataan vain 10 riviä.
- **Optimointi:** Kurssien kysely käyttää `ORDER BY id` -komentoa. Koska `id` on pääavain (Primary Key), SQLite hyödyntää sen automaattista indeksiä, mikä tekee järjestämisestä välitöntä jopa 100 000 rivin joukosta. Arvostelut järjestetään `created_at`-sarakkeen mukaan.

#### 2. Arvostelun avaaminen ja kommentit - NOPEA
Yksittäisen arvostelun avaaminen ja siihen liittyvien kommenttien lataaminen on välitöntä, vaikka kommentteja on yhteensä miljoona.
- **Optimointi:** Kommenttien hakuun on luotu erillinen indeksi:
  ```sql
  CREATE INDEX idx_review_comments ON comments (review_id);
  ```
#### 3. Hakutoiminto - HIDAS
Hakutoiminto on testatun kokonaisuuden ainoa osa-alue, jossa suuri datamäärä aiheuttaa isompaa viivettä. Kun hakutuloksia on paljon (esim. `seed.py`-skriptin täytön jälkeen haku "TKT"), vasteaika nousee noin yhteen sekuntiin.
```
127.0.0.1 - - [01/Mar/2026 15:29:36] "GET /search?query=TKT HTTP/1.1" 200 -
elapsed time: 1.03 s
```
- **Optimointi** Hakua voitaisiin optimoida käyttämällä SQL-sivutusta (`LIMIT` ja `OFFSET`), jolloin sivulle ladattaisiin kerralla huomattavasti pienempi määrä tuloksia.
