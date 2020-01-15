#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lixiaofeng
# @Site    :
# @File    : base_page.py
# @Software: PyCharm
import os
import time
from PIL import Image
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  # web
from appium.webdriver.common.touch_action import TouchAction  # app
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from Product.models import Element
import logging

log = logging.getLogger('log')  # 初始化log


class PageObject:
    """基于原生的selenium框架做二次封装"""
    timeout = 10  # 显示等待超时时间
    t = 1
    driver = None

    def open(self, url, title=""):
        """get url，最大化浏览器，判断title"""
        self.driver.set_page_load_timeout(self.timeout)  # 页面加载等待
        try:
            self.driver.get(url)
        except TimeoutException as e:
            log.error("打开 {} 页面加载超时！{}".format(url, e))
            self.driver.execute_script("window.stop()")
            raise TimeoutException("打开 {} 页面加载超时！{}".format(url, e))
        if title != "":
            try:
                WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
                log.info("打开网页成功！")
            except TimeoutException as e:
                log.error("打开网页 {} 判断 title 出现错误！ {}".format(url, e))
                raise TimeoutException("打开网页 {} 判断 title 出现错误！ {}".format(url, e))
            except Exception as msg:
                log.error("打开网页产生的其他错误：{}".format(msg))
                raise Exception("打开网页产生的其他错误：{}".format(msg))

    def maximize_window(self):
        """最大化浏览器"""
        self.driver.maximize_window()

    def sleep(self, seconds):
        """强制等待"""
        log.info("强制等待：{} 秒.".format(seconds))
        if str(seconds).isdigit():
            time.sleep(int(seconds))
        else:
            time.sleep(0.5)

    def wait(self, seconds):
        """隐式等待"""
        if not str(seconds).isdigit():
            return
        log.info("隐式等待：{} 秒.".format(seconds))
        self.driver.implicitly_wait(int(seconds))

    def find_element(self, driver, locator, more=False):
        """定位元素方法"""
        if locator is None:
            return
        if isinstance(locator, dict):
            locator = (locator.get("by", None), locator.get("locator", None))
            message = locator
        elif isinstance(locator, list) and len(locator) > 2:
            locator = (locator[0], locator[1])
            message = locator
        elif isinstance(locator, Element):
            message = locator.name
            locator = (locator.by, locator.locator)
        elif isinstance(locator, str):
            locator = tuple(locator.split(".", 1))
            message = locator
        else:
            log.error("element参数类型错误: type:" + str(type(locator)))
            raise TypeError("element参数类型错误: type:" + str(type(locator)))
        try:
            try:
                if more:
                    return WebDriverWait(driver, self.timeout).until(EC.visibility_of_all_elements_located(locator))
                else:
                    return WebDriverWait(driver, self.timeout).until(EC.visibility_of_element_located(locator))
            except:
                if more:
                    return WebDriverWait(driver, self.timeout).until(EC.presence_of_all_elements_located(locator))
                else:
                    return WebDriverWait(driver, self.timeout).until(EC.presence_of_element_located(locator))
        except Exception:
            log.error("页面中未能找到元素：{}".format(message))
            raise NoSuchElementException("找不到元素:" + str(message))

    def handle_exception(self, locator):
        """自定义异常处理"""
        self.driver.implicitly_wait(0)  # 隐式等待
        page_source = self.driver.page_source
        if "image_cancel" in page_source:
            self.click(locator)
        elif "tips" in page_source:
            pass
        self.driver.implicitly_wait(10)  # 隐式等待

    def clicks(self, locator, n):
        """点击一组元素中的几个"""
        if not str(n).isdigit():
            return
        log.info("点击一组元素 {} 中的 {} 个.".format(locator, n))
        element = self.find_element(self.driver, locator, more=True)[int(n)]
        element.click()

    def click(self, locator):
        """点击操作"""
        log.info("点击元素：{}".format(locator))
        element = self.find_element(self.driver, locator)
        element.click()

    def click_text(self, locator, text, n=""):
        """点击指定文本元素"""
        log.info("点击指定文本 {} 的元素 {}".format(text, locator))
        if n == "":
            if self.get_text(locator) == text:
                self.click(locator)
        elif str(n).isdigit():
            if self.get_texts(locator, n) == text:
                self.clicks(locator, n)
        else:
            elements = self.find_element(self.driver, locator, more=True)
            for element in elements:
                if element.text.strip() == text:
                    element.click()

    def double_click(self, locator):
        """双击操作"""
        element = self.find_element(self.driver, locator)
        ActionChains(self.driver).double_click(element).perform()

    def send_keys(self, locator, text):
        """发送文本，清空后输入"""
        log.info("输入框元素 {} 输入文本 {}".format(locator, text))
        element = self.find_element(self.driver, locator)
        element.clear()
        element.send_keys(text)

    def sends_keys(self, locator, text, n):
        """选中一组元素中的一个，发送文本，清空后输入"""
        if not str(n).isdigit():
            return
        log.info("选中一组元素 {} 中的 {} 个，发送文本 {}，清空后输入.".format(locator, text, n))
        element = self.find_element(self.driver, locator, more=True)[int(n)]
        element.clear()
        element.send_keys(text)

    # ================================================App===============================================================

    def click_coordinate(self, coordinate, timeout=10):
        """点击坐标"""
        self.driver.tap(coordinate, timeout)

    def long_press(self, element):
        """长按"""
        return TouchAction(self.driver).long_press(element).perform()

    def unknown_drag_and_drop(self, element_obj, element):
        """长按后才能发现另一个元素的 拖放"""
        element_obj.move_to(element).wait(1000).release().perform()

    def drag_and_drop(self, element, element1):
        """能同时发现两个元素的 拖放"""
        element_obj = self.long_press(element)
        element_obj.move_to(element1).wait(1000).release().perform()

    def switch_context(self, i):
        """切换上下文"""
        context = self.driver.contexts
        if isinstance(context, list) and str(i).isdigit():
            self.driver.switch_to.context(context[int(i)])

    def swipeDown(self, t=500, n=1):
        """向下滑动屏幕"""
        time.sleep(2)
        l = self.driver.get_window_size()
        x1 = l["width"] * 0.5  # x坐标
        y1 = l["height"] * 0.25  # 起始y坐标
        y2 = l["height"] * 0.85  # 终点y坐标
        for i in range(n):
            time.sleep(0.5)
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipeUp(self, t=500, n=1):
        """向上滑动屏幕"""
        time.sleep(2)
        l = self.driver.get_window_size()
        x1 = l["width"] * 0.5  # x坐标
        y1 = l["height"] * 0.65  # 起始y坐标
        y2 = l["height"] * 0.25  # 终点y坐标
        for i in range(n):
            time.sleep(0.5)
            self.driver.swipe(x1, y1, x1, y2, t)

    # ================================================Web===============================================================

    def send_keys_enter(self):
        """敲enter"""
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def send_keys_down(self):
        """敲向下键"""
        ActionChains(self.driver).send_keys(Keys.DOWN).perform()

    def send_keys_arrow_down(self):
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()

    def send_keys_arrow_right(self):
        ActionChains(self.driver).send_keys(Keys.ARROW_RIGHT).perform()

    def is_text_in_element(self, locator, text):
        """判断文本在元素里，没定位到元素返回False，定位到返回判断结果布尔值"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element(locator, text))
            log.info("is_text_in_element     成功")
            return result
        except TimeoutException:
            log.error(" {} 元素没有定位到".format(locator))
            raise NoSuchElementException(" {} 元素没有定位到".format(locator))

    def is_text_in_value(self, locator, value):
        """判断元素的value值，没有定位到返回False，定位到返回判断结果布尔值"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element_value(locator, value))
        except TimeoutException:
            log.error("元素的value值没有定位到：{}".format(locator))
            raise NoSuchElementException("{} 元素的value值没有定位到".format(locator))
        else:
            return result

    def is_title(self, title):
        """判断title完全等于"""
        result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title))
        return result

    def is_title_contains(self, title):
        """判断title包含"""
        result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
        return result

    def is_selected(self, locator):
        """判断元素被选中，返回布尔值， 一般用在下拉框"""
        result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.element_located_to_be_selected(locator))
        return result

    def is_selected_be(self, locator, selected=True):
        """判断元素的状态，selected是期望的参数True/False，返回布尔值"""
        result = WebDriverWait(self.driver, self.timeout, self.t).until(
            EC.element_located_selection_state_to_be(locator, selected))
        return result

    def is_alert_present(self):
        """判断页面是否有alert，有返回alert，没有返回False"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until((EC.alert_is_present()))
            return result
        except TimeoutException:
            return False

    def alert_operations(self, opera=0, text=""):
        """确认alert存在后，可以进行的操作"""
        if not str(opera).isdigit():
            return
        alert = EC.alert_is_present()(self.driver)
        if alert:
            log.info("alert弹框显示文本是：{}".format(alert.text))
            if int(opera) == 0:
                log.info("点击确认按钮中...")
                alert.accept()
            elif int(opera) == 1:
                log.info("点击取消按钮中...")
                alert.dismiss()
            elif int(opera) == 2:
                log.info("输入文本并点击确认按钮中...")
                alert.send_keys(text)
                alert.accept()
            elif int(opera) == 3:
                log.info("输入文本并点击取消按钮中...")
                alert.send_keys(text)
                alert.dismiss()
            else:
                log.warning("参数输入有误，请核实后再进行的操作！")
        else:
            log.warning("没有发现alert弹框。")

    def is_visibility(self, locator):
        """元素可见返回本身，不可见返回False"""
        result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.visibility_of_element_located(locator))
        return result

    def is_invisibility(self, locator):
        """元素可见返回本身，不可见返回True，没有找到元素也返回True"""
        result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.invisibility_of_element_located(locator))
        return result

    def is_clickAble(self, locator):
        """元素可以点击返回本身，不可点击返回False"""
        result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.element_to_be_clickable(locator))
        return result

    def is_locator(self, locator):
        """判断元素有没有被定位到（并不意味着可见），定位到返回element，没有定位到返回False"""
        result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
        return result

    def move_to_element(self, locator):
        """鼠标悬停操作"""
        element = self.find_element(self.driver, locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def move(self, locator, locator1):
        """循环调用鼠标事件，死循环"""
        self.move_to_element(locator)
        time.sleep(2)
        element = self.find_element(self.driver, locator1)
        self.move_to_element(locator1)
        try:
            if element.is_displayed:
                self.click(locator1)
            else:
                self.move(locator, locator1)
        except ElementNotVisibleException as e:
            log.error("鼠标点击事件失败：{}".format(e))
            raise ElementNotVisibleException("鼠标点击事件失败：{}".format(e))

    def switch_frame(self, frame):
        """判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False
            frame：元素定位的元组
        """
        try:
            iframe = self.find_element(self.driver, frame)
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.frame_to_be_available_and_switch_to_it(iframe))
            if result:
                log.info("切换iframe成功！")
            else:
                log.warning("iframe 切换失败！")
                raise NoSuchFrameException("frame 切换失败！")
        except TimeoutException:
            log.warning("没有发现iframe元素：{}".format(frame))
            raise TimeoutException("没有发现iframe元素：{}".format(frame))

    def default_content(self):
        "跳出frame到默认<跳到最外层>"
        self.driver.switch_to.default_content()

    def parent_frame(self):
        """跳出frame到父frame"""
        self.driver.switch_to.parent_frame()

    def current_window_handle(self):
        """当前浏览器handle"""
        return self.driver.current_window_handle

    def switch_window_handle(self, n):
        """切换handle"""
        if not str(n).isdigit():
            self.driver.switch_to.window(n)
        else:
            all_handle = self.driver.window_handles
            log.info("打开的所有handle: {}".format(all_handle))
            self.driver.switch_to.window(all_handle[int(n)])

    def back(self):
        """返回之前的网页"""
        self.driver.back()

    def forward(self):
        """前往下一个网页"""
        self.driver.forward()

    def close(self):
        """关闭当前网页"""
        self.driver.close()

    def quit(self):
        """关闭所有网页"""
        self.driver.quit()

    def get_title(self):
        """获取title"""
        return self.driver.title

    def get_texts(self, locator, n):
        """获取一组相同元素中的指定文本"""
        if not str(n).isdigit():
            return
        element = self.find_element(self.driver, locator, more=True)[int(n)]
        return element.text.strip()

    def get_text(self, locator, make=None):
        """获取文本"""
        element = self.find_element(self.driver, locator)
        return element.text.strip()

    def get_attribute(self, locator, name):
        """获取属性"""
        if name is None:
            name = ""
        element = self.find_element(self.driver, locator)
        return element.get_attribute(name)

    def js_execute(self, js):
        """执行js"""
        return self.driver.execute_script(js)

    def js_focus_element(self, locator):
        """聚焦元素"""
        target = self.find_element(self.driver, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        """滚动到顶部"""
        js = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)

    def js_scroll_bottom(self):
        """滚动到底部"""
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)

    def select_by_index(self, locator, index):
        """通过索引，index是第几个，从0开始, 下拉框"""
        element = self.find_element(self.driver, locator)
        if str(index).isdigit():
            Select(element).select_by_index(int(index))

    def select_by_value(self, locator, value):
        """通过value属性"""
        element = self.find_element(self.driver, locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        """通过text属性"""
        element = self.find_element(self.driver, locator)
        Select(element).select_by_visible_text(text)

    def save_screenshot(self, img_path):
        """获取电脑屏幕截屏"""
        self.driver.save_screenshot(img_path)

    def save_report_html(self):
        """可以在html报告中使用的截图"""
        self.driver.get_screenshot_as_base64()

    def save_element_img(self, locator, img_path):
        """获取元素截图"""
        self.driver.save_screenshot(img_path)
        element = self.find_element(self.driver, locator)
        left = element.location["x"]
        top = element.location["y"]
        right = element.location["x"] + element.size["width"]
        bottom = element.location["y"] + element.size["height"]
        im = Image.open(img_path)
        im = im.crop((left, top, right, bottom))
        im.save(img_path)

    def get_cookies(self):
        """获取cookies"""
        return self.driver.get_cookies()
