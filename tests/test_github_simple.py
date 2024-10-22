from selene import browser
from selene import by, be, have


def test_github_simple():
    browser.open('https://github.com')

    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type('denisgaldin/qa_guru_hw10').press_enter()
    browser.element(by.link_text('denisgaldin/qa_guru_hw10')).click()
    browser.element('#issues-tab').click()
    browser.element(by.text('Issue for qa_guru_hw10')).click()

    browser.element('.gh-header-title').should(have.text('Issue for qa_guru_hw10'))
