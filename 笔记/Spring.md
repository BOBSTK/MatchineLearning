# Spring

## 1、简介

- 向后兼容，简化企业应用开发，整合了现有得技术框架。
- 开源的免费框架；
- 轻量级的、非入侵式的框架。
- 支持事务的处理，对框架整合的支持
- **控制反转(IOC)，面向切面编程(AOP)**

SSH: Struct2 + Spring + Hibernate

 SSM: SpringMvc + Spring + Mybatis

 官网：https://spring.io/

依赖

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-webmvc</artifactId>
    <version>5.2.6.RELEASE</version>
</dependency>
```

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-jdbc</artifactId>
    <version>5.2.6.RELEASE</version>
</dependency>
```

## 2、IOC理论推导

### 2.1为什么

- 之前的业务中，用户的需求可能会影响我们原来的代码，我们需要根据用户的需求去修改源代码！
- 程序主动创建对象，控制权在程序员手上！
- 如果程序代码量十分大，**修改一次的成本代价很高**！

使用set注入后，程序不再具有主动性，而成了被动的接受对象，系统的耦合性大大降低，这是IOC的原型！

### 2.2是什么

- 控制反转Ioc(Inversion of control)是一种设计思想，**DI(依赖注入)**是实现Ioc的一种方法。
- Ioc是Spring的核心内容，新版本可以零配置实现Ioc。

Spting容器在初始化时先读取配置文件，根据配置文件或元数据创建与组织对象存入容器，程序使用时再从Ioc容器中取出需要的对象。

