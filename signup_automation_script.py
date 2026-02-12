from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

print("Mulai menjalankan automation test...")

# buka browser chrome otomatis
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()  # supaya tampilan penuh

# buka halaman register
driver.get("https://authorized-partner.vercel.app/register")
print("Halaman register berhasil dibuka")

# wait dipakai supaya selenium menunggu elemen muncul dulu
wait = WebDriverWait(driver, 15)

try:
    # STEP 1: klik checkbox persetujuan
    print("Mencari checkbox persetujuan...")
    checkbox = wait.until(EC.presence_of_element_located((By.ID, "remember")))
    time.sleep(1)
    checkbox.click()
    print("Checkbox berhasil diklik")

    # STEP 2: klik tombol Continue
    print("Mencari tombol Continue...")
    continue_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue')]"))
    )
    time.sleep(1)
    continue_btn.click()
    print("Tombol Continue sudah diklik")

    # STEP 3: isi form data diri satu per satu
    print("Mulai mengisi form register...")

    first = wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
    first.send_keys("Tessa")
    time.sleep(1)

    last = wait.until(EC.visibility_of_element_located((By.NAME, "lastName")))
    last.send_keys("Manurung")
    time.sleep(1)

    email = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
    email.send_keys("tessa12234@gmail.com")
    time.sleep(1)

    phone = wait.until(EC.visibility_of_element_located((By.NAME, "phoneNumber")))
    phone.send_keys("0812234546")
    time.sleep(1)

    password = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    password.send_keys("PasswordRahasia1223!")
    time.sleep(1)

    confirm = wait.until(EC.visibility_of_element_located((By.NAME, "confirmPassword")))
    confirm.send_keys("PasswordRahasia1223!")
    time.sleep(1)

    print("Semua field form sudah diisi")

    # STEP 4: klik tombol submit
    submit_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'].primary-btn"))
    )
    time.sleep(1)
    submit_btn.click()
    print("Form sudah disubmit")

    # STEP 5: LOOP UNTUK MULTI-STEP SIGNUP
    time.sleep(2)
    while "register" in driver.current_url:
        try:
            print("Mendeteksi step berikutnya...")

            # jika ada field di step berikutnya, isi di sini
            # contoh:
            # company = wait.until(EC.visibility_of_element_located((By.NAME, "companyName")))
            # company.send_keys("My Company")
            # time.sleep(1)

            # klik tombol Continue / Next
            next_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue')]"))
            )
            time.sleep(1)
            next_btn.click()
            print("Step berikutnya sudah diklik")
            time.sleep(2)

        except Exception:
            print("Tidak ada step berikutnya, signup flow selesai")
            break

    print("Signup flow selesai, URL terakhir:", driver.current_url)

except Exception as e:
    print("Terjadi error saat menjalankan automation:", e)

finally:
    time.sleep(3)
    driver.quit()
    print("Browser ditutup, automation selesai")
