# Stillin Project

## Commit Messages

**IMPORTANT**: Before creating any commit message, ALWAYS read [.claude/commit-message-guidelines.md](.claude/commit-message-guidelines.md) and follow its format exactly.

## Build System

This project uses Bazel with Bzlmod for dependency management. A hermetic Bazel is provided at `./bazel`.

### Dependencies

- **rules_python** (1.7.0) - Python toolchain
- **aspect_rules_py** (1.6.6) - Python build rules (py_binary, py_library, py_test)
- **rules_uv** (0.89.2) - UV-based requirements compilation

### Python Requirements

- Add dependencies to `requirements.in`
- Run `./bazel run //:generate_requirements_txt` to compile `requirements.txt`
- The `generate_requirements_txt_test` target automatically verifies requirements.txt is up-to-date

### Writing Python Targets

Use rules from `@aspect_rules_py//py:defs.bzl`:

```starlark
load("@aspect_rules_py//py:defs.bzl", "py_binary", "py_library", "py_test")

py_library(
    name = "mylib",
    srcs = ["mylib.py"],
    deps = ["@pip//some_package"],
)

py_binary(
    name = "myapp",
    srcs = ["main.py"],
    deps = [":mylib"],
)

py_test(
    name = "mylib_test",
    srcs = ["mylib_test.py"],
    deps = [":mylib"],
)
```

### Using pip Dependencies

Import pip packages using `@pip//<package_name>`:

```starlark
deps = [
    "@pip//gpiozero",
]
```

### GPIO Access

The `.bazelrc` configures `--spawn_strategy=local` to disable Bazel's sandbox. This is required because GPIO access needs `/dev/gpiomem` which isn't available inside the sandbox.

### Common Commands

```bash
# Compile requirements.in to requirements.txt
./bazel run //:generate_requirements_txt

# Build a target
./bazel build //path/to:target

# Run a binary
./bazel run //path/to:binary

# Run tests
./bazel test //...
```
