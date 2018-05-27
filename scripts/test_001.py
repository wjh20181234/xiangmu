import allure
import pytest

class Test_001():

    @allure.step(title='添加测试标题001')
    @pytest.mark.parametrize('a',[1,2,3])
    def test01(self,a):
        assert a !=2

    @allure.step(title='添加测试标题002')
    @pytest.mark.parametrize('a', [4, 5, 6])
    def test02(self, a):
        assert a != 2