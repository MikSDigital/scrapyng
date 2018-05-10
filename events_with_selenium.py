from selenium import webdriver

def get_upcoming_events(url):
    driver = webdriver.Firefox()

    driver.get(url)

    events = driver.find_elements_by_xpath('//ul[contains(@class, "list-recent-events")]/li')

    for event in events:
        event_details = dict()

        event_details['name'] = event.find_element_by_xpath('h3[@class="event-title"]/a').text
        event_details['location'] = event.find_element_by_xpath('p/span[@class="event-location"]').text
        event_details['time'] = event.find_element_by_xpath('p/time').text
        print(event_details)

    driver.close()

get_upcoming_events('https://www.aliexpress.com/item/best-seller-HDMI-1080P-Matrix-Switcher-40x40-support-DVI-1-0-protocol/32751070654.html')