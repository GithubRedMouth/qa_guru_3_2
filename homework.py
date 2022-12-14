from selene.support.shared import browser
from selene import be, have


def test_serh(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in'))


def test_serh_negative(open_browser):
    browser.element('[name="q"]').should(be.blank).type('kduffsvdlnkgushugshndliugerfuisfkjslzdjcnslvj').press_enter()
    browser.element('[id="result-stats"]').should(have.text('About 0 results'))