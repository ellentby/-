## 纯本地抽奖（专业）应用

### 快速开始

1. 打开index.html，点击“开始滚动”
2. 专业名称会开始随机滚动
3. 点击”抽！“停止滚动

### 定制抽奖内容

1. （可跳过）将抽奖内容保存在`majors.xlsx`中，运行`python genMajorsJson.py`，生成相对应的`majors.json`文档
2. （可跳过）将`majors.json`中的json对象赋给`majors.js`中的`majors`变量
3. 修改`index.html`中的`randMajor()`函数，使之适应`majors.js`中的`majors`变量的格式

> 可以利用1.2.步从excel表中提取抽奖内容，也可以直接修改majors.js定制抽奖内容。

### 环境

- 生成抽奖内容（可选）

  Python 3和package openpyxl


