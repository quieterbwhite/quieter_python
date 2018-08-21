## **Step 1 —— 学习一门语言（Learn a Language）**

语言有很多选择，我已经将它们分成几类，以便更容易做出决定。对于刚开始进入后端开发的初学者，我建议你选择任何脚本语言，因为它们有很多功能，可以让你快速起步。如果你有一些前端知识，你可能会发现 Node.js 更容易（还有一个很大的就业市场）。

如果你已经是后端开发并了解一些脚本语言，我建议不要选择其他脚本语言，而是从「函数式（Functional）」或「多范式（Multiparadigm）」中选择。例如，如果你已经在使用 PHP 或Node.js，请不要使用 Python 或 Ruby，而应该尝试使用 Erlang 或 Golang。它一定会帮助你延伸思维，并将你的思想带到新的视野。

## **Step 2 —— 练习你学到的东西（Practice what you have Learnt）**

没有比实践更好的学习方式了。一旦你选择了语言，并且对这些概念有了基本的了解，就可以使用它们，尽你所能制作尽可能多的小应用。下面是一些让你开始的 Idea：

-   在 bash 中实现一些你自己使用的命令，比如尝试实现 ls；
-   编写一个获取和保存 reddit 上 `/r/programming` 文章的命令，并保存为 JSON；
-   编写一个以 JSON 格式列出目录结构的命令，例如 jsonify dir-name 返回一个带有 dir-name 内部结构的 JSON 文件；
-   编写一个读取从上面的步骤得到的 JSON 的命令，并创建目录结构；
-   考虑将每天做的一些任务，并尝试将其自动化。

## **Step 3 —— 学习软件包管理器（Learn Package Manager）**

了解该语言的基础知识并制作了一些示例应用之后，需要了解如何使用该语言的软件包管理器，包管理器可帮助在应用程序中使用外部库，并分发你自己的库供其他人使用。

如果你选择了 PHP，你将学习的是 Composer，Node.js 有 NPM 或 Yarn，Python 有 Pip，Ruby 有 RubyGems。无论选择什么，请继续学习如何使用其包管理器。

## **Step 4 —— 标准和最佳实践 （ Standards and Best Practices）**

每种语言都有自己的标准和开发的最佳实践，例如 PHP 有 PHP-FIG 和 PSR，使用 Node.js 有许多不同的社区驱动指南，其他语言也有相同的指导。

## **Step 5 —— 安全（Security）**

请务必阅读有关安全的最佳实践，阅读 OWASP 指南并了解不同的安全问题以及如何以选择的语言避免它们。

## **Step 6 —— 实践（Practice）**

你已经掌握了语言、标准和最佳实践的基础知识，安全性以及如何使用软件包管理器。现在开始创建一个包并分发给其他人使用，并确保遵循迄今为止学到的标准和最佳实践。例如，如果您选择了 PHP，那么可以在 Packagist 上发布，如果选择了Node.js，那么可以在 Npm 上发布，等等。

如果完成了，在 Github 上搜索一些项目，并在某些项目中提一些 PR。下面是一些 Idea：

-   重构并实现学到的最佳实践
-   查看未解决的 issue 并尝试解决
-   添加任何附加功能

## **Step 7 —— 了解测试（Learn about Testing）**

了解如何在应用程序中编写单元测试和集成测试，另外，了解不同的测试术语，如`mocks`, `stubs` 等

## **Step 8 —— 练习（Practical）**

为目前为止所做的实际任务编写单元测试，尤其是步骤 6 中所做的练习。还要学习和计算编写的测试的覆盖率。

## **Step 9 —— 了解关系数据库（Learn about the Relational Databases）**

了解如何将数据保存在关系数据库中。在选择要学习的工具之前，请先了解不同的数据库术语，例如键，索引，规范化，元组等。

这里有几个选项，但如果你学习一个，其的应该也是相当容易去学。你想学习的应该是 MySQL，MariaDB 和 PostgreSQL。可以选择 MySQL。

## **Step 10 —— Practical Time**

现在是时候把学到的东西拿来用了，使用迄今为止学到的所有内容创建一个简单的应用程序。选择任何一个 idea，可以是创建一个简单的博客，并实现其中的以下功能：

-   用户帐户 —— 注册和登录
-   注册用户可以创建博客文章
-   用户应该能够查看他创建的所有博客文章
-   用户应该能够删除他们的博客文章
-   确保用户只能看到他的个人博客文章（而不能看其他人的）
-   编写单元/集成测试
-   应该为查询应用索引，分析查询以确保索引有作用。

## **Step 11 —— 学习框架（ Learn a Framework）**

根据选择的项目和语言，可能需要也可能不需要框架。每种语言都有几个不同的选项，继续看看选择的语言有哪些选项可供选择，然后选择一个。

如果选择了 PHP，我会建议使用 Laravel 或 Symfony 以及微架构（Lumen 或 Slim），如果你选择 Node.js，有几种不同的选择，但突出的是 Express.js。

## **Step 12 ——  Practical Time**

将 step10 中创建的应用程序转换为使用选择的框架，还要确保移植包括测试在内的所有内容。

## **Step 13 —— 学习 NoSQL 数据库（Learn a NoSQL Database）**

首先了解它们是什么，它们与关系数据库有什么不同以及为什么需要它们。 有几种不同的选择，稍微研究下看看，并比较它们的特点和差异。 可以选择的一些常用选项有 MongoDB，Cassandra，RethinkDB 和 Couchbase，如果必须选择一个，请使用 MongoDB。

## **Step 14 —— 缓存（Caching）**

了解如何在应用程序中实现应用程序级缓存，了解如何使用 Redis 或 Memcached，并在 step 12 中创建的应用程序中使用缓存。

## **Step 15 —— 创建 RESTful API（Creating RESTful APIs）**

了解 REST 并学习如何制作 RESTful API，在 Roy Fielding 的文章中阅读关于 REST 的部分，如果他们说 REST 只适用于 HTTP API，那么确保你能够与他人争论。

## **Step 16  —— 了解不同的认证方法（Learn about Different Auth Methods）**

了解不同的认证和认证方法，你应该知道他们是什么，有什么不同以及什么时候使用偏好。

-   OAuth — Open Authentication
-   Basic Authentication
-   Token Authentication
-   JWT — JSON Web Tokens
-   OpenID

## **Step 17  ——  消息代理（Message Brokers）**

了解消息代理并了解何时以及为何使用它们。同样有多种选择，但突出的是 RabbitMQ 和Kafka，如果你想选择一个的话，可以先从 RabbitMQ 开始。

## **Step 18 —— 搜索引擎（Search Engines）**

随着应用程序的增长，关系数据库或 NoSQL 数据库的简单查询不能够满足要求，而不得不求助于搜索引擎。

## **Step 19 —— 了解如何使用Docker（ Learn how to use Docker）**

无论是在复制与生产环境相同的环境，保持操作系统清洁或加快编码、测试或部署，Docker 可以在开发过程中大大方便工作，学习如何使用 Docker。

## **Step 20 —— Web 服务器知识（Knowledge of Web Servers）**

如果你已经走到这么远了，你可能已经在前面的步骤中使用了服务器，这一步主要是找出不同Web 服务器之间的差异，了解限制和不同的可用配置选项，以及如何最好地利用这些限制编写应用程序。

## **Step 21 —— 了解如何使用Web Scoket（Learn how to use Web Sockets）**

虽然不是必需的，但在工具带中有这些知识是有益的，学习如何使用 web-sockets 编写实时Web 应用程序并使用它创建一些示例应用程序。可以在上面制作的博客应用程序中使用它来实现博客文章列表中的实时更新。

## **Step 22 —— 学习 GraphQL（Learn GraphQL）**

学习如何使用 GraphQL 制作 API，了解它与 REST 的不同之处，以及它为什么被称为 REST 2.0。

## **Step 23 —— 看看图数据库（Look into Graph Databases）**

图模型代表了一种非常灵活的处理数据关系的方式，图数据库为其提供了快速高效的存储、检索和查询方式，学习如何使用 Neo4j 或 OrientDB。

## **Step 24 —— 继续探索（Keep Exploring）**

一旦你开始学习和练习，你一定会遇到我们在这个路线图中没有涉及的东西，只要保持开放的心态和对新事物的渴望就好。

关键是要尽可能多地练习，起初你可能会觉得你并没有抓住任何东西，但这是正常的，随着时间的推移，你会觉得越来越好。