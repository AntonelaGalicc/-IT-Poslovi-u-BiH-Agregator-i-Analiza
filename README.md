# -IT-Poslovi-u-BiH-Agregator-i-Analiza

End-to-end podatkovni projekt koji prikuplja, analizira i vizualizira oglase za posao na IT sceni u Bosni i Hercegovini.
Arhitektura Sustava (ETL)
- Extract (Web Scraping): Python (`BeautifulSoup`, `requests`) dohvaća najnovije oglase s lokalnih IT portala.
- Transform (Data Processing): `Pandas` čisti podatke, ekstrahira ključne tehnologije (Python, SQL, React...) i prepoznaje lokacije/Remote status.
- Load (Storage): Podaci se pohranjuju u `SQLite` bazu podataka.
- Dashboard (Visualization): Interaktivni `Streamlit` dashboard prikazuje analitiku traženih vještina i lokacija.

- streamlit run app.py -> pokretanje
