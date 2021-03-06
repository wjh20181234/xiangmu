import allure
import pytest

class Test_001():
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title='添加测试标题001')
    @pytest.mark.parametrize('a',[1,2,3])
    def test01(self,a):
        allure.attach('描述','我是01的描述信息')
        assert a !=2

    @allure.step(title='添加测试标题002')
    @pytest.mark.parametrize('a', [4, 5, 6])
    def test02(self, a):
        allure.attach('描述','我是02的描述信息')
        assert a != 2