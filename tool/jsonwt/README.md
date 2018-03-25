Json Web Token

JWT 代表 JSON Web Token ，它是一种用于认证头部的 token 格式。这个 token 帮你实现了在两个系统之间以一种安全的方式传递信息。
 token 包含了三部分：header，payload，signature。
header 是 token 的一部分，用来存放 token 的类型和编码方式，通常是使用 base-64 编码。
payload 包含了信息。你可以存放任一种信息，比如用户信息，产品信息等。它们都是使用 base-64 编码方式进行存储。
signature 包括了 header，payload 和密钥的混合体。密钥必须安全地保存储在服务端。

优势
基于 token 的认证在解决棘手的问题时有几个优势：
Client Independent Services 。在基于 token 的认证，token 通过请求头传输，而不是把认证信息存储在 session 或者 cookie 中。这意味着无状态。你可以从任意一种可以发送 HTTP 请求的终端向服务器发送请求。
CDN 。在绝大多数现在的应用中，view 在后端渲染，HTML 内容被返回给浏览器。前端逻辑依赖后端代码。这中依赖真的没必要。而且，带来了几个问题。比如，你和一个设计机构合作，设计师帮你完成了前端的 HTML，CSS 和 JavaScript，你需要拿到前端代码并且把它移植到你的后端代码中，目的当然是为了渲染。修改几次后，你渲染的 HTML 内容可能和设计师完成的代码有了很大的不同。在基于 token 的认证中，你可以开发完全独立于后端代码的前端项目。后端代码会返回一个 JSON 而不是渲染 HTML，并且你可以把最小化，压缩过的代码放到 CDN 上。当你访问 web 页面，HTML 内容由 CDN 提供服务，并且页面内容是通过使用认证头部的 token 的 API 服务所填充。
No Cookie-Session (or No CSRF) 。CSRF 是当代 web 安全中一处痛点，因为它不会去检查一个请求来源是否可信。为了解决这个问题，一个 token 池被用在每次表单请求时发送相关的 token。在基于 token 的认证中，已经有一个 token 应用在认证头部，并且 CSRF 不包含那个信息。
Persistent Token Store 。当在应用中进行 session 的读，写或者删除操作时，会有一个文件操作发生在操作系统的temp 文件夹下，至少在第一次时。假设有多台服务器并且 session 在第一台服务上创建。当你再次发送请求并且这个请求落在另一台服务器上，session 信息并不存在并且会获得一个“未认证”的响应。我知道，你可以通过一个粘性 session 解决这个问题。然而，在基于 token 的认证中，这个问题很自然就被解决了。没有粘性 session 的问题，因为在每个发送到服务器的请求中这个请求的 token 都会被拦截。

Before we get started, it's important to note that JWT does not encrypt the payload, it only signs it. You should not send any secret information using JWT, rather you should send information that is not secret but needs to be verified. For instance, sending a signed user id to indicate the user that should be logged in would work great! Sending a user's password would be very, very bad.

You can include an iat claim in your payload that is a UNIX timestamp of when the token was issued. The decoder should then check that this timestamp is within a certain valid window or otherwise reject it.You can include an exp claim in your payload that is a UNIX timestamp indicating when the token will expire. The decoding end should check that the current time is before the expiration and otherwise reject the token.You can assign a unique value to the jti claim. This way, the decoding end can check to make sure that the token has never been consumed before, making sure that it is one-use.

