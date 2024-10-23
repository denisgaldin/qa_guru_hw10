import allure
from allure_commons.types import Severity
from model.IssuePage import IssuePage


@allure.tag("Github")
@allure.severity(Severity.CRITICAL)
@allure.label("Denis", "Galdin")
@allure.feature("Задачи в репозитории")
@allure.story("Название репозитория содержит правильный заголовок")
@allure.link("https://github.com", name="Testing")
@allure.title('Тест Github steps')
def test_github_steps():
    issue = IssuePage()
    issue.open_page('https://github.com')
    issue.go_to_repo('eroshenkoam/allure-example')
    issue.go_to_issue('Issue for HW qa.guru')
    issue.assert_tittle_text('Issue for HW qa.guru')
