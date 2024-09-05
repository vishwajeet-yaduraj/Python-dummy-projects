import csv
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# Step 1: Set up Selenium with Edge driver
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

# Step 2: Open the YouTube video
video_url = "https://www.youtube.com/watch?v=kbvHM2S2_bk"
driver.get(video_url)

# Wait for the page to load
time.sleep(5)

# Step 3: Scroll down to load all comments
SCROLL_PAUSE_TIME = 2

# Get initial scroll height
last_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    # Scroll down to the bottom
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

    # Wait for new content to load
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Step 4: Wait until all comments are loaded
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comment-thread-renderer"))
)

# Step 5: Extract comments, replies, and likes
comments_data = []

comment_elements = driver.find_elements(By.CSS_SELECTOR, "ytd-comment-thread-renderer")

for comment_element in comment_elements:
    try:
        # Extract comment text
        comment_text = comment_element.find_element(By.CSS_SELECTOR, "#content-text").text.strip()

        # Extract likes (if available)
        likes = comment_element.find_element(By.CSS_SELECTOR, "#vote-count-middle").text.strip()

        # Extract replies (if available)
        reply_elements = comment_element.find_elements(By.CSS_SELECTOR, "ytd-comment-renderer #content-text")
        replies = [reply.text.strip() for reply in reply_elements]

        comments_data.append({
            "Comment": comment_text,
            "Replies": " | ".join(replies) if replies else "No Replies",
            "Likes": likes if likes else "0"
        })

    except Exception as e:
        print(f"Error processing comment: {e}")

# Step 6: Write to CSV file
csv_file = "youtube_comments.csv"

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["Comment", "Replies", "Likes"])
    writer.writeheader()
    for data in comments_data:
        writer.writerow(data)

# Step 7: Close the browser
driver.quit()

print(f"Comments have been saved to {csv_file}")
