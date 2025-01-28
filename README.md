# 桌面助手

一个功能丰富的桌面助手应用，提供多种实用工具和服务。

## 功能特点

- 🕒 实时时钟显示
- 🌤️ 天气查询
- 💱 货币转换
- 🚗 交通信息查询
- 📅 日程管理
- 🔍 网络搜索
- 🌐 网页内容抓取
- 💬 AI对话助手
- 🎨 深色/浅色主题切换

## 安装说明

1. 克隆项目到本地：
```
git clone https://github.com/AnthonyDuan1128/desktop-assistant
cd desktop-assistant
```

2. 安装依赖：
```
pip install -r requirements.txt
```

3. 配置设置：
   - 复制 `config.example.json` 为 `config.json`
   - 在 `config.json` 中填入相应的API密钥

4. 运行应用：
```
python src/main.py
```

## 打包说明

使用以下命令将应用打包为可执行文件：
```
python build.py
```
打包后的程序将在 `dist` 目录下生成。

## 使用说明

- 按 `Esc` 键显示菜单
- 在对话框中输入内容后按回车进行查询
- 点击相应按钮使用不同功能
- 通过设置按钮可以切换主题

## 配置文件说明

配置文件 `config.json` 包含以下设置：
- API密钥配置
- 界面主题设置
- 语言设置

## 系统要求

- Python 3.8 或更高版本
- Windows 7/10/11
- 网络连接

## 常见问题

1. **应用无法启动**
   - 检查是否已安装所有依赖
   - 确认配置文件格式正确

2. **API服务无响应**
   - 检查网络连接
   - 验证API密钥是否正确

3. **界面显示异常**
   - 尝试切换主题
   - 重启应用

## 更新日志

### v1.0.0 (2024-03)
- 初始版本发布
- 实现基础功能
- 添加主题切换
- 集成AI对话功能

## 贡献指南

欢迎提交 Pull Request 或创建 Issue。

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 联系方式

如有问题或建议，请通过以下方式联系：
- 提交 Issue
- 发送邮件至 [help@duanmail.xyz]
