# import module
import smtplib
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
  
# Create the webdriver object. Here the 
# chromedriver is present in the driver 
# folder of the root directory.  
# get https://www.geeksforgeeks.org/
Detect = True 
while(True) : 
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
    password_field.send_keys("put-password-here")  # Fill the password input field
    buttons[3].click()

    driver.get("https://logement.cesal-residentiel.fr/espace-resident/cesal_mon_logement_reservation.php")
    driver.maximize_window()
    time.sleep(1)

    buttons = driver.find_elements_by_tag_name("button")

    date_arrivee_span = driver.find_element_by_id("select2-date_arrivee-container")
    date_arrivee_span.click()  # Click on the span to open the dropdown

    # Find the desired date option in the dropdown and click on it
    #desired_date_option = driver.find_element_by_xpath("//li[contains(text(), '07/07/2023')]")
    desired_date_option = driver.find_element_by_xpath("//ul[@id='select2-date_arrivee-results']/li[last()]")
    desired_date_option.click()

    # Find the date sortie input field by its ID
    date_sortie_input = driver.find_element_by_id("date_sortie")
    date_sortie_input.clear()  # Clear the input field (optional)
    date_sortie_input.send_keys("30/05/2024")  # Fill the date sortie input field

    buttons[4].click()
    time.sleep(1)
    body = ""
    recipient_email = "zern74523@gmail.com"
    mail_password = "pwd"
    mail_user = "mohsine.zireg@student-cs.fr"
    for k in range(1, 5):
        element_id = f"residence_{k}_logements_disponibles"
        element = driver.find_element_by_id(element_id)
        text = element.text
        
        if text != "Aucun logement disponible":
            message = f"Yes Dispo Residence {k}!! \n"
            #print(f"Yaay Residence {k} disponible !!")
        else : 
            message = f"No Dispo Residence {k} !!\n"
            #print(f"Nooo Residence {k} indisponible !!")
            
            # Sending email
        subject = "Logement"
        body += message
        #print(body)

    email_text = f"Subject: {subject}\n\n{body}"

    if "Yes" in body:
        try:
            server = smtplib.SMTP("smtp.office365.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_password)
            server.sendmail(gmail_user, recipient_email, email_text)
            server.close()
            print("Email sent successfully!")
            break
        except Exception as e:
            print("Failed to send email.")
            print(e)
    time.sleep(300)
        





    #buttons = driver.find_elements_by_tag_name("button")
    #buttons[4].click()
    # Obtain button by link text and click.
    #button = driver.find_element_by_link_text(buttons[0].text)
    #button.click()
