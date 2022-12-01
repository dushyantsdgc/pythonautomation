Feature: Test Home Page
    This is to test home page

    Scenario: Validate Home page UI
        Given driver 'http://saviconsultancy.com/'
        When click("//a[normalize-space()='Get Started']")
        Then match driver.title == 'SAVI Consultancy'