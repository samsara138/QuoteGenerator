from time import sleep
from SeleniumBrowser import SeleniumBrowser
import csv
import threading

debug = True
log = lambda x : print(x) if debug else None

def generate_quotes(quote, author):
    website = "https://quotescover.com/"
    browser = SeleniumBrowser(website, headless=False)
    error = False
    try:
        log("********************************************")
        log("Browser init finish, going to website ...")

        main_quote_input_field = browser.get_element_by_id("quotes")
        author_quote_input_field = browser.get_element_by_id("author")
        make_quote_btn = browser.get_element_by_id("template-contactform-submit")

        browser.fill_input(main_quote_input_field, quote)
        browser.fill_input(author_quote_input_field, author)
        browser.click_button(make_quote_btn)

        log("Generating quote")
        start_download_xpath = "/html/body/div[3]/div[2]/div/header/div[2]/div[2]/div/div[2]/button"
        start_download_btn = browser.get_element_by_xpath(start_download_xpath, timeout=10000)
        browser.click_button(start_download_btn)

        log("Waiting the 20 seconds")
        sleep(22)

        log("Choose png")
        png_btn_xpath = "/html/body/div[18]/div[1]/div/div/div/div/button[1]"
        png_btn = browser.get_element_by_xpath(png_btn_xpath, timeout=2000)
        browser.click_button(png_btn)

        log("Start downloading")
        save_png_xpath = "/html/body/div[21]/div[1]/div/div/div[1]/div[4]/button[1]"
        save_png_btn = browser.get_element_by_xpath(save_png_xpath, timeout=2000)
        browser.click_button(save_png_btn)
        sleep(5)

    except Exception as e:
        error = True
        print(e)
    finally:
        browser.close()
        log("********************************************\n")
    return error

def read_csv():
    with open('quotes.csv', newline='', encoding='utf-8') as f:
        return list(csv.reader(f))[1:]  # Read all rows and skip the header


def main():
    quotes = read_csv()
    threads = [threading.Thread(target=generate_quotes, args=(quote[0], quote[1])) for quote in quotes]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    print("Download complete")


if __name__ == '__main__':
    main()
