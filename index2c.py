# import module
from selenium import webdriver
import time
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=chrome_options)
  
# Create the webdriver object. Here the 
# chromedriver is present in the driver 
# folder of the root directory.  
# get https://www.geeksforgeeks.org/
driver.get("https://logement.cesal-residentiel.fr/espace-resident/cesal_login.php")
  
# Maximize the window and let code stall 
# for 10s to properly maximise the window.
#driver.maximize_window()
time.sleep(1)

buttons = driver.find_elements_by_tag_name("button")
buttons[1].click()
time.sleep(1)

buttons = driver.find_elements_by_tag_name("button")
email_field = driver.find_element_by_id("login-email")
email_field.clear()  # Clear the input field (optional)
email_field.send_keys("mohsine.zireg@student-cs.fr")  # Fill the email input field

# Find the password input field by its ID
password_field = driver.find_element_by_id("login-password")
password_field.clear()  # Clear the input field (optional)
password_field.send_keys("")  # Fill the password input field
buttons[3].click()

driver.get("https://logement.cesal-residentiel.fr/espace-resident/cesal_mon_logement_reservation.php")
driver.maximize_window()
time.sleep(1)

buttons = driver.find_elements_by_tag_name("button")

date_arrivee_span = driver.find_element_by_id("select2-date_arrivee-container")
date_arrivee_span.click()  # Click on the span to open the dropdown

# Find the desired date option in the dropdown and click on it
desired_date_option = driver.find_element_by_xpath("//li[contains(text(), '07/07/2023')]")
desired_date_option.click()

# Find the date sortie input field by its ID
date_sortie_input = driver.find_element_by_id("date_sortie")
date_sortie_input.clear()  # Clear the input field (optional)
date_sortie_input.send_keys("30/05/2024")  # Fill the date sortie input field

buttons[4].click()
time.sleep(1)

for k in range(1, 5):
    element_id = f"residence_{k}_logements_disponibles"
    element = driver.find_element_by_id(element_id)
    text = element.text
    
    if text == "Aucun logement disponible":
        print(f"Residence {k} disponible !!")




#buttons = driver.find_elements_by_tag_name("button")
#buttons[4].click()
# Obtain button by link text and click.
#button = driver.find_element_by_link_text(buttons[0].text)
#button.click()
