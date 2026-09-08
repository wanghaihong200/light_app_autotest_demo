"""WebView 链路冒烟：css 候选自动触发 WEBVIEW 上下文切换。

前置条件（ADR-0005）：被测包必须开启 WebView 调试。
heytap 浏览器（release）未开调试 → 默认跳过；换成产品线调试包后移除 skip 即可跑。
"""

import pytest

from pages.browser_app import BrowserHomePage, ExamplePage

pytestmark = [
    pytest.mark.app,
    pytest.mark.real_device,
    pytest.mark.skip(reason="需要开启 WebView 调试的被测包（ADR-0005）；产品线调试包就绪后移除"),
]


def test_webview_context_switch(driver, flow):
    """原生定位 → 导航 → css 定位自动切 WEBVIEW 上下文。"""
    home = flow.page(BrowserHomePage)
    home.wait_ready()                      # acc_id 命中：原生侧
    home.on("addr_bar").tap()
    driver.type_text("example.com")        # 输入到焦点控件
    driver.press_enter()                   # 触发"前往"
    page = flow.page(ExamplePage)
    page.wait_ready(timeout=15)            # css 候选：框架自动切 WEBVIEW
    assert page.on("title").text() == "Example Domain"
