## 本项目基于[chineseocr](https://github.com/ouyanghuiyu/chineseocr_lite) 

# 环境
- pytorch
- python3

# 配置
- 参考[Python构建快速高效的中文文字识别OCR](https://blog.csdn.net/lly1122334/article/details/104752851)
## PSENET 编译
``` Bash
cd psenet/pse
rm -rf pse.so 
make 
```
  
# 运行
``` bash
python app.py
```
访问
http://localhost:8888/
