import time
import threading
import os
import base64
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from tqdm import tqdm  # Import tqdm for progress bar

# Kill switch flag
stop_script = False

def kill_switch():
    """Listens for user input to stop the script."""
    global stop_script
    input("\nPress Enter to stop the script at any time...\n")
    stop_script = True

# Start the kill switch in a separate thread
threading.Thread(target=kill_switch, daemon=True).start()

# Setup Chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Keeps the browser open

# Automatically install and set up ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

def save_as_pdf(driver, filename):
    """Uses Chrome's DevTools Protocol to print the page with both image & text layers."""
    result = driver.execute_cdp_cmd(
        "Page.printToPDF",
        {
            "landscape": False,
            "displayHeaderFooter": False,
            "printBackground": True,
            "paperWidth": 8.5,
            "paperHeight": 11.0,
            "marginTop": 0.1,
            "marginBottom": 0.1,
            "marginLeft": 0.1,
            "marginRight": 0.1,
            "scale": 0.83,
            "preferCSSPageSize": False,
            "printSelectionOnly": False,
        },
    )
    pdf_data = base64.b64decode(result["data"])
    with open(filename, "wb") as pdf_file:
        pdf_file.write(pdf_data)

try:
    # Ensure "ind_pdfs" folder exists
    os.makedirs("ind_pdfs", exist_ok=True)

    # Open RedShelf page
    driver.get("page_log_in_URLR}")
    time.sleep(35)  # time to log in

    if stop_script:
        driver.quit()
        exit()

    # Redirect to Virdocs book page
    driver.get("book_URL")
    time.sleep(3)

    if stop_script:
        driver.quit()
        exit()

    # Loop through pages 1-x with progress bar
    total_pages = 1000
    with tqdm(total=total_pages, desc="Saving PDFs", unit="page") as pbar:
        for page_num in range(1, total_pages + 1):
            if stop_script:
                break

            page_url = f"page_URL_with_page_num"
            driver.get(page_url)
            time.sleep(0.1)  # Shortened time between page loads

            pdf_path = os.path.join("ind_pdfs", f"page_{page_num}.pdf")
            save_as_pdf(driver, pdf_path)
            print(f"✅ Saved page {page_num} as {pdf_path}")
            pbar.update(1)  # Update progress bar

    print("\n✅ PDFs saved in 'ind_pdfs' folder.")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    driver.quit()
