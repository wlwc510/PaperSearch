# PaperSearch
由四个部分组成

### 1. NcCrawler ###
爬虫 负责搜集原始的期刊全文数据 此部分采用了MongoDB数据库，需要本地安装数据库

### 2. vue-biblio-system-ly ###
前端代码 负责界面可视化 与 交互功能实现 基于https://github.com/lin-xin/vue-manage-system 修改而来

### 3. papersearch ###
后端代码基于 https://github.com/lihengming/spring-boot-api-project-seed 修改而来

### 4. CPyWebMachine ###
模型实现与服务 基于flask的web框架以及 sci-kit learn实现
