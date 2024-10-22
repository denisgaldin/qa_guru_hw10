import allure
from allure_commons.types import Severity
from model.issues_page import Issue_page


@allure.tag("Github")
@allure.severity(Severity.CRITICAL)
@allure.label("Denis", "Galdin")
@allure.feature("Задачи в репозитории")
@allure.story("Название репозитория содержит правильный заголовог")
@allure.link("https://github.com", name="Testing")
@allure.title('Тест Github steps')
def test_github_steps():
    issue = Issue_page()
    issue.open_page('https://github.com')
    issue.go_to_repo('denisgaldin/qa_guru_hw10')
    issue.go_to_issue('Issue for qa_guru_hw10')
    issue.assert_tittle_text('Issue for qa_guru_hw10')
