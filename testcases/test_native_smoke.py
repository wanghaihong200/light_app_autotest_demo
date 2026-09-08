"""原生链路冒烟：设置 App。跑法：

    pytest testcases/test_native_smoke.py --laf-app settings --laf-env test
"""

import pytest

from pages.settings_app import SettingsHomePage

pytestmark = [pytest.mark.app, pytest.mark.real_device]


def test_settings_home_ready(driver, flow):
    home = flow.page(SettingsHomePage)
    home.wait_ready()
    assert home.has("search_box"), "设置首页搜索框未出现"


def test_candidate_chain_and_tap(driver, flow):
    home = flow.page(SettingsHomePage)
    home.wait_ready()
    home.scroll_to("about_item").tap()  # 关于本机在列表底部，需滚动查找
    driver.back()


import os

import pytest as _pytest


@_pytest.mark.skipif(
    os.environ.get("LAF_EVIDENCE_DEMO") != "1",
    reason="故意失败用例：LAF_EVIDENCE_DEMO=1 时运行，验证失败现场包",
)
def test_deliberate_failure_for_evidence(driver, flow):
    """运行于 LAF_EVIDENCE_DEMO=1：真实候选链超时 → LocatorError + 现场包。"""
    home = flow.page(SettingsHomePage)
    home.wait_ready()
    home.on("ghost_item")
