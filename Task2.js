{
    "id": "login-test",
    "name": "Login Page Valid/Invalid Credentials Test",
    "commands": [
      {
        "command": "open",
        "target": "https://example.com/login",
        "value": ""
      },
      {
        "command": "type",
        "target": "id=username",
        "value": "validUser"
      },
      {
        "command": "type",
        "target": "id=password",
        "value": "validPassword123"
      },
      {
        "command": "click",
        "target": "id=login-button",
        "value": ""
      },
      {
        "command": "assertText",
        "target": "id=welcome-message",
        "value": "Welcome validUser"
      },
      {
        "command": "open",
        "target": "https://example.com/login",
        "value": ""
      },
      {
        "command": "type",
        "target": "id=username",
        "value": "invalidUser"
      },
      {
        "command": "type",
        "target": "id=password",
        "value": "wrongPassword"
      },
      {
        "command": "click",
        "target": "id=login-button",
        "value": ""
      },
      {
        "command": "assertText",
        "target": "id=error-message",
        "value": "Invalid credentials"
      }
    ]
  }
  