# CP68-SistemRekomendasi
Capstone Project Machine Leaning SIB Dicoding Team 068

## Latar Belakang
Peraturan [Permendikbud nomor 62 tahun 2014](https://jdih.kemdikbud.go.id/arsip/Permendikbud%20Nomor%2062%20Tahun%202014.pdf) tentang kegiatan ekstrakurikuler, menyebutkan bahwa setiap peserta didik memiliki hak mengikuti kegiatan ekstrakurikuler sesuai dengan minat dan bakat mereka. Penentuan pemilihan ekstrakurikuler berdasarkan minat dan bakat terjadi di Sekolah Menengah Atas (SMA) diserahkan sepenuhnya pada siswa. Menurut [Sari dan Simanjuntak (2020)](http://ejournal.upbatam.ac.id/index.php/comasiejournal/article/view/2141/1249) terkadang siswa cenderung bingung memilih ekstrakurikuler dikarenakan orang tua yang tidak suka dengan hobi anaknya atau siswa tersebut menganggap bahwa dirinya tidak sungguh-sungguh dengan hobi dan bakatnya. Maka dari itu dibangun sistem rekomendasi ekstrakurikuler pada siswa SMA dengan harapan membantu para siswa memilih ekstrakurikuler yang sesuai dengan mereka.

## Sistem Rekomendasi Ekstrakurikuler : Content Based Filtering
Metode Content Based Filtering digunakan dalam pembuatan model Sistem Rekomendasi Ekstrakurikuler SMA. Content Based Filtering bekerja  dengan menyarankan item serupa yang pernah disukai di masa lalu atau sedang dilihat di masa kini kepada pengguna.  Pada sistem rekomendasi ini metode content based filtering digunakan untuk merekomendasikan ekstrakurikuler berdasarkan pengalaman-pengalaman para siswa SMA terdahulu yang pernah atau sekarang sedang mengikuti ekstrakurikuler.

## Prediksi Ekstrakurikuler : Support Vector Machine (SVM)
Support Vector Machine (SVM) untuk memprediksi ekstrakurikuler yang sesuai berdasarkan minat dan bakat yang dimiliki siswa. SVM merupakan model ML multifungsi yang dapat digunakan untuk menyelesaikan permasalahan klasifikasi, regresi, dan pendeteksian outlier.

## Deployement
Deploy model Content Based Filtering dan Support Vector Machine dengan memanfaatkan flask dan menggunakan heroku untuk proses hosting web.

## DEMO
https://sistemrekomendasi68.herokuapp.com/
      
