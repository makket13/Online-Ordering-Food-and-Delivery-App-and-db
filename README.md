Το παραπάνω αποθετήριο είναι εργασία εξαμήνου των φοιτητών Γιαννακάκη Αναστάσιου και Μακρή Κωνσταντίνου, για το μάθημα Βάσεις Δεδομένων του τμήματος Ηλεκτρολόγων Μηχανικών και Τεχνολογίας Υπολογιστών του Πανεπιστημίου Πατρών.

Το θέμα της εργασίας ήταν η δημιουργία μιας βάσης δεδομένων που θα διαχειρίζεται τις υπηρεσίες μιας online-delivery-and-food επιχείρησης.

Οδηγίες Εγκατάστασης

Για την χρήση της εφαρμογής χρειάζονται οι παρακάτω βιβλιοθήκες της python: 
• sqlite3 (για την επικοινωνία της εφαρμογής με την βάση δεδομένων και για την εκτέλεση εντολών sql)
• tkinter (για την γραφική διεπαφή) 
• random (για την παραγωγή των «τυχαίων» δεδομένων που χρειάστηκαν να παράγουμε για τα δεδομένα της βάσης) 
• PIL(κυρίως για την χρήση των συναρτήσεων Image και ImageTk οι οποίες βοηθάνε στη διαχείριση των φωτογραφιών στη γραφική διεπαφή μας)

Πρώτο βήμα για την χρήση της εφαρμογής είναι να γίνει χρήση του αρχείου online_food_delivery.db. Για να γίνει αυτό χρειάζεται να βρισκόμαστε στον φάκελο στον οποίο τρέχει και το αρχείο του κώδικα μας.Το ίδιο ισχύει και για τις φωτογραφίες μας τις οποίες έχουμε προσκομίσει στο παραδοτέο.Μόλις τρέξει το script δημιουργείται μια πλατφόρμα είτε εγγραφής, είτε σύνδεσης ενός πελάτη, είτε σύνδεση ως διαχειριστής με τα στοιχεία "username":"admin" και "password":"admin".

• Για τη σύνδεση ως διαχειριστής ακολουθούν 3 πλαίσια που μπορούμε να γράψουμε για να αναζητήσουμε ακριβώς αυτό που θέλουμε στο database μας. Το πρώτο παίρνει ένα variable ενός πίνακα το δεύτερο με τι θέλουμε να ισούται και το τρίτο κατά ποιο variable θέλουμε να το κάνουμε sort διαλέγοντας επίσης ascending ή descending order.(π_χ where: Κόστος , equals to: 4, Sort: Χρόνος Παράδοσης (το οποίο μας δείχνει τις παραγγέλιες που κοστίζουν 4 ευρώ και ταξινόμησε της ανάλογα με το χρόνο παράδοσης τους)

• Για τη σύνδεση ως πελάτης, μπορούμε να επιλέξουμε είτε τη δημιουργία παραγγελίας είτε να δούμε το ιστορικό παραγγελιών.
