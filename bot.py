from driver import get_driver
from fake_account_generator import new_account
import os


class BOT():
    def __init__(self):
        self.account_info = None
        self.user_name = None
        self.password = None
        self.email = None
        self.fullname = None
        self.driver = None

    def new_account(self):
        self.account_info = new_account()
        self.user_name = self.account_info['username']
        self.password = self.account_info['password']
        self.email = self.account_info['email']
        self.fullname = self.account_info['name']
        if self.driver is not None:
            self.driver.quit() 
        self.driver = get_chrome_driver()
    
    def signup(self):
        url = 'https://instagram.com/accounts/emailsignup/'
        self.driver.get(url)
        while True:
            try:
                
                email_field = self.driver.find_element_by_name('emailOrPhone')

                fullname_field = self.driver.find_element_by_name('fullName')

                username_field = self.driver.find_element_by_name('username')

                password_field = self.driver.find_element_by_name('password')

                email_field.send_keys(self.email)
                time.sleep(1)
                fullname_field.send_keys(self.fullname)
                time.sleep(1)
                username_field.send_keys(self.user_name)
                time.sleep(1)
                password_field.send_keys(self.password)
                time.sleep(1)
                submit = None
                try:
                    submit = self.driver.find_element_by_xpath("//button[text()='Sign up']")
                except:
                    pass
                try:
                    submit = self.driver.find_element_by_xpath("//button[@type='submit']")
                except:
                    pass
                submit.click()
                time.sleep(5)
                break
            except Exception as e:
                pass
        try:
            banned = self.driver.find_element_by_xpath("//p[text()='Sorry, something went wrong creating your account. Please try again soon.']")
            print("[***] Sorry, something went wrong creating your account")
            return False
        except Exception as e:
            print("[!!] Oopes ! Insta Detect me !")
        try:
            notif=driver.find_element_by_xpath("//p[@class='Ma93n']")
            print(notif.text())
        except:
            pass
        try:
            under = self.driver.find_element_by_xpath("//input[@value='under_18']")
            older = self.driver.find_element_by_xpath("//input[@value='above_18']")
            next_btn = self.driver.find_elements_by_xpath("//button[@type='button']")[-1]
            under.click()
            next_btn.click()
            time.sleep(1.5)
        except Exception as e:
            print(e)
        try:
            btn = self.driver.find_elements_by_xpath("//button[@type='button']")[-1]
            btn.click()
            time.sleep(5)
        except:
            pass
        try:
            banned = self.driver.find_element_by_xpath("//p[text()='Sorry, something went wrong creating your account. Please try again soon.']")
            return False
        except Exception as e:
            pass

        return True

    def save_account_to_file(self):
        try:
            with open(users_file,'r') as f:
                f.close()
        except:
            with open(users_file,'w') as f:
                f.close()
        with open(users_file,'a') as f:        
            one_line = self.user_name+","+self.password+"\n"
            f.write(one_line)
            f.close()
        print("[*] Writing to File is Done !")

    def display_success(self):
        self.save_account_to_file()
        print("\n[**] ---- account created Successfully ---- ")
        print("[*] Username = {}".format(self.user_name))
        print("[*] password = {}".format(self.password))
        print("[*] email = {}".format(self.email))
        print("[*] full name = {}".format(self.fullname))
        print("\n")


if __name__ == "__main__":
    bot = BOT()
    # res = False
    # while not bool(res):
    bot.new_account()
    res = bot.signup()
    if res:
        bot.display_success()
    




