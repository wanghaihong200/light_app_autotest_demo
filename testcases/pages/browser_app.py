"""heytap 浏览器页面实现——真机沉淀的实战示例。

要点：release 浏览器控件 id 全混淆（a91/bjx…）、text 全空，
唯一稳定锚点是 content-desc（= accessibility id），候选链以 acc_id 领衔。
注意：该浏览器未开 WebView 调试（见框架 ADR-0005），css 候选仅适用于
开启了调试的产品线 App；此处页面实现只覆盖原生层。
"""

from laf.core.locator import Locator
from laf.core.page import Page


class BrowserHomePage(Page):
    """浏览器首页（图标+content-desc 形态）。"""

    ready_marker = Locator(acc_id="搜索", desc="搜索/地址栏入口")

    LOCATORS = {
        "addr_bar": Locator(acc_id="搜索", desc="搜索/地址栏入口"),
    }


class ExamplePage(Page):
    """example.com 加载后的页面（需被测包开启 WebView 调试才可用）。"""

    ready_marker = Locator(css="h1", desc="Example Domain 标题")

    LOCATORS = {
        "title": Locator(css="h1", desc="Example Domain 标题"),
    }
