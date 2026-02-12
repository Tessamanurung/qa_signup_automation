QA Signup Automation
Description
Script ini mengotomasi seluruh proses signup pada website berikut:
https://authorized-partner.vercel.app/
Automation mencakup seluruh flow tanpa intervensi manual, termasuk:
1. Klik checkbox persetujuan
2. Klik tombol Continue
3. Mengisi form data diri (First Name, Last Name, Email, Phone, Password, Confirm Password)
4. Submit form
5. Menangani multi-step signup hingga proses selesai
6. Script memastikan seluruh halaman signup diproses secara otomatis.

Environment / Setup
1. Python 3.11 
2. Google Chrome versi terbaru
3. Selenium
4. WebDriver Manager

Install dependencies dengan menjalankan:
1. pip install -r requirements.txt
2. Script menggunakan WebDriver Manager sehingga ChromeDriver akan otomatis diunduh sesuai versi Chrome.

How to Run
1. Buka terminal di folder repository.
2. Jalankan perintah berikut:
python signup_automation_script.py
3. Browser akan terbuka otomatis.
4. Script akan menjalankan seluruh flow signup tanpa intervensi manual.
5. Setelah selesai, browser akan tertutup otomatis.

Test Data Used
1. First Name: Tessa
2. Last Name: Manurung
3. Email: tessa12234@gmail.com
4. Phone Number: 0812234546
5. Password: PasswordRahasia1223!

Expected Outcome
1. Browser terbuka secara otomatis.
2. Checkbox persetujuan berhasil diklik.
3. Tombol Continue berhasil diklik.
4. Form berhasil diisi otomatis.
5. Form berhasil disubmit.
6. Semua step signup selesai secara otomatis.
7. URL terakhir menunjukkan bahwa proses signup telah diproses.

Additional Notes
1. Script menggunakan explicit wait (WebDriverWait) untuk memastikan elemen tersedia sebelum diinteraksi.
2. Tidak ada langkah manual yang diperlukan.
3. Jika struktur halaman berubah, locator dapat diperbarui pada bagian script.
4. Automation ini memenuhi requirement: entire signup flow fully automated.
