# SMS_mycomsos
Send SMS via mycosmos.gr

Σίγουρα όλοι έχουμε δοκιμάσει τα "demo" api αποστολής SMS από ίντερνετ όπως το twilio.

Εδώ θα δούμε πώς μπορούμε να στείλουμε SMS μέσα από την σελίδα του mycomsos.gr. Όσοι από εσάς είσαστε παλαιοί συνδρομητές της comsote σίγουρα έχετε και πρόσβαση στην WEB εφαρμογή (με 400 SMS δωρεάν ανά μήνα).

Το σκεπτικό είναι το εξής: Σύνδεση από python στην WEB υπηρεσία και αποστολή SMS.

Κάνουμε εγκατάσταση τα απαραίτητα.
sudo apt-get install xvfb
sudo pip install PyVirtualDisplay
sudo pip install xvfbwrapper
sudo pip install selenium
sudo apt-get install chromium-driver
sudo pip install chromedriver
sudo apt-get install chromium-browser

Λειτουργία: Επειδή θέλουμε να μην ανοίγει σε κάποια οθόνη η σύνδεσή μας με την υπηρεσία του mycosmos.gr (selenium) την κάνουμε κρυφή (PyVirtualDisplay). Έτσι λοιπόν αποφεύγουμε τους περίεργους οφθαλμούς ;-)

Δίνουμε τα απαραίτητα στοιχεία για την σύνδεσή μας όπως LOGIN και PASS (προσοχή χρειάζεται να ψάξουμε την σελίδα σε μορφή "πηγαίου κώδικα" για πάρουμε τις πληροφορίες των "id" και "name" πεδίων).

Στην συνέχεια με τον ίδιο τρόπο και αφού έχουμε δει και πάλι από τον πηγαίο κώδικα της σελίδας τα πεδία που μας ενδιαφέρουν τα "γεμίζουμε" και κάνουμε αποστολή το μήνυμα μας.
