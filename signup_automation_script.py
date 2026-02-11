from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Tambahkan timeout load halaman
driver.set_page_load_timeout(120)

# Buka website
driver.get("https://authorized-partner.vercel.app/register")
wait = WebDriverWait(driver, 10)
print("Website opened successfully!")

# Klik checkbox
checkbox = wait.until(EC.element_to_be_clickable((By.ID, "remember")))
checkbox.click()
print("Checkbox clicked")

# Klik tombol Continue
continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue')]")))
continue_button.click()
print("Continue button clicked")

# Isi First Name
first_name = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
first_name.send_keys("Tessaa")
print("First Name filled")

# Isi Last Name
last_name = wait.until(EC.presence_of_element_located((By.NAME, "lastName")))
last_name.send_keys("mnrga")
print("Last Name filled")

# Isi Email
email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
email_input.send_keys("Tessa12234@gmail.id")
print("Email filled")

# Isi Phone (gunakan JavaScript agar tidak error ElementNotInteractable)
phone_input = wait.until(EC.presence_of_element_located((By.NAME, "phoneNumber")))
driver.execute_script("arguments[0].value='812234546';", phone_input)
print("Phone filled")

# 🔹 Isi Password
password_input = wait.until(
    EC.presence_of_element_located((By.NAME, "password"))
)
password_input.send_keys("PasswordRahasia1223!")  # ganti sesuai password yang ingin diuji

print("Password filled")

# 🔹 Isi Confirm Password
confirm_password_input = wait.until(
    EC.presence_of_element_located((By.NAME, "confirmPassword"))
)
confirm_password_input.send_keys("PasswordRahasia1223!")  # pastikan sama dengan password
print("Confirm Password filled!")


print("Form submitted")

next_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'].primary-btn"))
)
next_button.click()
print("Next button clicked")



# Tunggu 5 detik untuk verifikasi
time.sleep(5)

# Tutup browser
driver.quit()
print("Script completed successfully!")
