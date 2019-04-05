test fixture
    表示执行一个或多个测试所需的准备、以及任何关联清理操作。
     例如：创建临时或代理数据库、目录或启动服务器进程。

test case
    测试用例是单独的测试单元。 它检查对特定输入集的特定响应。
    unittest提供了一个基类TestCase，可用于创建新的测试用例。

test suite
    它用于聚合应该一起执行的测试
    测试用例集合、测试套件集合、两者组合集合

test runner
    是协调测试执行并向用户提供结果的组件。
    可以使用图形界面、文本界面、或返回特殊值来指示执行测试的结果。

tip: doctest、Nose、pytest是另一种风格的测试、暂时不研究
        第三方单元测试框架，具有较轻的语法，用于编写测试。 例如，assert func（10）== 42。
        众多测试工具：https://wiki.python.org/moin/PythonTestingToolsTaxonomy

Python源代码发行版中的脚本Tools / unittestgui / unittestgui.py是用于测试发现和执行的GUI工具。
对于生产环境，建议测试由Buildbot，Jenkins或Hudson等持续集成系统驱动。


import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()


======
1.通过继承unittest.TestCase创建一个测试用例。使用名称以字母test开头的方法定义n个单独的测试。此命名约定通知测试运行器哪些方法代表测试。
2.每个测试的关键是调用assertEqual()来检查预期结果;
    assertTrue()或assertFalse()来验证条件;
    或assertRaises()以验证是否引发了特定异常。
    使用这些方法代替assert语句，以便测试运行器可以累积所有测试结果并生成报告。
3.setUp()和tearDown()方法允许您定义将在每个测试方法之前和之后执行的指令。
    unittest.main()为测试脚本提供命令行界面.






    单元测试的基本构建块是测试用例 - 必须设置并检查正确性的单个方案。
    在unittest中，测试用例由unittest.TestCase实例表示。
    要创建自己的测试用例，必须编写TestCase的子类或使用FunctionTestCase。

    TestCase实例的测试代码应完全自包含，以便可以单独运行，也可以与任意数量的其他测试用例任意组合运行。
    最简单的TestCase子类将简单地实现一个测试方法（即名称以test开头的方法），以便执行特定的测试代码：

    如果setUp()成功，则无论测试方法是否成功，都将运行tearDown()。

    测试套件，由unittest的TestSuite类表示。
    调用unittest.main() 收集所有模块的测试用例并执行它们。

    如果您想自定义测试套件的构建，您可以自己完成：
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(WidgetTestCase('test_default_widget_size'))
        suite.addTest(WidgetTestCase('test_widget_resize'))
        return suite

    if __name__ == '__main__':
        runner = unittest.TextTestRunner()
        runner.run(suite())


    跳过测试和预期的失败
    Unittest支持跳过单个测试方法甚至整个测试类。
    跳过测试只是使用skip()装饰器或其条件变体之一。
     @unittest.skip(reason)
     @unittest.skipIf(condition, reason)
     @unittest.skipUnless(condition, reason)
     @unittest.expectedFailure          # 预期的失败使用expectedFailure()装饰器

     使用子测试区分测试迭代
     当测试之间存在非常小的差异时，例如某些参数，unittest允许您使用subTest()上下文管理器在测试方法的主体内区分它们。

     class NumbersTest(unittest.TestCase):
        def test_even(self):
            """
            Test that numbers between 0 and 5 are all even.
            """
            for i in range(0, 6):
                with self.subTest(i=i):
                    self.assertEqual(i % 2, 0)

    如果不使用子测试，执行将在第一次失败后停止，并且错误将不太容易诊断，因为i的值不会显示：







#
