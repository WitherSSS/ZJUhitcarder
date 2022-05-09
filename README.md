# ZJUhitcarder

## Step1. Fork本仓库

1. 点击右上角`Fork`Fork本仓库到自己github账号下

## Step2. 添加账⼾密码

1. 点击仓库的右上⻆的`Settings`

2. 点击下⾯的`Secret`

3. 点击右上⻆的`New repository Secret`，添加⼀个Secret

Name必须为ACCOUNT，Value填⼊⾃⼰的浙⼤通⾏证账号，注意name和value的前后不要前后有多余空格。然后仿照上⾯的操作，再添加⼀个Name为PASSWORD，Value为浙⼤通⾏证密码的Secret，⾃动打卡脚本就配置完成了。

## Step3. 开启github action

1. 在`Action`的`Workflows`中`Enable workflow`

### 如何触发打卡？

有两种⽅式，第⼀种是在⾃⼰的仓库⾥点击`Star`（已经Star的就取消Star，再重新点击）。
第⼆种是等待8小时，这个脚本是每隔8小时触发⼀次的。

### 如何判断打卡是否成功？

每次触发打卡就会在右边多出⼀个记录，⽐如现在我已经执⾏过四次打卡脚本了，点击你需要查看的记
录，再点击⾥⾯的`ClockIn`按钮，我们就可以看到本次打卡的情况了

### Q: 这个脚本安全么？

这个脚本是开源的，⼤家可以⾃由观看它的代码，内容很简单，没有任何窃取个⼈信息的操作我们的账⼾密码是放⼊github的secret中的，只有仓库的所有者才能看到你设置的ACCOUNT和PASSWORD。
这个项⽬的所有者虽然是我，但你是先Fork再操作的，此时Fork得到的仓库所有者是你⾃⼰，我们所有的操作都是在Fork后进⾏的，我是没有办法看到你的secret的。
所以只要保证你⾃⼰的github账号密码不泄漏，浙⼤通⾏证的密码就是安全的
