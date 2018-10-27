几天前学习多模块依赖的时候,添加了模块间的依赖后,提示找不到依赖,今天搜索gradle implementation找到了解决方案,原来是com.android.tools.build:gradle:3.0.0-beta6插件跟原来比改动了很多东西.转个帖子.

android gradle tools 3.X 中依赖,implement、api 指令

安卓工程依赖方式:Implementation vs API dependency

 

用api指令编译,Glide依赖对app Module 是可见的 

 

用implement指令编译依赖对app Module 是不可见的 

Android Gradle plugin 3.0带来了解决方案 

最新版的Gradle plugin需要你指出一个module的接口是否对外暴露其依赖lib的接口。基于此,可以让项目构建时,gradle可以判断哪个需要重新编译。因此,老版本的构建关键字compile被废弃了,而是改成了这两个:
api:同compile作用一样,即认为本module将会泄露其依赖的module的内容。
implementation:本module不会通过自身的接口向外部暴露其依赖module的内容。
由此,我们可以明确的告诉gradle去重新编译一个module,若是这个使用的module的接口发生变化的话。

dependencies { 

//当legofy接口发生变化时,需要重新编译本module以及所有使用本module的module 

api project(':legofy') 

// 仅当landscapevideocamera发生变化时,重新编译本module 

implementation project(':landscapevideocamera:1.0.0') 

} 

其它的变化 

既然有了比较大的改变,索性官方团队利用此机会改了更多配置属性的名字,
比如provided改成了compileOnly,apk改成了runtimeOnly