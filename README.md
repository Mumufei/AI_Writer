# -简 介-
该项目可以根据用户给出的上文自动生成下文
该项目是本人的本科毕业设计。项目主要基于GPT-2 Chinese实现。本人的工作主要是用新的语料库进行了几次训练，得出来了一个还凑合的模型。该项目已经初步完成，不再进行进一步的更新。
演示效果参看以下视频
<video src="https://www.iqiyi.com/v_19rxoxbkhk.html#curid=16678996500_b4cdcb4320cdfae5f480487b73576efb" controls="controls" width="500" height="300">您的浏览器不支持播放该视频！</video>
# -系统环境-
本人不保证在其他环境下可以运行该项目，也不保证在其他环境下一定不能运行
0)  Windows 10，系统版本1903
1)	NVIDIA GTX1060 6G，显卡驱动为Geforce Game Ready Driver 442.59
2)	Python 3.7，且Python库安装了torch、numpy、tqdm、sklearn、keras、tb-nightly、future、thulac
3)	CUDA 10.1及cuDNN 7.6.5 for CUDA 10.1
4)  使用软件：Anaconda 3、Pycharm、Windows Terminal(Preview)、

# -GPT-2 Chinese-
项目的深度学习代码基于[GPT-2 Chinese](https://github.com/Morizeyao/GPT2-Chinese)项目。
安装方法：
请先于NVIDIA官网下载
  0)  显卡驱动
  1)  CUDA 10.1
  2)  cuDNN 7.6.5 for CUDA 10.1
之后，在Windows Terminal中将工作路径跳转到gpt-2 chinese目录下输入pip install -r requirements.txt

本人在几乎对GPT-2没有改动的前提下，为该项目添加了bat脚本：
  0)  train.bat  训练脚本
  1)  generate.bat  生成脚本
可以根据自己的需要调整bat脚本

# -语料库-
如果您想使用我们的语料库，可以在[网盘链接](https://pan.baidu.com/s/1LcHMtyhUEqpGa46bA1aDTg)（提取码：9k3e）下载语料库。语料库包含：
  0)  已经转换为GPT-2 Chinese要求的JSON格式的《最终幻想14》截至5.1版本的剧本
  1） 已经转换为GPT-2 Chinese要求的JSON格式的《少女前线》截至4月1日的剧本
  2） 尚未转换为GPT-2 Chinese要求的JSON格式的《Fate/Grand Order》1.0的剧本
爬取和整合数据的方式可以参考文件夹“Spider”中的Python脚本
