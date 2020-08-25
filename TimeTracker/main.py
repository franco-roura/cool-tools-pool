import argparse

from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from lib import dom_elements
from lib.config import *
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("no-sandbox")
options.add_argument("headless")


def parse_arguments():
    """
    This functions parses the arguments passed through the command line.
    :return: A Namespace object representing the arguments
    :rtype: Namespace
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--description', required=True)
    parser.add_argument('--hours', required=True)
    parser.add_argument('--date', required=False)
    args = parser.parse_args()
    return args


def login(driver):
    """
    This function logs you in.
    :param driver: The RemoteWebDriver object
    :type driver: RemoteWebDriver
    """
    driver.get(Urls.login)
    username_input = driver.find_element_by_css_selector(dom_elements.Login.username)
    username_input.send_keys(Account.username)
    password_input = driver.find_element_by_css_selector(dom_elements.Login.password)
    password_input.send_keys(Account.password)
    login_button = driver.find_element_by_css_selector(dom_elements.Login.button)
    login_button.click()


def track_hour(driver, ticket_description, hours, date=None):
    """
    This function tracks an hour of your time.
    :param driver: The RemoteWebDriver object
    :type driver: RemoteWebDriver
    :param ticket_description: The ticket's description
    :type ticket_description: str
    :param hours: The amount of hours worked on the ticket
    :type hours: str
    :param date: The date if specified, otherwise it defaults as today.
    :type date: A date string in "dd/mm/YYYY" format
    :return:
    """
    driver.get(Urls.track_hours)
    if date:
        date_input = driver.find_element_by_css_selector(dom_elements.TrackHours.date)
        date_input.clear()
        date_input.send_keys(date)
    project = driver.find_element_by_css_selector(dom_elements.TrackHours.project)
    select_project = Select(project)
    select_project.select_by_visible_text(Account.project_name)
    WebDriverWait(driver, 15).until(
        visibility_of_element_located((By.CSS_SELECTOR, dom_elements.TrackHours.software_assignment))
    )
    assignment_type = driver.find_element_by_css_selector(dom_elements.TrackHours.assignment_type)
    select_assignment = Select(assignment_type)
    select_assignment.select_by_visible_text(Account.assignment_type)
    focal_point = driver.find_element_by_css_selector(dom_elements.TrackHours.focal_point)
    select_focal_point = Select(focal_point)
    select_focal_point.select_by_visible_text(Account.client_focal_point)
    hours_input = driver.find_element_by_css_selector(dom_elements.TrackHours.hours)
    hours_input.send_keys(hours)
    description_input = driver.find_element_by_css_selector(dom_elements.TrackHours.description)
    description_input.send_keys(ticket_description)
    accept = driver.find_element_by_css_selector(dom_elements.TrackHours.accept_button)
    accept.click()


def main():
    arguments = parse_arguments()
    driver = webdriver.Chrome(options=options)
    login(driver)
    track_hour(driver, arguments.description, arguments.hours, arguments.date)
    print("Tracked \"%s\" successfully" % arguments.description)
    driver.close()
    print("You can validate your tickets at https://timetracker.bairesdev.com/ListaTimeTracker.aspx")


if __name__ == '__main__':
    main()
