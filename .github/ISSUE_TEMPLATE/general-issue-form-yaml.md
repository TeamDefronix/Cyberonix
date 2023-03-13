---
name: general-issue-form.yaml
about: If you get any issues in this tool you can report it here
title: ''
labels: ''
assignees: ''

---

body:
  - type: markdown
    attributes:
      value: |
        _Before reporting:_ search [existing issues](https://github.com/TeamMetaxone/Cyberonix/issues) (both open and closed).
        If you need real-time help, join us on Discord. Thank you for helping us improve!
  - type: textarea
    id: problem-description
    attributes:
      label: Problem description
      description: Also tell us, what did you expect to happen?
      placeholder: |
        Steps to reproduce the behavior:
        1. Go to '...'
        2. Click on '....'
        3. Scroll down to '....'
        4. See error
    validations:
      required: true
  - type: input
    id: version
    attributes:
      label: python version
      description: "use python -v"
      placeholder: |
        branch-commit
    validations:
      required: true
    required: true
  - type: textarea
    id: steps
    attributes:
      label: "Steps to reproduce"
      description: "Steps to reproduce"
  - type: textarea
    id: screenshots
    attributes:
      label: Screenshots
      description: If applicable, add screenshots to help explain your problem
