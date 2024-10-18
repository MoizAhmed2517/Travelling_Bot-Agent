from playwright.sync_api import sync_playwright
import booking.constants as const

class Booking():
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
     
    def open_website(self):
        self.page.goto(const.GOTO_PAGE)
        self.implicity_waiting()
        self.dismiss_popup_if_exists()

    def implicity_waiting(self, by_default=4000):
        self.page.wait_for_timeout(by_default)
    
    def dismiss_popup_if_exists(self):
        try:
            dismiss_button = self.page.locator(
                'button[aria-label="Dismiss sign-in info."]'
            )
            if dismiss_button.is_visible():
                dismiss_button.click()
                print("Popup dismissed.")
        except TimeoutError:
            print("No popup detected.")
        finally:
            self.page.locator("body").click()
    
    def click_locator(self, query, exception="No Exception", timeout=3000):
        try:
            locator = self.page.locator(query)
            locator.wait_for(state="visible", timeout=timeout)
            locator.click()
        except Exception as e:
            print(exception, 
                  e, 
                  e.__traceback__.tb_frame
                )
            
    def multi_click_locator(self, query, exception="No Exception", timeout=3000, index=0):
        try:
            locator = self.page.locator(query)
            locator.wait_for(state="visible", timeout=timeout)
            for _ in range(index):
                locator.click()
        except Exception as e:
            print(exception,
                  e,
                  e.__traceback__.tb_frame
            )
            
    def change_currency(self, currency="USD"):
            self.click_locator(
                query='//*[@id="b2indexPage"]/div[2]/div/div/header/div/nav[1]/div[2]/span[1]/button',
                exception="Error in Picking the currency Header"
            )
            self.implicity_waiting(1000)
            self.click_locator(
               query=f'button[data-testid="selection-item"]:has-text("{currency}") >> nth=0',
               exception="Error in selecting the currency" 
            )
            self.implicity_waiting(2000)
            
    def select_place_togo(self, place):
        search_field = self.page.wait_for_selector('//*[@id=":rh:"]')
        search_field.fill("")
        self.implicity_waiting(1000)
        search_field.type(place)
        self.implicity_waiting(1500)
        self.click_locator(
            query=f'//li[@id="autocomplete-result-0"]',
            exception="Error in selecting the first search result"
        )
        self.implicity_waiting(2000)
    
    def select_dates(self, check_in_date, check_out_date):
        self.click_locator(
            query=f'span[data-date="{check_in_date}"]',
            exception="Error in selecting the check in date"
        )
        self.click_locator(
            query=f'span[data-date="{check_out_date}"]',
            exception="Error in selecting the check out date"
        )
        self.implicity_waiting(2000)
        
    def select_confs(self, adults=1, rooms=1, children=0, **kwargs):
        children_ages = [kwargs.get(f'age_{i + 1}', '0 years old') for i in range(children)]
        self.click_locator(
            query='button[data-testid="occupancy-config"]',
            exception="Error in selecting the occupancy config"
        )
        if children == 0:
            self.multi_click_locator(
                query='//*[@id=":ri:"]/div/div[1]/div[2]/button[2]',
                exception="Error in increasing the number of adults",
                index=adults-2
            )
            self.multi_click_locator(
                query='//*[@id=":ri:"]/div/div[3]/div[2]/button[2]',
                exception="Error in increasing the number of rooms",
                index=rooms-1
            )
        else:
            pass
            self.multi_click_locator(
                query='//*[@id=":ri:"]/div/div[1]/div[2]/button[2]',
                exception="Error in increasing the number of adults",
                index=adults-2
            )
            self.multi_click_locator(
                query='//*[@id=":ri:"]/div/div[2]/div[2]/button[2]',
                exception="Error in increasing the number of children",
                index=children
            )
            for i, age in enumerate(children_ages):
                age_selector = f'xpath=/html/body/div[3]/div[2]/div/form/div/div[3]/div/div/div/div/div[3]/div[{i + 1}]/div/select'
                self.page.locator(age_selector).select_option(label=age)
                self.implicity_waiting(500)
            self.multi_click_locator(
                query='//*[@id=":ri:"]/div/div[5]/div[2]/button[2]',
                exception="Error in increasing the number of rooms",
                index=rooms-1
            )
            
        self.click_locator(
            query=f'button[type="submit"]',
            exception="Error in searching for deals"
        )
        self.implicity_waiting(3000)
        
        
     
        
        