# Pylint-raportti

Pylint antaa seuraavan raportin sovelluksesta:

```
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:21:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:27:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:33:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:42:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:52:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:62:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:70:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:100:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:133:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:156:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:169:8: R1705: Unnecessary "else" after "return" (no-else-return)
app.py:156:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:177:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:182:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:204:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:213:8: R1705: Unnecessary "else" after "return" (no-else-return)
app.py:204:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:223:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:228:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:248:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:259:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:282:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:294:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:317:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:335:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:354:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module config
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module courses
courses.py:1:0: C0114: Missing module docstring (missing-module-docstring)
courses.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
courses.py:3:34: W0622: Redefining built-in 'credits' (redefined-builtin)
courses.py:3:0: R0913: Too many arguments (6/5) (too-many-arguments)
courses.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
courses.py:24:0: C0116: Missing function or method docstring (missing-function-docstring)
courses.py:39:0: C0116: Missing function or method docstring (missing-function-docstring)
courses.py:51:0: C0116: Missing function or method docstring (missing-function-docstring)
courses.py:56:0: C0116: Missing function or method docstring (missing-function-docstring)
courses.py:69:0: C0116: Missing function or method docstring (missing-function-docstring)
courses.py:69:48: W0622: Redefining built-in 'credits' (redefined-builtin)
courses.py:69:0: R0913: Too many arguments (6/5) (too-many-arguments)
courses.py:83:0: C0116: Missing function or method docstring (missing-function-docstring)
courses.py:88:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module db
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:18:4: E0237: Assigning to attribute 'last_insert_id' not defined in class slots (assigning-non-slot)
db.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module reviews
reviews.py:1:0: C0114: Missing module docstring (missing-module-docstring)
reviews.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:12:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:12:0: R0913: Too many arguments (6/5) (too-many-arguments)
reviews.py:21:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:35:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:52:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:66:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:71:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:81:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:86:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:98:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:104:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:12:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:32:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:39:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:47:4: R1705: Unnecessary "else" after "return" (no-else-return)

------------------------------------------------------------------
Your code has been rated at 8.01/10 (previous run: 8.01/10, +0.00)

```
Käydään seuraavaksi läpi tarkemmin raportin sisältö ja perustellaan, miksi kyseisiä asioita ei ole korjattu sovelluksessa.

## Docstring-ilmoitukset

Suuri osa raportin ilmoituksista on seuraavan tyyppisiä ilmoituksia:

```
app.py:70:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:100:0: C0116: Missing function or method docstring (missing-function-docstring)
```

Nämä ilmoitukset tarkoittavat, että moduuleissa ja funktioissa ei ole docstring-kommentteja. Sovelluksen kehityksessä on tehty tietoisesti päätös, ettei käytetä docstring-kommentteja.

## Tarpeeton else

Raportissa on seuraavat ilmoitukset liittyen `else`-haaroihin:

```
app.py:169:8: R1705: Unnecessary "else" after "return" (no-else-return)
users.py:47:4: R1705: Unnecessary "else" after "return" (no-else-return)
```

Esimerkiksi ensimmäinen ilmoitus koskee seuraavaa koodia:

```python
if request.method == "POST":
    if "remove" in request.form:
        courses.remove_course(course_id)
        return redirect("/")
    else:
        return redirect("/course/" + str(course_id))
```

Tämä koodi olisi mahdollista kirjoittaa tiiviimmin ilman `else` -haaraa, mutta sovelluksen kehittäjän näkemyksen mukaan tällaisissa tapauksissa on selkeämpää kirjoittaa `else`-haara, koska se tuo esille kaksi vaihtoehtoa, miten koodi voi toimia

## Puuttuva palautusarvo

Raportissa on seuraavat ilmoitukset liittyen funktion palautusarvoon:

```
app.py:156:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:204:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)

```

Nämä ilmoitukset liittyvät tilanteeseen, jossa funktio käsittelee metodit `GET` ja `POST` mutta ei muita metodeja. Esimerkiksi ensimmäinen ilmoitus koskee seuraavaa funktiota:

```python
@app.route("/remove_course/<int:course_id>", methods=["GET", "POST"])
def remove_course(course_id):
    require_login()

    course = courses.get_course(course_id)
    if not course:
        abort(404)
    if course["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove_course.html", course=course)

    if request.method == "POST":
        if "remove" in request.form:
            courses.remove_course(course_id)
            return redirect("/")
        else:
            return redirect("/course/" + str(course_id))
```

Tässä funktio palauttaa arvon, kun `request.method` on `GET` tai `POST`, mutta periaatteessa voisi tulla tilanne, jossa `request.method` on jotain muuta eikä koodi palauttaisi arvoa. Käytännössä tällainen tilanne ei ole kuitenkaan mahdollinen, koska funktion dekoraattorissa on vaatimus, että metodin tulee olla `GET` tai `POST`. Niinpä tässä tapauksessa ei ole riskiä, että funktio ei jossain tilanteessa palauttaisi arvoa.

## Vakion nimi

Raportissa on seuraava ilmoitus liittyen vakion nimeen:

```
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
```

Tässä koodin päätasolla määritelty muuttuja tulkitaan vakioksi, jonka nimen tulisi olla kirjoitettu suurilla kirjaimilla. Kuitenkin sovelluksen kehittäjän näkemyksen mukaan tässä tilanteessa näyttää paremmalta, että muuttujan nimi on pienillä kirjaimilla. Muuttujaa käytetään koodissa näin:

```python
app.secret_key = config.secret_key
```

## Liikaa argumentteja

Raportissa on seuraava ilmoitus liittyen funktion argumenttien määrään:

```
courses.py:3:0: R0913: Too many arguments (6/5) (too-many-arguments)
courses.py:69:0: R0913: Too many arguments (6/5) (too-many-arguments)
reviews.py:12:0: R0913: Too many arguments (6/5) (too-many-arguments)
```

Esimerkiksi ensimmäinen ilmoitus koskee seuraavaa funktiota:

```python
def add_course(name, code, grade, credits, user_id, classes):
    sql = "INSERT INTO courses (name, code, grade, credits, user_id) VALUES (?, ?, ?, ?, ?)"
    db.execute(sql, [name, code, grade, credits, user_id])

    course_id = db.last_insert_id()

    sql = "INSERT INTO course_classes (course_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [course_id, title, value])
```

Pylintin oletusraja on viisi argumenttia, mutta sovelluksen kehityksessä on katsottu, että kuusi argumenttia on tässä tapauksessa perusteltua, koska ne kaikki ovat lisättävän kurssin kannalta välttämättömiä tietoja. Argumenttien pakkaaminen esimerkiksi sanakirjaan tai erilliseen olioon vain Pylint-ilmoituksen välttämiseksi tekisi koodista tässä vaiheessa tarpeettoman monimutkaista ja vähemmän läpinäkyvää.

## Sisäänrakennetun nimen uudelleenmäärittely

Raportissa on seuraava ilmoitus liittyen muuttujan nimeämiseen:

```
courses.py:3:34: W0622: Redefining built-in 'credits' (redefined-builtin)
```

Pylint huomauttaa, että muuttujan nimi `credits` on sama kuin Pythonin sisäänrakennetun `credits()` -funktion nimi.

Kuitenkin sovelluksen kontekstissa `credits` on luontevin ja selkein termi kuvaamaan kurssin opintopisteitä. Pythonin omaa `credits()` -funktiota käytetään lähinnä interaktiivisessa tulkissa, eikä sen peittäminen tässä paikallisessa funktiossa aiheuta sovellukselle mitään toiminnallista haittaa. Nimen säilyttäminen ennallaan pitää koodin myös yhtenäisenä tietokannan sarakkeiden ja HTML-lomakkeen kenttien kanssa.

## Määrittelemätön attribuutti

Raportissa on seuraava ilmoitus liittyen attribuutin asettamiseen:

```
db.py:18:4: E0237: Assigning to attribute 'last_insert_id' not defined in class slots (assigning-non-slot)
```

Tämä ilmoitus liittyy Flask-sovelluksen g-olion käyttöön, johon tallennetaan viimeisimmän lisäyksen ID:

```
g.last_insert_id = result.lastrowid
```
Pylint tulkitsee Flaskin g-olion tavalliseksi Python-luokaksi, jolla on rajoitetut muuttujapaikat (slots), eikä se ymmärrä g-olion dynaamista luonnetta. Flask-ympäristössä g-olioon on nimenomaan tarkoitus voida asettaa dynaamisesti uusia attribuutteja pyynnön elinkaaren ajaksi. Ilmoitus on siis virheellinen tulkinta Pylintiltä, ja koodi toimii Flask-ympäristössä täysin oikein.


