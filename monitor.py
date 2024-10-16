import os
import smtplib
import time
import requests
import hashlib


WAIT_TIME = 43200 #Seconds
SAT_SITE = "https://satsuite.collegeboard.org/sat/dates-deadlines?gclid=Cj0KCQjwgrO4BhC2ARIsAKQ7zUk3yx6vj1qW3-dZa917cD8VbJ-oxeGAc0TwnpXu9DBAz8hpJWoxms8aArKmEALw_wcB&ef_id=Cj0KCQjwgrO4BhC2ARIsAKQ7zUk3yx6vj1qW3-dZa917cD8VbJ-oxeGAc0TwnpXu9DBAz8hpJWoxms8aArKmEALw_wcB:G:s&s_kwcid=AL!4330!3!686853399560!e!!g!!sat%20test%20dates%20and%20locations!20924334928!166035249508&gad_source=1"
EMAIL_ADDRESS = 'satchecker123@gmail.com'
EMAIL_PASSWORD = 'lexl qgfm saze hnpr'

RECIEVER_EMAIL_ADDRESS = 'example@gmail.com'#Put In Your Email

r = requests.get('https://tinyurl.com/3wa6xb82', timeout=5)

#if r.status_code != 200:

def get_website_hash(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        content = response.text
        # Return an MD5 hash of the content
        return hashlib.md5(content.encode('utf-8')).hexdigest()
    except requests.RequestException as e:
        print(f"Error fetching the website: {e}")
        return None

# Function to check for changes
def check_for_changes(url):
    print(f"Checking changes for SAT site")
    initial_hash = get_website_hash(url)
    current_hash = get_website_hash(url)

    # Compare the hashes
    if current_hash != initial_hash:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            subject = 'CHANGES DETECTED'
            body = 'CHECK COLLEGEBOARD NOW TO BOOK SAT: https://tinyurl.com/3wa6xb82'#make it so that the email is more detailed
            msg = f'Subject: {subject}\n\n{body}'
            
            for i in range(15):
                smtp.sendmail(EMAIL_ADDRESS, RECIEVER_EMAIL_ADDRESS, msg)
                time.sleep(1)

    elif current_hash == initial_hash:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            subject = 'No Updates on SAT Site'
            body = "Hello,\n\n" \
                    "We checked the SAT dates and deadlines page, and there have been no updates at this time.\n\n" \
                    "You can check back later for new updates\n\n" \
                    "Best regards,\nSAT Checker"
            #make it so that the email is more detailed
           
            msg = f'Subject: {subject}\n\n{body}'
            
            smtp.sendmail(EMAIL_ADDRESS, RECIEVER_EMAIL_ADDRESS, msg)



while True:
    check_for_changes(SAT_SITE)
    time.sleep(WAIT_TIME)  # Wait before the next cycle


