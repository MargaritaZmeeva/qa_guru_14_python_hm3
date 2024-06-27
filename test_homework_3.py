from selene import browser, have


def test_positive():
    browser.open('')
    browser.element('[name="q"]').type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative():
    browser.open('')
    browser.element('[name="q"]').type('rfrefervrfrefervrfrefervrfrefervrfrefervrfrefervrfrefervrfrefervrfrefervrfrefervrfrefervrfreferv').press_enter()
    browser.element('.card-section').should(have.text('По запросу rfrefervrfrefervrfrefervrfrefervrfrefervrfrefervrfrefervrfrefervrfrefervrfrefervrfrefervrfreferv ничего не найдено.'))