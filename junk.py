# Failed Login Code
def type(str, path):
    for char in str:
        time.sleep(random.randint(25, 75) / 100)
        path.send_keys(char)

def login():
    driver.get("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")
    time.sleep(4)
    type(os.getenv('email'), driver.find_element_by_id("identifierId"))

    time.sleep(2)
    driver.find_element_by_id("identifierNext").click()

    time.sleep(5)
    type(os.getenv('password'), driver.find_element_by_name("//input[@name='password']"))
    time.sleep(2)

    element = driver.find_element_by_id('passwordNext')
    driver.execute_script("arguments[0].click();", element)

    time.sleep(5)

# Failed Schedule Code

def handler(name):
    meet = ''
    for json in classes:
        if(json['name'] == name):
            meet = json['meet']

    def h():
        join(meet)

    return h

for json in classes:
    schedule.every().day.at(json['time']).do(handler(json['name']))

while True:
    schedule.run_pending()
    time.sleep(5)