# DFA-minimization
<br />
&emsp;In cadrul acestui proiect am implementat procedeul de minimizare a unui Automat Finit Determinist dat ca input prin intermediul unui fisier text. <br />
&emsp;Mai exact, stim ca un DFA poate avea mai multe stari initiale si/sau mai multe stari finale si, de asemenea, pot exista mai multe drumuri care sa duce dinspre un nod spre altul, permitand transmiterea aceluiasi mesaj, deci putem spune ca acele muchii sunt duble, deci redundante. <br />
&emsp;Minimizarea unui DFA presupune ca daca avem mai multe stari initiale sa adaugam o noua stare initiala (momentan inexistenta in automat) din care sa ne ducem cu lambda muchii inspre vechile stari initiale, iar daca avem mai multe stari finale sa adaugam o noua stare finala (momentan inexistenta in automat) in care sa ne ducem cu lambda muchii dinspre vechile stari finale. Astfel, vom obtine un nou automat care sa aiba o singura stare initiala si o singura stare finala. Mai departe, trebuie sa asociem muchiile care pornesc dintr-un nod si ajung in acelasi nod cu un acelasi limbaj, astfel incat sa eliminam muchiile duble (redundante). <br /><br />
&emsp;Inputul necesar executarii acestui program este de tipul:<br />
&emsp;&emsp;lista_noduri_automat (starile existente) <br />
&emsp;&emsp;lista_alfabet_modelat <br />
&emsp;&emsp;lista_stari_initiale (poate fi si una singura) <br />
&emsp;&emsp;lista_stari_finale (poate fi si una singura) <br />
&emsp;&emsp;nr_muchii <br />
&emsp;Pentru fiecare muchie: <br />
&emsp;&emsp;nod_start nod_final cod_acceptat <br /><br />
&emsp;Outputul va afisa in consola prima data structura automatului care trebuie minimizat, dupa transformarea starilor initiale si finale (daca este cazul), iar apoi se va prezenta structura acestuia dupa minimizare. <br /><br />
&emsp;Un exemplu de input poate fi regasit in fisierul de intrare 'int'. <br />
&emsp;&emsp; **a b c d e f** <br />
&emsp;&emsp; **0 1** <br />
&emsp;&emsp; **a** <br />
&emsp;&emsp; **c d e** <br />
&emsp;&emsp; **12** <br />
&emsp;&emsp; **a 0 b** <br />
&emsp;&emsp; **a 1 c** <br />
&emsp;&emsp; **b 0 a** <br />
&emsp;&emsp; **b 1 d** <br />
&emsp;&emsp; **c 0 e** <br />
&emsp;&emsp; **c 1 f** <br />
&emsp;&emsp; **d 0 e** <br />
&emsp;&emsp; **d 1 f** <br />
&emsp;&emsp; **e 0 e** <br />
&emsp;&emsp; **e 1 f** <br />
&emsp;&emsp; **f 0 f** <br />
&emsp;&emsp; **f 1 f** <br /><br />
&emsp;Outputul corespunzator acestuia este: <br />
&emsp;&emsp; **Inainte de minimizare:** <br />
&emsp;&emsp; **a -- 0 --> b** <br />
&emsp;&emsp; **a -- 1 --> c** <br />
&emsp;&emsp; **b -- 0 --> a** <br />
&emsp;&emsp; **b -- 1 --> d** <br />
&emsp;&emsp; **c -- 0 --> e** <br />
&emsp;&emsp; **c -- 1 --> f** <br />
&emsp;&emsp; **d -- 0 --> e** <br />
&emsp;&emsp; **d -- 1 --> f** <br />
&emsp;&emsp; **e -- 0 --> e** <br />
&emsp;&emsp; **e -- 1 --> f** <br />
&emsp;&emsp; **f -- 0 --> f** <br />
&emsp;&emsp; **f -- 1 --> f** <br />
&emsp;&emsp; **@ -- 0 --> @** <br />
&emsp;&emsp; **@ -- 1 --> @** <br />
&emsp;&emsp; **Dupa minimizare:** <br />
&emsp;&emsp; **Noua stare initiala este: a,b** <br />
&emsp;&emsp; **Noua stare finala este: c,d,e** <br />
&emsp;&emsp; **Noul automat are: 3 stari** <br />
&emsp;&emsp; **c,d,e -- 0 --> c,d,e** <br />
&emsp;&emsp; **c,d,e -- 1 --> @,f** <br />
&emsp;&emsp; **a,b -- 0 --> a,b** <br />
&emsp;&emsp; **a,b -- 1 --> c,d,e** <br />
&emsp;&emsp; **@,f -- 0 --> @,f** <br />
&emsp;&emsp; **@,f -- 1 --> @,f** <br />


