"""设置 App（ColorOS / Android 14）页面实现。定位情报来自 uiautomator dump。"""

from laf.core.locator import Locator
from laf.core.page import Page


class SettingsHomePage(Page):
    """设置首页。"""

    ready_marker = Locator(
        id="com.android.settings:id/recycler_view",
        text="关于本机",
        desc="设置首页列表",
    )

    LOCATORS = {
        "search_box": Locator(
            id="com.android.settings:id/searchView",
            text="搜索设置项",
            desc="设置搜索框",
        ),
        "about_item": Locator(
            text="关于本机",
            xpath='//android.widget.TextView[@text="关于本机"]',
            desc="关于本机条目",
        ),
        # 仅用于验证候选链超时与失败现场包（屏上不存在）
        "ghost_item": Locator(
            text="不存在的菜单项",
            desc="幽灵条目（用于失败验证）",
        ),
    }
