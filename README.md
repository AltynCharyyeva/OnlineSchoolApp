# OnlineSchoolApp
INFORMATIA GENERALA
Aceasta este un web-app simplu care gestioneaza inscrierea userilor la cursuri online. Cursurile sunt despre programare in diferite limbaje. Informatii despre cursuri si despre traineri se poate vizualiza pe site.
Pentru a inscrie la un curs userul trebuie sa faca un cont si dupa aia un login. Daca registrarea, logarea sau inscrierea a terminat cu success apare un mesaj de success. 

DESPRE IMPLEMENTARE
Sunt 4 tabele in baza de date: Trainer, Student, Course, User, School_onfo
Relatii intre tabele:
Trainer si Student => ManyToMany;
Course si Student => ManyToMany;
Trainer si Course => OneToMany;

Backendul este implementat cu Django (python)
Frontendul este implementat cu Html, CSS
