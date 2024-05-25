from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Replace with the path to your ChromeDriver
driver = webdriver.Chrome("path/to/chromedriver")

driver.get("https://jqueryui.com/droppable/")

# Wait for the page to load completely (adjust wait time if needed)
driver.implicitly_wait(10)

# Locate the draggable element (white rectangle)
draggable = driver.find_element(By.ID, "draggable")

# Locate the droppable element (yellow rectangle)
droppable = driver.find_element(By.ID, "droppable")

# Create an ActionChains object
actions = ActionChains(driver)

# Build the drag and drop action sequence
actions.drag_and_drop(draggable, droppable).perform()

# Optional: Wait for the drop animation to finish (adjust wait time if needed)
driver.implicitly_wait(2)

# Close the browser window
driver.quit()
