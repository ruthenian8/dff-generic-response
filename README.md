
# DFF Generic Response

[DFF Generic Response](https://github.com/ruthenian8/dff-generic-response) is an extension to the [Dialogflow Engine](https://github.com/deepmipt/dialog_flow_engine), a minimalistic open-source engine for conversational services.

[DFF Generic Response](https://github.com/ruthenian8/dff-generic-response) introduces a GenericResponse class as well as generic classes for various media types. Using this API, you can create identical responses in dff adapters for Telegram, Yandex's Alice, or other services instead of learning service-specific classes. 

Note that some of the options that are present in the generic response will be ignored, when the service API does not support them. For instance, since Yandex's Alice does not support sending videos or documents, fields like `video` or `attachment` will be skipped by `dff-alice-adapter`.  

<!-- uncomment one of these to add badges to your project description -->
<!-- [![Documentation Status](https://dff-generic-response.readthedocs.io/en/stable/?badge=stable)](https://readthedocs.org/projects/dff-generic-response/badge/?version=stable) -->
<!-- [![Coverage Status](https://coveralls.io/repos/github/ruthenian8/dff-generic-response/badge.svg?branch=main)](https://coveralls.io/github/ruthenian8/dff-generic-response?branch=main) -->
<!-- [![Codestyle](https://github.com/ruthenian8/dff-generic-response/workflows/codestyle/badge.svg)](https://github.com/ruthenian8/dff-generic-response)
[![Tests](https://github.com/ruthenian8/dff-generic-response/workflows/test_coverage/badge.svg)](https://github.com/ruthenian8/dff-generic-response) -->
[![License Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/ruthenian8/dff-generic-response/blob/main/LICENSE)
![Python 3.6, 3.7, 3.8, 3.9](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-green.svg)
<!-- [![PyPI](https://img.shields.io/pypi/v/dff-generic-response)](https://pypi.org/project/dff-generic-response/)
[![Downloads](https://pepy.tech/badge/dff-generic-response)](https://pepy.tech/project/dff-generic-response) -->

# Quick Start
## Installation
```bash
pip install dff-generic-response
```

## Basic example
```python

```

To get more advanced examples, take a look at [examples](https://github.com/ruthenian8/dff-generic-response/tree/main/examples) on GitHub.

# Contributing to the Dialog Flow Engine

Please refer to [CONTRIBUTING.md](https://github.com/deepmipt/dialog_flow_engine/blob/dev/CONTRIBUTING.md).