# Kura - Kurssien Rehelliset Arvostelut

**Kura** on verkkosovellus, jonka avulla opiskelijat voivat lisätä ja jakaa kurssiarvosteluja sekä etsiä muiden kokemuksia. Sovelluksen keskiössä on opiskelijoiden tuottama rehellinen tieto: vastaako kurssin työmäärä opintopisteitä, kuinka haastava kurssi todellisuudessa on ja mikä on sen yleinen arvosana muiden opiskelijoiden silmissä.

## Tulossa olevat toiminnot

### Perusominaisuudet (Arvosana 3)
* **Käyttäjienhallinta:** Käyttäjä voi luoda tunnuksen, kirjautua sisään ja hallinnoida omaa profiiliaan.
* **Kurssien hallinta:** Käyttäjät voivat lisätä uusia kursseja (nimi, koodi, opintopisteet) sekä muokata tai poistaa omia lisäyksiään.
* **Arvostelut (toissijaiset tietokohteet):** Käyttäjät voivat jättää kursseista arvosteluja, jotka sisältävät numeerisia arvioita (yleisarvosana, vaikeus, työmäärän vastaavuus) ja sanallista palautetta.
* **Haku ja suodatus:** Kursseja voi etsiä hakusanalla tai suodattaa luokittelun (kategorioiden) perusteella.
* **Käyttäjäsivu ja tilastot:** Käyttäjä näkee omat suorituksensa ja tilastoja sovelluksen käytöstä.

## Lisäominaisuudet (Arvosanat 4 ja 5)
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

* **Projektin seuranta:** Voit seurata kehityksen vaiheita ja tulevia ominaisuuksia [TODO.md-tiedostosta]([TODO.md](https://github.com/ValioEilax/kura/blob/main/todo.md)).
* **Pylint:** Lopullinen Pylint-raportti ja selitykset mahdollisista huomautuksista lisätään tiedostoon `pylint-report.md` sovelluksen valmistuttua.
* **Suuren tietomäärän testaus:** Testaustulokset, suorituskykyanalyysi ja SQL-indeksien vaikutus raportoidaan tiedostossa `testing-report.md` projektin loppuvaiheessa.
