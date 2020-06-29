############# RSA #############
####### Author: aalp75 ########
####### Edited in 2020 ########


Contents
I   - RSA
II  - Prime Number
III - Code
IV  - How to run
V   - Examples

I - RSA

This Notebook replicate the famous cryptosystem RSA

II - Prime Number

You can also find a file PrimeNumber.py (or in Notebook Jupyter). This file contains all basic function with prime number.

PGC: Greatest Common Divisor
is_prime_number: naive method and Miller-Rabin test
Integer factorization: naive method and Pollars Rho decomposition


III - Code

RSA is represented as a a class

with attribute

 p : 1st big prime number
 q : 2nd big prime number
 n : n * q
 phi : (p-1)*(q-1)
 e : public key
 d : private key

 e is the 1st prime number bigger than p and q

 d the inverse of e is calculated with the Extended Euclidean algorithm

 You can test the robustness of you chose of p and q by applying the Pollars Rho decomposition on n, to see how hard it's hard to find back p and q.

 The function Miller-Rabin test and Pollard Rho decomposition are not by myself

 Miller-Rabin test: Wikipedia
 Pollars Rho: Les recettes python de Tyrtamos

 IV - How to run

Create a RSA object with RSA(p,q)
If p or q are not prime number you can see an error message

Print the public key with public_key and the private key with private_key()

Write your text in message_clean.txt

Use the function encrypt_file('message_clean.txt') and the message is encrypt in message_encrypt.txt

For decrypt the message use decrypt_file ('message_encrypt.txt') and the message is back clean in message_decrypt.txt

V - Examples

Basic example with p = 379 and q = 467 but for more robustness we recommend you to take p and q at least of length 100 number.
You need to take at least p et q such that p*q > 9999 because we regroup the number by bloc of 4 (possibility to change this with self.bloc) to avoid frequency analysis

-> rsa = RSA(p,q)

RSA system created with succes
Public Key :
(n,e) = (493,31)
Private Key :
(n,d) = (493,159)

#####message_clean.txt#####

Maître Corbeau, sur un arbre perché,
Tenait en son bec un fromage.
Maître Renard, par l'odeur alléché,
Lui tint à peu près ce langage :
Et bonjour, Monsieur du Corbeau.
Que vous êtes joli ! que vous me semblez beau !
Sans mentir, si votre ramage
Se rapporte à votre plumage,
Vous êtes le Phénix des hôtes de ces bois.
À ces mots, le Corbeau ne se sent pas de joie ;
Et pour montrer sa belle voix,
Il ouvre un large bec, laisse tomber sa proie.
Le Renard s'en saisit, et dit : Mon bon Monsieur,
Apprenez que tout flatteur
Vit aux dépens de celui qui l'écoute.
Cette leçon vaut bien un fromage, sans doute.
Le Corbeau honteux et confus
Jura, mais un peu tard, qu'on ne l'y prendrait plus.

-> rsa.encrypt_file('message_clean.txt')

#####message_encrypt.txt#####

["57663", "85219", "99491", "155579", "23970", "169480", "154466", "24708", "152411", "37377", "142923", "59654", "109089", "95568", "14299", "109089", "72692", "169480", "5061", "70210", "92853", "78710", "122360", "42356", "160503", "32076", "86726", "12544", "112144", "42356", "102886", "25981", "129166", "143473", "169104", "1724", "96606", "169104", "169480", "27872", "175767", "1724", "81192", "108293", "97078", "122016", "108125", "38210", "135364", "118172", "139462", "71533", "70382", "21518", "889", "107993", "168490", "120309", "32785", "92853", "166758", "75225", "154017", "5061", "75225", "30032", "129607", "57720", "42356", "81192", "75225", "38210", "9045", "61755", "169313", "63846", "145363", "139462", "49772", "25981", "1724", "10750", "169399", "129166", "147870", "75225", "91714", "120309", "158435", "91714", "10016", "37485", "169480", "153430", "107993", "30032", "5061", "78710", "38210", "135364", "107993", "86959", "126544", "111727", "169480", "10313", "169104", "119832", "167167", "71001", "59654", "148843", "89048", "72762", "36910", "43785", "70599", "63640", "65746", "58989", "90781", "89048", "14299", "27872", "170665", "58989", "15259", "23507", "70599", "78710", "152790", "167167", "81192", "108037", "47837", "10750", "173375", "1724", "57645", "162564", "89572", "119662", "20466", "6211", "120721", "107993", "42622", "167167", "148443", "1724", "79412", "107993", "136283", "27023", "156786", "96710", "71472", "89640", "152411", "37377", "142923", "169480", "122303", "115187", "38210", "42356", "108037", "158379", "120309", "108719", "134041", "63831", "75225", "136283", "169167", "152790", "167167", "155579", "23970", "1724", "160503", "126440", "38210", "135364", "16627", "12822", "78710", "29332", "38210", "133204", "147686", "92853", "10750", "107993", "56745", "109089", "159381", "21518", "889", "107993", "91714", "69456", "126440", "38210", "135364", "43368", "139462", "86922", "171007", "87385", "144283", "142026", "42356", "148353", "21913", "16627", "38689", "99354", "56001", "16627", "95018", "1724", "77184", "173375", "1724", "52564", "142026", "42356", "148353", "65746", "16627", "149405", "57268", "87385", "149405", "159381", "134041", "5858", "84455", "84143", "149405", "57268", "87385", "143473", "8869", "21518", "5858", "75225", "96710", "78710", "89225", "167167", "160503", "38309", "38210", "18505", "67374", "16627", "109089", "43785", "1724", "36910", "169104", "129166", "109089", "130297", "87385", "143473", "29749", "1724", "57645", "95230", "16627", "55096", "29437", "102626", "156399", "122360", "167167", "81192", "75225", "158379", "167167", "108719", "92853", "120309", "75225", "87385", "107060", "94719", "42356", "9045", "38309", "1724", "31497", "95230", "2109", "12544", "44658", "30032", "109089", "171007", "42622", "889", "107993", "70599", "36111", "21913", "38210", "889", "65127", "169480", "27872", "175767", "59654", "143473", "53937", "134041", "96606", "43785", "1724", "155579", "108125", "152411", "120309", "75225", "87385", "107060", "122360", "92853", "169104", "43785", "23128", "10567", "57496", "169480", "171485", "169104", "38210", "889", "108293", "87385", "16393", "169104", "1724", "154198", "25981", "136283", "43097", "97481", "1724", "120309", "27389", "119216", "43097", "27389", "86959", "148843", "89048", "57720", "149405", "159381", "57720", "148843", "89048", "72762", "36910", "43785", "70599", "63831", "15124", "41876", "133204", "29332", "42356", "16627", "125676", "1724", "151042", "43974", "1724", "155579", "171007", "129166", "143473", "21913", "38210", "155579", "57496", "70599", "117684", "113825", "134041", "156399", "130297", "70599", "33871", "65746", "56001", "118942", "169104", "87385", "143473", "29749", "169480", "153430", "162564", "70599", "169167", "138939", "70599", "169167", "21913", "60097", "116177", "8869", "70599", "10750", "118172", "139462", "122955", "79191", "21518", "78710", "21913", "103651", "15646", "169104", "1724", "29058", "142923", "129166", "149405", "97882", "42356", "36111", "32382", "57720", "143473", "29332", "167167", "163167", "131810", "16627", "70578", "37485", "38210", "42356", "108037", "119216", "167167", "34381", "16627", "15259", "50718", "16627", "90781", "89048", "14299", "27872", "170665", "58989", "143473", "173032", "72762", "10750", "171007", "2109", "143473", "79191", "169480", "148856", "169104", "97078", "81192", "15131", "94514", "81192", "65529", "59654", "143473", "175478", "134041", "148353", "32382", "57720", "109089", "19946", "58989", "109089", "87793", "92853", "166758", "75225", "6211", "18505", "8869", "57720", "109089", "29749", "1724", "163611", "112947", "1724", "133204", "23970", "72762", "59037", "65529", "134041", "156399", "122360", "96710", "81192", "95981"]

-> rsa.decrypt_file('message_encrypt.txt')

#####message_decrypt.txt#####

Maître Corbeau, sur un arbre perché,
Tenait en son bec un fromage.
Maître Renard, par l'odeur alléché,
Lui tint à peu près ce langage :
Et bonjour, Monsieur du Corbeau.
Que vous êtes joli ! que vous me semblez beau !
Sans mentir, si votre ramage
Se rapporte à votre plumage,
Vous êtes le Phénix des hôtes de ces bois.
À ces mots, le Corbeau ne se sent pas de joie ;
Et pour montrer sa belle voix,
Il ouvre un large bec, laisse tomber sa proie.
Le Renard s'en saisit, et dit : Mon bon Monsieur,
Apprenez que tout flatteur
Vit aux dépens de celui qui l'écoute.
Cette leçon vaut bien un fromage, sans doute.
Le Corbeau honteux et confus
Jura, mais un peu tard, qu'on ne l'y prendrait plus.
