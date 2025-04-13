# CHANGELOG


## v2.4.5 (2025-04-13)

### Bug Fixes

- Fixes fallback bug with pydantic
  ([`70d1257`](https://github.com/crypticorn-ai/api-client/commit/70d125723c7e707f765892270e6aa6977b5b25a5))


## v2.4.4 (2025-04-12)

### Bug Fixes

- Auth fixes on auth module
  ([`7c3ed5d`](https://github.com/crypticorn-ai/api-client/commit/7c3ed5d460e464939716361014514baff50d380d))

### Documentation

- Update advanced usage section
  ([`1c804bf`](https://github.com/crypticorn-ai/api-client/commit/1c804bf6eddceb19c31a553c1ff98b31fdd8cbc0))


## v2.4.3 (2025-04-12)

### Bug Fixes

- Fix utils import
  ([`29cc346`](https://github.com/crypticorn-ai/api-client/commit/29cc346c2ff835f8732644fbe21aadf62153c1d0))


## v2.4.2 (2025-04-12)

### Bug Fixes

- Add global utils and add http error mapping
  ([`c3ce565`](https://github.com/crypticorn-ai/api-client/commit/c3ce565446535038f196f65b9fdf276a6ce71563))


## v2.4.1 (2025-04-12)

### Bug Fixes

- Add market metrics scopes
  ([`2dc0b4f`](https://github.com/crypticorn-ai/api-client/commit/2dc0b4f1761d5bae07c946448a820d1fc9814288))

### Documentation

- Update structure section
  ([`cc77abc`](https://github.com/crypticorn-ai/api-client/commit/cc77abc19b5813e335356f4539654e04b8ba2014))


## v2.4.0 (2025-04-12)

### Features

- Add enum fallbacks, enum validation mixin and enum tests
  ([`63bd61c`](https://github.com/crypticorn-ai/api-client/commit/63bd61cd826f9de1aec40d5f877d82126b59fbf8))

- Start cli support for initializing files from templates
  ([`5411d12`](https://github.com/crypticorn-ai/api-client/commit/5411d12704605e6d6af46477ff74e1ac44abd259))


## v2.3.0 (2025-04-11)

### Features

- Add exchange and market enums
  ([`8ad2d7d`](https://github.com/crypticorn-ai/api-client/commit/8ad2d7dc982261f3e710c3e61755ea9613d982c3))


## v2.2.3 (2025-04-11)

### Bug Fixes

- Update error codes
  ([`3121fb0`](https://github.com/crypticorn-ai/api-client/commit/3121fb0bb4d05a6d62083d806fbc636761254448))


## v2.2.2 (2025-04-09)

### Bug Fixes

- Refactor generated model name by partial_model and add to init file
  ([`e663848`](https://github.com/crypticorn-ai/api-client/commit/e6638483bdeb01121749b579268493c7c67227dc))


## v2.2.1 (2025-04-09)

### Bug Fixes

- Add pydantic decorator that makes all fields of a model optional
  ([`1ae4432`](https://github.com/crypticorn-ai/api-client/commit/1ae44325194be3ca86eb72be5d3edc2442dd00cc))


## v2.2.0 (2025-04-09)

### Bug Fixes

- Fix import issues (fixes #22) and add auth module to main client
  ([`7f3f7c2`](https://github.com/crypticorn-ai/api-client/commit/7f3f7c2120af053b916aaa045444331998986f7d))

### Documentation

- Update README with configuration and response type sections
  ([`a9fbccf`](https://github.com/crypticorn-ai/api-client/commit/a9fbccfed254573d3e62332901704f39d8a6777f))

### Features

- Add module based configuration options for the client
  ([`553400c`](https://github.com/crypticorn-ai/api-client/commit/553400c642d3da4459daa4fa9b56588e9f519581))


## v2.1.6 (2025-04-08)

### Bug Fixes

- Add market metrics module
  ([`2954702`](https://github.com/crypticorn-ai/api-client/commit/29547025a0226bca1b9da9cfff5c89d3ed30f497))


## v2.1.5 (2025-04-08)

### Bug Fixes

- Update auth and trade module
  ([`df936b6`](https://github.com/crypticorn-ai/api-client/commit/df936b6eb76179a3eac6d7997c82ef30e74de860))


## v2.1.4 (2025-04-08)

### Bug Fixes

- Refactor api errors
  ([`885a20e`](https://github.com/crypticorn-ai/api-client/commit/885a20ec839dcf14fb4ec8d946cea76dcb15a65e))


## v2.1.3 (2025-04-08)

### Bug Fixes

- Use SecurityScopes class instead of list[Scope]
  ([`b41c718`](https://github.com/crypticorn-ai/api-client/commit/b41c718acc108e05b307abb399137c2fc30e56fd))


## v2.1.2 (2025-04-08)

### Bug Fixes

- Allow scopes to be set as strings
  ([`600babb`](https://github.com/crypticorn-ai/api-client/commit/600babb87c93aeecdc42aa19ebff1076a76404ea))


## v2.1.1 (2025-04-08)

### Bug Fixes

- Remove three unused scopes
  ([`3167308`](https://github.com/crypticorn-ai/api-client/commit/3167308b3df0c68b8e4c134841b437f40315a8e9))


## v2.1.0 (2025-04-07)

### Features

- Add api key authorization and websocket auth support
  ([`adeb8bd`](https://github.com/crypticorn-ai/api-client/commit/adeb8bdf42ed3da1b63b430f291e920e97d62d14))

### Refactoring

- Rename scopes and make requirements more strict
  ([`abf53a6`](https://github.com/crypticorn-ai/api-client/commit/abf53a6de46703a3ac2b0c66c101ec58ae8928f2))


## v2.0.1 (2025-04-06)

### Bug Fixes

- Refactor Scopes and Exception handling in auth client
  ([`8e9a64a`](https://github.com/crypticorn-ai/api-client/commit/8e9a64aa091cc3c840230ad2a7167c98426ae5c9))

### Build System

- Fix ci syntax and ssh errors
  ([`9ecfaa4`](https://github.com/crypticorn-ai/api-client/commit/9ecfaa4f09dfa4ae1667f9c1b9307d2623288f5f))

- Separate ci and update package config and deps
  ([`5367f2a`](https://github.com/crypticorn-ai/api-client/commit/5367f2a79028ed1f5e2c05ddded91a9ddbd0d9fa))

- Update ci
  ([`799fd96`](https://github.com/crypticorn-ai/api-client/commit/799fd962529b0120b290c3f5c253e9050b40a41b))

### Documentation

- Update Readme
  ([`39825b1`](https://github.com/crypticorn-ai/api-client/commit/39825b1506c2d5663ae8eecc6f73f8d6bed5692e))


## v2.0.0 (2025-04-06)

### Build System

- Add psr build_command
  ([`b661846`](https://github.com/crypticorn-ai/api-client/commit/b6618464c7d7727d34ab4a448f2e0104fcf4f3cc))

- Fix ci-cd
  ([`6edcb36`](https://github.com/crypticorn-ai/api-client/commit/6edcb3611673f191ec482e9d40614c7c2d2b59f3))

- Fix signing error in ci
  ([`0dcbf22`](https://github.com/crypticorn-ai/api-client/commit/0dcbf22892dbc17297cf9b91b35d62ec205a76ea))

- Fixes pypi packages dir
  ([`a25a458`](https://github.com/crypticorn-ai/api-client/commit/a25a4580c6a656e30d55b52c837480b833cb9aab))

- Update ci cd and configure PSR
  ([`e5d6fa5`](https://github.com/crypticorn-ai/api-client/commit/e5d6fa5d2ff4355f59fd4c92e4b9bed77fcae2d8))

BREAKING CHANGE: add several more backend api clients and restructure the modules


## v1.0.0 (2024-11-27)

### Continuous Integration

- Trigger workflow on PRs and changes to public folder (close #4)
  ([`08b9317`](https://github.com/crypticorn-ai/api-client/commit/08b931780ac872c6034883cd5ab83d2c7b380414))

### Features

- Add get Economics News
  ([`81575b1`](https://github.com/crypticorn-ai/api-client/commit/81575b18a7c925c5dafe18bd9e15807a282134e3))

- Add get Economics News
  ([`ccbfb7a`](https://github.com/crypticorn-ai/api-client/commit/ccbfb7a3d857ff5d531ec06f3b9df05b63f8dbf3))

- Add get Economics News
  ([`bc6574d`](https://github.com/crypticorn-ai/api-client/commit/bc6574dcadcdc9d05e860fde0aa285a4e7dcba32))
