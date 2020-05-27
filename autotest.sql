SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

INSERT INTO `auth_user` VALUES (1, 'pbkdf2_sha256$120000$UvFFGKczofz7$9747Yc/FusMaedOgszn8VpXs6ke/I+k5vqfM7olUJsE=', '2019-12-30 21:53:29', 1, 'lixiaofeng', '', '', '18701137212@163.com', 1, 1, '2019-12-30 21:53:06');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NULL DEFAULT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('zu8b0gm8biufrl4i2hfakx1i0z2pyepi', 'OGNiZTczNGIxNTViMGM3Y2IzNzkzMTViZGRjMmUzMTc0ODc4MDViYjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2YzI0YTNiMjkxOWZjOTE5ZGYzMWNmZTI0YmZjNmY4MzNmMzc4ZTk2IiwidXNlciI6ImxpeGlhb2ZlbmcifQ==', '2020-1-13 21:53:29');


-- ----------------------------
-- Table structure for Browser
-- ----------------------------
DROP TABLE IF EXISTS `Browser`;
CREATE TABLE `Browser`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `value` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `remark` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `status` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `installPath` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `driverPath` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of Browser
-- ----------------------------
INSERT INTO `Browser` VALUES (1, 'chrome', 'chrome', NULL, 0,NULL, NULL);
INSERT INTO `Browser` VALUES (2, 'firefox', 'firefox', NULL,0, NULL, NULL);
INSERT INTO `Browser` VALUES (3, 'app', 'android', NULL, NULL,1, NULL);
INSERT INTO `Browser` VALUES (4, '手机浏览器', 'html', NULL, 1,NULL, NULL);
INSERT INTO `Browser` VALUES (5, '模拟器', 'simulator', NULL, 1,NULL, NULL);
INSERT INTO `Browser` VALUES (6, 'chrome-no-web', 'chrome-no-web', NULL,0, NULL, NULL);
-- ----------------------------
-- Table structure for project
-- ----------------------------
DROP TABLE IF EXISTS `project`;
CREATE TABLE `project`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `remark` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `creator` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `createTime` datetime(6) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of project
-- ----------------------------
INSERT INTO `project` VALUES (1, '百度测试项目', '', 'lixiaofeng', '2019-12-30 22:06:19');
INSERT INTO `project` VALUES (2, '雪球app', '', 'lixiaofeng', '2019-12-30 22:28:11');
INSERT INTO `project` VALUES (3, 'backlight项目', '', 'lixiaofeng', '2019-12-30 22:45:59');


-- ----------------------------
-- Table structure for Environment
-- ----------------------------
DROP TABLE IF EXISTS `Environment`;
CREATE TABLE `Environment`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `projectId` int(11) NULL DEFAULT NULL,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `host` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `remark` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of Environment
-- ----------------------------
INSERT INTO `Environment` VALUES (1, 1, '百度测试环境', 'https://www.baidu.com/', '');
INSERT INTO `Environment` VALUES (2, 2, '雪球app测试环境', '{\'platformName\': \'Android\', \'noReset\': \'true\', \'unicodeKeyboard\': \'true\', \'resetKeyboard\': \'true\', \'appPackage\': \'com.xueqiu.android\', \'appActivity\': \'.view.WelcomeActivityAlias\', \'browserName\': \'\'}', '');
INSERT INTO `Environment` VALUES (3, 3, 'backlight测试环境', '{\'platformName\': \'Android\', \'noReset\': \'true\', \'unicodeKeyboard\': \'true\', \'resetKeyboard\': \'true\', \'appPackage\': \'\', \'appActivity\': \'\', \'browserName\': \'chrome\'}', '');


-- ----------------------------
-- Table structure for page
-- ----------------------------
DROP TABLE IF EXISTS `page`;
CREATE TABLE `page`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `projectId` int(11) NOT NULL,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `remark` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `createTime` datetime(6) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of page
-- ----------------------------
INSERT INTO `page` VALUES (1, 1, '百度首页', '', '2019-12-30 22:06:32');
INSERT INTO `page` VALUES (2, 1, '百度搜索页', '', '2019-12-30 22:06:43');
INSERT INTO `page` VALUES (3, 2, '雪球app页面', '', '2019-12-30 22:29:14');
INSERT INTO `page` VALUES (4, 3, 'backlight首页', '', '2019-12-30 22:53:01');

-- ----------------------------
-- Table structure for element
-- ----------------------------
DROP TABLE IF EXISTS `element`;
CREATE TABLE `element`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `projectId` int(11) NOT NULL,
  `pageId` int(11) NOT NULL,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `remark` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `createTime` datetime(6) NULL DEFAULT NULL,
  `by` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `locator` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 149 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of element
-- ----------------------------
INSERT INTO `element` VALUES (1, 1, 1, '百度搜索框', '', '2019-12-30 22:07:54', 'id', 'kw');
INSERT INTO `element` VALUES (2, 1, 1, '百度一下按钮', '', '2019-12-30 22:08:21', 'id', 'su');
INSERT INTO `element` VALUES (3, 1, 2, '搜索内容多个', '', '2019-12-30 22:10:22', 'xpath', '//*[@id=\'content_left\']/div/h3/a');
INSERT INTO `element` VALUES (4, 1, 2, '搜索结果页面标题', '', '2019-12-30 22:11:38', 'xpath', '//*[@id=\"__next\"]/div[1]/div/div/section[1]/h1');
INSERT INTO `element` VALUES (5, 2, 3, '首页搜索框', '', '2019-12-30 22:30:09', 'id', 'com.xueqiu.android:id/home_search');
INSERT INTO `element` VALUES (6, 2, 3, '搜索页面输入框', '', '2019-12-30 22:30:45', 'id', 'com.xueqiu.android:id/search_input_text');
INSERT INTO `element` VALUES (7, 2, 3, '搜索内容联想', '', '2019-12-30 22:31:36', 'id', 'com.xueqiu.android:id/name');
INSERT INTO `element` VALUES (8, 3, 4, '下方系统栏', '', '2019-12-30 22:55:43', 'id', 'com.android.chrome:id/infobar_close_button');
INSERT INTO `element` VALUES (9, 3, 4, '菜单按钮', '', '2019-12-30 22:56:26', 'xpath', '//android.widget.Button[@text=\'菜单\']');

-- ----------------------------
-- Table structure for keyword
-- ----------------------------
DROP TABLE IF EXISTS `keyword`;
CREATE TABLE `keyword`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `projectId` int(11) NOT NULL,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `type` int(11) NOT NULL,
  `package` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `clazz` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `method` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `params` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `steps` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `createTime` datetime(6) NULL DEFAULT NULL,
  `remark` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of keyword
-- ----------------------------
INSERT INTO `keyword` VALUES (1, 0, 'open_url', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'open', '[{\"type\": \"string\", \"key\": \"url\"}, {\"type\": \"string\", \"key\": \"title\"}]', '[]', '2019-12-30 21:55:25', '打开浏览器url');
INSERT INTO `keyword` VALUES (2, 0, 'sleep', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'sleep', '[{\"type\": \"string\", \"key\": \"seconds\"}]', '[]', '2019-12-30 21:56:03', '强制等待');
INSERT INTO `keyword` VALUES (3, 0, 'wait', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'wait', '[{\"type\": \"string\", \"key\": \"seconds\"}]', '[]', '2019-12-30 21:56:24', '隐式等待');
INSERT INTO `keyword` VALUES (4, 0, 'handle_exception', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'handle_exception', '[{\"type\": \"element\", \"key\": \"locator\"}]', '[]', '2019-12-30 21:57:06', '自定义异常处理');
INSERT INTO `keyword` VALUES (5, 0, 'click', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'click', '[{\"type\": \"element\", \"key\": \"locator\"}]', '[]', '2019-12-30 21:57:41', '点击操作');
INSERT INTO `keyword` VALUES (6, 0, 'clicks', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'clicks', '[{\"type\": \"element\", \"key\": \"locator\"}, {\"type\": \"string\", \"key\": \"n\"}]', '[]', '2019-12-30 21:58:25', '点击一组元素中的第几个');
INSERT INTO `keyword` VALUES (7, 0, 'click_text', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'click_text', '[{\"type\": \"element\", \"key\": \"locator\"}, {\"type\": \"string\", \"key\": \"text\"}, {\"type\": \"string\", \"key\": \"n\"}]', '[]', '2019-12-30 21:59:11', '点击指定文本元素');
INSERT INTO `keyword` VALUES (8, 0, 'double_click', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'double_click', '[{\"type\": \"element\", \"key\": \"locator\"}]', '[]', '2019-12-30 21:59:35', '双击操作');
INSERT INTO `keyword` VALUES (9, 0, 'send_keys', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'send_keys', '[{\"type\": \"element\", \"key\": \"locator\"}, {\"type\": \"string\", \"key\": \"text\"}]', '[]', '2019-12-30 22:00:16', '发送文本，清空后输入');
INSERT INTO `keyword` VALUES (10, 0, 'sends_keys', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'sends_keys', '[{\"type\": \"element\", \"key\": \"locator\"}, {\"type\": \"string\", \"key\": \"text\"}, {\"type\": \"string\", \"key\": \"n\"}]', '[]', '2019-12-30 22:03:01', '选中一组元素中的第几个，发送文本，清空后输入');
INSERT INTO `keyword` VALUES (12, 0, 'switch_window_handle', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'switch_window_handle', '[{\"type\": \"string\", \"key\": \"n\"}]', '[]', '2019-12-30 22:05:29', '切换浏览器handle');
INSERT INTO `keyword` VALUES (13, 0, 'switch_context', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'switch_context', '[{\"type\": \"string\", \"key\": \"i\"}]', '[]', '2019-12-30 22:55:13', '手机切换上下文');
INSERT INTO `keyword` VALUES (14, 0, 'maximize_window', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'maximize_window', '[]', '[]', '2019-12-30 23:04:38', '最大化浏览器');
INSERT INTO `keyword` VALUES (17, 0, 'switch_frame', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'switch_frame', '[{\"type\": \"element\", \"key\": \"frame\"}]', '[]', '2020-1-2 19:36:03', '切换iframe');
INSERT INTO `keyword` VALUES (18, 0, 'send_keys_enter', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'send_keys_enter', '[]', '[]', '2020-1-3 14:54:25', '敲enter');
INSERT INTO `keyword` VALUES (19, 0, 'send_keys_down', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'send_keys_down', '[]', '[]', '2020-1-3 14:55:18', '敲向下键');
INSERT INTO `keyword` VALUES (20, 0, 'alert_operations', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'alert_operations', '[{\"type\": \"string\", \"key\": \"opera\"}, {\"type\": \"string\", \"key\": \"text\"}]', '[]', '2020-1-3 14:57:33', '确认alert存在后，可以进行的操作');
INSERT INTO `keyword` VALUES (21, 0, 'move_to_element', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'move_to_element', '[{\"type\": \"element\", \"key\": \"locator\"}]', '[]', '2020-1-3 14:58:13', '鼠标悬停操作');
INSERT INTO `keyword` VALUES (22, 0, 'move', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'move', '[{\"type\": \"element\", \"key\": \"locator\"}, {\"type\": \"element\", \"key\": \"locator1\"}]', '[]', '2020-1-3 14:59:15', '循环调用鼠标事件，死循环');
INSERT INTO `keyword` VALUES (23, 0, 'parent_frame', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'parent_frame', '[]', '[]', '2020-1-3 14:59:34', '跳出frame到父frame');
INSERT INTO `keyword` VALUES (24, 0, 'default_content', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'default_content', '[]', '[]', '2020-1-3 14:59:48', '跳出frame到默认<跳到最外层>');
INSERT INTO `keyword` VALUES (25, 0, 'back', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'back', '[]', '[]', '2020-1-3 15:00:32', '返回之前的网页');
INSERT INTO `keyword` VALUES (26, 0, 'forward', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'forward', '[]', '[]', '2020-1-3 15:00:44', '前往下一个网页');
INSERT INTO `keyword` VALUES (27, 0, 'close', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'close', '[]', '[]', '2020-1-3 15:01:02', '关闭当前网页');
INSERT INTO `keyword` VALUES (28, 0, 'js_execute', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'js_execute', '[{\"type\": \"string\", \"key\": \"js\"}]', '[]', '2020-1-3 15:01:50', '执行js');
INSERT INTO `keyword` VALUES (29, 0, 'js_focus_element', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'js_focus_element', '[{\"type\": \"element\", \"key\": \"locator\"}]', '[]', '2020-1-3 15:02:28', '聚焦元素');
INSERT INTO `keyword` VALUES (30, 0, 'js_scroll_top', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'js_scroll_top', '[]', '[]', '2020-1-3 15:02:43', '滚动到顶部');
INSERT INTO `keyword` VALUES (31, 0, 'js_scroll_bottom', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'js_scroll_bottom', '[]', '[]', '2020-1-3 15:02:55', '滚动到底部');
INSERT INTO `keyword` VALUES (32, 0, 'select_by_index', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'select_by_index', '[{\"type\": \"element\", \"key\": \"locator\"}, {\"type\": \"string\", \"key\": \"index\"}]', '[]', '2020-1-3 15:05:59', '通过索引，index是第几个，从0开始');
INSERT INTO `keyword` VALUES (33, 0, 'select_by_value', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'select_by_value', '[{\"type\": \"element\", \"key\": \"locator\"}, {\"type\": \"string\", \"key\": \"value\"}]', '[]', '2020-1-3 15:06:29', '通过value属性');
INSERT INTO `keyword` VALUES (34, 0, 'select_by_text', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'select_by_text', '[{\"type\": \"element\", \"key\": \"locator\"}, {\"type\": \"string\", \"key\": \"text\"}]', '[]', '2020-1-3 15:07:24', '通过text属性');
INSERT INTO `keyword` VALUES (35, 0, 'save_screenshot', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'save_screenshot', '[{\"type\": \"string\", \"key\": \"img_path\"}]', '[]', '2020-1-3 15:08:06', '获取电脑屏幕截屏');
INSERT INTO `keyword` VALUES (36, 0, 'uploaded', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'uploaded', '[{\"type\": \"string\", \"key\": \"path\"}]', '[]', '2020-4-15 19:55:13', '上传文件');
INSERT INTO `keyword` VALUES (37, 0, 'get_text', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'get_text', '[{\"type\": \"element\", \"key\": \"locator\"}, {\"type\": \"string\", \"key\": \"make\"}]', '[]', '2020-4-15 21:04:27', '获取元素文本，传参make，传递文本');
INSERT INTO `keyword` VALUES (38, 0, 'assert_text', 1, 'Autotest_platform.PageObject.base_page', 'PageObject', 'assert_text', '[{\"type\": \"element\", \"key\": \"locator\"}, {\"type\": \"string\", \"key\": \"text\"}]', '[]', '2020-4-20 08:51:10', '断言函数');

-- ----------------------------
-- Table structure for testcase
-- ----------------------------
DROP TABLE IF EXISTS `testcase`;
CREATE TABLE `testcase`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `projectId` int(11) NOT NULL,
  `title` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `level` int(11) NOT NULL,
  `beforeLogin` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `steps` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `parameter` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `checkType` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `checkValue` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `checkText` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `selectText` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `createTime` datetime(6) NULL DEFAULT NULL,
  `remark` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 82 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of testcase
-- ----------------------------
INSERT INTO `testcase` VALUES (1, 1, '二级页面标题测试用例', 2, '[]', '[{\"keywordId\": \"1\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"url\", \"value\": \"https://www.baidu.com/\"}, {\"isParameter\": false, \"type\": \"string\", \"value\": \"百度一下，你就知道\", \"key\": \"title\"}]}, {\"keywordId\": \"9\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"1\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"selenium\"}]}, {\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"2\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"1\"}]}, {\"keywordId\": \"7\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"3\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"selenium库的基本使用 - 简书\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"n\", \"value\": \"true\"}]}, {\"keywordId\": \"12\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"n\", \"value\": \"1\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"5\"}]}]', '[{\"expect\": true}]', 'element', '4', 'selenium库的基本使用', 'all', '2019-12-30 22:13:07', '');
INSERT INTO `testcase` VALUES (2, 2, '雪球app搜索测试用例', 1, '[]', '[{\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"5\"}]}, {\"keywordId\": \"9\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"6\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"阿里巴巴\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"5\"}]}]', '[{\"expect\": true}]', 'element', '7', '阿里巴巴', 'all', '2019-12-30 22:32:59', '');
INSERT INTO `testcase` VALUES (3, 3, 'backlight测试用例', 1, '[]', '[{\"keywordId\": \"1\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"url\", \"value\": \"http://www.easytest.xyz\"}, {\"type\": \"string\", \"key\": \"title\", \"value\": \"\"}]}, {\"keywordId\": \"13\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"i\", \"value\": \"0\"}]}, {\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"8\"}]}, {\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"9\"}]}]', '[{\"expect\": true}]', 'element', '9', '菜单', 'in', '2019-12-30 22:58:53', '');


-- ----------------------------
-- Table structure for Result
-- ----------------------------
DROP TABLE IF EXISTS `Result`;
CREATE TABLE `Result`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `taskId` int(11) NULL DEFAULT NULL,
  `projectId` int(11) NOT NULL,
  `testcaseId` int(11) NOT NULL,
  `browsers` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `beforeLogin` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `environments` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `status` int(11) NOT NULL,
  `parameter` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `steps` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `checkType` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `checkValue` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `checkText` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `selectText` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `createTime` datetime(6) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 393 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of Result
-- ----------------------------
INSERT INTO `result` VALUES (1, '二级页面标题测试用例', 0, 1, 1, '[\"1\"]', '[]', '[\"1\"]', 40, '[{\"expect\": true}]', '[{\"keywordId\": \"1\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"url\", \"value\": \"https://www.baidu.com\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"title\", \"value\": \"百度一下，你就知道\"}]}, {\"keywordId\": \"9\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"1\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"selenium\"}]}, {\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"2\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"1\"}]}, {\"keywordId\": \"7\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"selenium库的基本使用 - 简书\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"n\", \"value\": \"true\"}, {\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"3\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"5\"}]}]', 'element', '4', 'selenium库的基本使用', 'all', '2019-12-30 22:19:18');
INSERT INTO `result` VALUES (2, '二级页面标题测试用例', 0, 1, 1, '[\"1\"]', '[]', '[\"1\"]', 40, '[{\"expect\": true}]', '[{\"keywordId\": \"1\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"url\", \"value\": \"https://www.baidu.com\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"title\", \"value\": \"百度一下，你就知道\"}]}, {\"keywordId\": \"9\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"1\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"selenium\"}]}, {\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"2\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"1\"}]}, {\"keywordId\": \"7\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"selenium库的基本使用 - 简书\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"n\", \"value\": \"true\"}, {\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"3\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"5\"}]}]', 'element', '4', 'selenium库的基本使用', 'all', '2019-12-30 22:20:44');
INSERT INTO `result` VALUES (3, '二级页面标题测试用例', 0, 1, 1, '[\"1\"]', '[]', '[\"1\"]', 40, '[{\"expect\": true}]', '[{\"keywordId\": \"1\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"url\", \"value\": \"https://www.baidu.com\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"title\", \"value\": \"百度一下，你就知道\"}]}, {\"keywordId\": \"9\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"1\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"selenium\"}]}, {\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"2\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"1\"}]}, {\"keywordId\": \"7\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"selenium库的基本使用 - 简书\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"n\", \"value\": \"true\"}, {\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"3\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"5\"}]}]', 'element', '4', 'selenium库的基本使用', 'all', '2019-12-30 22:23:06');
INSERT INTO `result` VALUES (4, '二级页面标题测试用例', 0, 1, 1, '[\"1\"]', '[]', '[\"1\"]', 40, '[{\"expect\": true}]', '[{\"keywordId\": \"1\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"url\", \"value\": \"https://www.baidu.com\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"title\", \"value\": \"百度一下，你就知道\"}]}, {\"keywordId\": \"9\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"1\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"selenium\"}]}, {\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"2\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"1\"}]}, {\"keywordId\": \"7\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"3\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"selenium库的基本使用 - 简书\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"n\", \"value\": \"true\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"5\"}]}]', 'element', '4', 'selenium库的基本使用', 'all', '2019-12-30 22:24:57');
INSERT INTO `result` VALUES (5, '二级页面标题测试用例', 0, 1, 1, '[\"1\"]', '[]', '[\"1\"]', 40, '[{\"expect\": true}]', '[{\"keywordId\": \"1\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"url\", \"value\": \"https://www.baidu.com\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"title\", \"value\": \"百度一下，你就知道\"}]}, {\"keywordId\": \"9\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"1\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"selenium\"}]}, {\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"2\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"1\"}]}, {\"keywordId\": \"7\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"3\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"selenium库的基本使用 - 简书\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"n\", \"value\": \"true\"}]}, {\"keywordId\": \"12\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"n\", \"value\": \"1\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"5\"}]}]', 'element', '4', 'selenium库的基本使用', 'all', '2019-12-30 22:26:23');
INSERT INTO `result` VALUES (6, '二级页面标题测试用例', 0, 1, 1, '[\"1\"]', '[]', '[\"1\"]', 30, '[{\"expect\": true}]', '[{\"keywordId\": \"1\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"url\", \"value\": \"https://www.baidu.com/\"}, {\"isParameter\": false, \"type\": \"string\", \"value\": \"百度一下，你就知道\", \"key\": \"title\"}]}, {\"keywordId\": \"9\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"1\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"selenium\"}]}, {\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"2\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"1\"}]}, {\"keywordId\": \"7\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"3\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"selenium库的基本使用 - 简书\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"n\", \"value\": \"true\"}]}, {\"keywordId\": \"12\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"n\", \"value\": \"1\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"5\"}]}]', 'element', '4', 'selenium库的基本使用', 'all', '2019-12-30 22:27:03');
INSERT INTO `result` VALUES (7, '二级页面标题测试用例', 0, 1, 1, '[\"2\"]', '[]', '[\"1\"]', 30, '[{\"expect\": true}]', '[{\"keywordId\": \"1\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"url\", \"value\": \"https://www.baidu.com/\"}, {\"isParameter\": false, \"type\": \"string\", \"value\": \"百度一下，你就知道\", \"key\": \"title\"}]}, {\"keywordId\": \"9\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"1\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"selenium\"}]}, {\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"2\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"1\"}]}, {\"keywordId\": \"7\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"3\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"selenium库的基本使用 - 简书\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"n\", \"value\": \"true\"}]}, {\"keywordId\": \"12\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"n\", \"value\": \"1\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"5\"}]}]', 'element', '4', 'selenium库的基本使用', 'all', '2019-12-30 22:27:33');
INSERT INTO `result` VALUES (8, '雪球app搜索测试用例', 0, 2, 2, '[\"3\"]', '[]', '[\"2\"]', 30, '[{\"expect\": true}]', '[{\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"5\"}]}, {\"keywordId\": \"9\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"6\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"阿里巴巴\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"5\"}]}]', 'element', '7', '阿里巴巴', 'all', '2019-12-30 22:33:14');
INSERT INTO `result` VALUES (9, 'backlight测试用例', 0, 3, 3, '[\"4\"]', '[]', '[\"3\"]', 40, '[{\"expect\": true}]', '[{\"keywordId\": \"1\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"url\", \"value\": \"http://www.easytest.xyz\"}, {\"type\": \"string\", \"key\": \"title\", \"value\": \"\"}]}, {\"keywordId\": \"13\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"i\", \"value\": \"0\"}]}, {\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"8\"}]}, {\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"9\"}]}]', 'element', '9', '菜单', 'all', '2019-12-30 22:59:48');
INSERT INTO `result` VALUES (10, 'backlight测试用例', 0, 3, 3, '[\"4\"]', '[]', '[\"3\"]', 40, '[{\"expect\": true}]', '[{\"keywordId\": \"1\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"url\", \"value\": \"http://www.easytest.xyz\"}, {\"type\": \"string\", \"key\": \"title\", \"value\": \"\"}]}, {\"keywordId\": \"13\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"i\", \"value\": \"0\"}]}, {\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"8\"}]}, {\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"9\"}]}]', 'element', '9', '菜单', 'all', '2019-12-30 23:02:06');
INSERT INTO `result` VALUES (11, 'backlight测试用例', 0, 3, 3, '[\"4\"]', '[]', '[\"3\"]', 40, '[{\"expect\": true}]', '[{\"keywordId\": \"1\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"url\", \"value\": \"http://www.easytest.xyz\"}, {\"type\": \"string\", \"key\": \"title\", \"value\": \"\"}]}, {\"keywordId\": \"13\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"i\", \"value\": \"0\"}]}, {\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"8\"}]}, {\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"9\"}]}]', 'element', '9', '菜单', 'all', '2019-12-30 23:05:26');
INSERT INTO `result` VALUES (12, 'backlight测试用例', 0, 3, 3, '[\"4\"]', '[]', '[\"3\"]', 30, '[{\"expect\": true}]', '[{\"keywordId\": \"1\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"url\", \"value\": \"http://www.easytest.xyz\"}, {\"type\": \"string\", \"key\": \"title\", \"value\": \"\"}]}, {\"keywordId\": \"13\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"i\", \"value\": \"0\"}]}, {\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"8\"}]}, {\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"9\"}]}]', 'element', '9', '菜单', 'all', '2019-12-30 23:07:33');
INSERT INTO `result` VALUES (13, '雪球app搜索测试用例', 0, 2, 2, '[\"3\"]', '[]', '[\"2\"]', 30, '[{\"expect\": true}]', '[{\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"5\"}]}, {\"keywordId\": \"9\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"6\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"阿里巴巴\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"5\"}]}]', 'element', '7', '阿里巴巴', 'all', '2019-12-30 23:08:41');
INSERT INTO `result` VALUES (14, '二级页面标题测试用例', 0, 1, 1, '[\"1\", \"2\"]', '[]', '[\"1\"]', 30, '[{\"expect\": true}]', '[{\"keywordId\": \"1\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"url\", \"value\": \"https://www.baidu.com/\"}, {\"isParameter\": false, \"type\": \"string\", \"value\": \"百度一下，你就知道\", \"key\": \"title\"}]}, {\"keywordId\": \"9\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"1\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"selenium\"}]}, {\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"2\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"1\"}]}, {\"keywordId\": \"7\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"3\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"selenium库的基本使用 - 简书\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"n\", \"value\": \"true\"}]}, {\"keywordId\": \"12\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"n\", \"value\": \"1\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"5\"}]}]', 'element', '4', 'selenium库的基本使用', 'all', '2019-12-30 23:09:42');
INSERT INTO `result` VALUES (15, '二级页面标题测试用例', 0, 1, 1, '[\"2\"]', '[]', '[\"1\"]', 30, '[{\"expect\": true}]', '[{\"keywordId\": \"1\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"url\", \"value\": \"https://www.baidu.com/\"}, {\"isParameter\": false, \"type\": \"string\", \"value\": \"百度一下，你就知道\", \"key\": \"title\"}]}, {\"keywordId\": \"9\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"1\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"selenium\"}]}, {\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"2\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"1\"}]}, {\"keywordId\": \"7\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"3\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"selenium库的基本使用 - 简书\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"n\", \"value\": \"true\"}]}, {\"keywordId\": \"12\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"n\", \"value\": \"1\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"5\"}]}]', 'element', '4', 'selenium库的基本使用', 'all', '2019-12-31 09:30:11');
INSERT INTO `result` VALUES (16, '二级页面标题测试用例', 0, 1, 1, '[\"1\"]', '[]', '[\"1\"]', 30, '[{\"expect\": true}]', '[{\"keywordId\": \"1\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"url\", \"value\": \"https://www.baidu.com/\"}, {\"isParameter\": false, \"type\": \"string\", \"value\": \"百度一下，你就知道\", \"key\": \"title\"}]}, {\"keywordId\": \"9\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"1\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"selenium\"}]}, {\"keywordId\": \"5\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"2\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"1\"}]}, {\"keywordId\": \"7\", \"values\": [{\"isParameter\": false, \"type\": \"element\", \"key\": \"locator\", \"value\": \"3\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"text\", \"value\": \"selenium库的基本使用 - 简书\"}, {\"isParameter\": false, \"type\": \"string\", \"key\": \"n\", \"value\": \"true\"}]}, {\"keywordId\": \"12\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"n\", \"value\": \"1\"}]}, {\"keywordId\": \"2\", \"values\": [{\"isParameter\": false, \"type\": \"string\", \"key\": \"seconds\", \"value\": \"5\"}]}]', 'element', '4', 'selenium库的基本使用', 'all', '2019-12-31 09:37:43');

-- ----------------------------
-- Table structure for SplitResult
-- ----------------------------
DROP TABLE IF EXISTS `SplitResult`;
CREATE TABLE `SplitResult`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `environmentId` int(11) NULL DEFAULT NULL,
  `browserId` int(11) NULL DEFAULT NULL,
  `resultId` int(11) NOT NULL,
  `step_num` int(11) NOT NULL,
  `loginStatus` int(11) NOT NULL,
  `createTime` datetime(6) NULL DEFAULT NULL,
  `startTime` datetime(6) NULL DEFAULT NULL,
  `finishTime` datetime(6) NULL DEFAULT NULL,
  `parameter` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `error_name` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expect` tinyint(1) NOT NULL,
  `status` int(11) NOT NULL,
  `remark` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 33 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of SplitResult
-- ----------------------------