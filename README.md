# Kura - Kurssien Rehelliset Arvostelut

**Kura** on verkkosovellus, jonka avulla opiskelijat voivat lisätä ja jakaa kurssiarvosteluja sekä etsiä muiden kokemuksia. Sovelluksen keskiössä on opiskelijoiden tuottama rehellinen tieto: vastaako kurssin työmäärä opintopisteitä, kuinka haastava kurssi todellisuudessa on ja mikä on sen yleinen arvosana muiden opiskelijoiden silmissä.

## Keskeiset toiminnot
* **Käyttäjähallinta:** Rekisteröityminen ja sisäänkirjautuminen. Salasanat tallennetaan tietokantaan turvallisesti `werkzeug.security`-hashauksella.
* **Kurssien hallinta (CRUD):** * Käyttäjä voi lisätä uusia kursseja (nimi, koodi, opintopisteet, arvosana).
    * Käyttäjä voi muokata omia lisäyksiään.
    * Käyttäjä voi poistaa omia lisäyksiään erillisen vahvistussivun kautta.
* **Haku ja suodatus:** Kursseja voi etsiä hakusanalla kurssin nimen tai koodin (esim. "TKT10002") perusteella.
* **Tietoturva:** Sovellus tarkistaa käyttöoikeudet (omistajuuden) aina ennen muokkaus- tai poisto-operaatioita.

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

### 5. Sovelluksen käynnistys
```
flask run
```

Sovellus on nyt käytettävissä osoitteessa: http://127.0.0.1:5000

## Tulossa olevat toiminnot

### Lisäominaisuudet (Arvosanat 4 ja 5)
* **Arvostelut (toissijaiset tietokohteet):** Käyttäjät voivat jättää kursseista arvosteluja, jotka sisältävät numeerisia arvioita (yleisarvosana, vaikeus, työmäärän vastaavuus) ja sanallista palautetta.
* **Sosiaalinen syöte (Feed):** Käyttäjä voi seurata muita käyttäjiä ja nähdä heidän tuoreimmat arvostelunsa omalla etusivullaan.
* **Keskustelu ja kommentointi:** Arvosteluihin on mahdollista lisätä kommentteja (toisen tason toissijainen kohde).
* **Aggregoidut tilastot:** Kurssisivulla näytetään SQL:llä laskettuja keskiarvoja kaikkien opiskelijoiden antamista arvioista.
* **Sivutus (Pagination):** Kurssilistaukset ja syötteet on toteutettu sivutettuna suuren tietomäärän hallitsemiseksi.
* **Profiilikuvat:** Käyttäjät voivat ladata profiilikuvan (toteutettu `alt`-attribuutteja käyttäen saavutettavuuden varmistamiseksi).

## Tekniset tiedot
* **Ohjelmointikieli:** Python
* **Framework:** Flask
* **Tietokanta:** SQLite
* **Ulkoasu:** HTML ja CSS
* **Turvallisuus:** 
    * Salasanat tallennetaan käyttäen salt hashing -menetelmää.
    * CSRF-suojaus on käytössä kaikissa lomakkeissa.
    * SQL-injektiot on estetty käyttämällä parametrisoituja kyselyitä.

## Kehitys ja testaus

* **Projektin seuranta:** Voit seurata kehityksen vaiheita ja tulevia ominaisuuksia [TODO.md-tiedostosta](https://github.com/ValioEilax/kura/blob/main/todo.md).
* **Pylint:** Lopullinen Pylint-raportti ja selitykset mahdollisista huomautuksista lisätään tiedostoon `pylint-report.md` sovelluksen valmistuttua.
* **Suuren tietomäärän testaus:** Testaustulokset, suorituskykyanalyysi ja SQL-indeksien vaikutus raportoidaan tiedostossa `testing-report.md` projektin loppuvaiheessa.
