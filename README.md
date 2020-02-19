如何使用该模型？

1. 下载该项目，同时安装项目所依赖的Python模块: tensorflow, tornado;

2. 运行run.py，启动模型训练、预测的HTTP服务;

3. 在浏览器中输入: http://localhost:12306/model_train ，即可开始模型训练；或者直接运行train.py也可。模型训练的时间较长，需耐心等待，生成后的模型文件位于ckpt文件夹。

4. 模型预测为POST请求，可输入如下命令：

```python
curl -d "event=***" http://localhost:12306/subj_extract
```
理论介绍可以参考：https://www.cnblogs.com/gczr/p/12045358.html

注意事项：
1、参数配置在文件config_file，尤其num_tags表示标记总个数，包括程序里自动添加的CLS,SEP
2、maps.pkl保存的是tags与其对应ID的字典映射，在预测的时候还要加载用
3、本模型只有BiLSTM和CRF参数参与了训练，ALBERT只提供embedding功能，不参与训练。
4、albert_zh存放albert模型的python文件
5、albert_tiny存放albert的模型预训练参数，albert_config_tiny.json主要是albert模型内部的配置。
6、训练好整体模型参数存放在ckpt里面

语料：
CHINESE GLUE的MSRANER标注语料，该数据集共有5万多条中文命名实体识别标注数据（包括人名、地名、组织名），分别用nr、ns、nt表示，其他实体用o表示。
数据量：训练集(46,364)，测试集(4,365)
数据格式如下（与原始文件格式一致）

据说/o 应/o 老友/o 之/o 邀/o ，/o 梁实秋/nr 还/o 坐/o 着/o 滑竿/o 来/o 此/o 品/o 过/o 玉峰/ns 茶/o 。/o

链接：http://106.13.187.75:8003/dataSet
