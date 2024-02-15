# Easy Discord Webhook Message

A Python package for easily sending messages through Discord webhooks.

## Installation

Install the package using pip:

```bash
pip install easy_discord_webhook_message
```

## Usage

```python
from easy_discord_webhook_message import Webhook

# Create an instance of the Webhook class
webhook_instance = Webhook()

# Define the webhook URL
webhook_instance.define_webhook_url("your_discord_webhook_url")

# Define mentions (optional)
webhook_instance.define_mentions(["userId1", "userId2"])

# Define content (optional)
webhook_instance.define_content("Hello @user1, check this out!")

# Send a message
webhook_instance.send(
    title="New Release",
    description="Version 1.0 is now available!",
    author="Your Bot",
    color="00FF00",
    url="https://github.com/yourusername/yourrepository/releases/tag/v1.0"
)
```

## How to Contribute

We appreciate your interest in contributing. This document outlines the various ways you can contribute to the project.
Bug Reports and Feature Requests

If you encounter a bug or have a feature request, please open an issue on GitHub. When opening an issue, please provide detailed information about the problem or enhancement you are proposing.
### Code Contributions
#### Fork and Clone

1. Fork the repository to your GitHub account.
2. Clone the forked repository to your local machine.

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

#### Create a Branch

Create a new branch for your contribution.

```bash
git checkout -b feature/your-feature
```

#### Make Changes

Make your changes to the codebase.

#### Commit Changes

Commit your changes with a descriptive commit message.

```bash
git commit -m "Add your descriptive commit message"
```

#### Push Changes

Push your changes to your fork on GitHub.

```bash
git push origin feature/your-feature
```

### Create a Pull Request

1. Navigate to the Pull Requests tab of the original repository.
2. Click on "New Pull Request."
3. Select the branch with your changes.
4. Provide a descriptive title and summary of your changes.

## Code Style

Follow the existing code style and conventions in the project. If in doubt, refer to the project's style guide.

## Tests

Contribute to the tests by updating existing project

## Documentation

Contribute to the documentation by updating existing documentation or creating new documentation where needed.

## Security

If you discover security vulnerabilities, please follow our Security Policy for responsible disclosure.

## How to Reach Us

If you have questions or need assistance, feel free to reach out:

- Email
- Community Forum
- Gitter Chat

We appreciate your contributions to Easy Discord Webhook Message! Thank you for helping make this project better.
