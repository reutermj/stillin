# Stillin Project

## System Dependencies

Some Python packages with C extensions require system libraries to build. Install these before running Bazel:

```bash
sudo apt install swig clang liblgpio-dev
```

## Commit Messages

**IMPORTANT**: Before creating any commit message, ALWAYS read [.claude/commit-message-guidelines.md](.claude/commit-message-guidelines.md) and follow its format exactly.

## Build System

This project uses Bazel with Bzlmod for dependency management. A hermetic Bazel is provided at `./bazel`.

### Python Requirements

- Add dependencies to `requirements.in`
- Run `./bazel run //:generate_requirements_txt` to compile `requirements.txt`

### Writing Python Targets

Use rules from `@aspect_rules_py//py:defs.bzl`:

```starlark
load("@aspect_rules_py//py:defs.bzl", "py_binary", "py_library", "py_test")

py_library(
    name = "mylib",
    srcs = ["mylib.py"],
    deps = ["@pip//some_package"], # Using a pip dependency
)

py_binary(
    name = "myapp",
    srcs = ["main.py"],
    deps = [":mylib"], # Using a bazel dependency
)

py_test(
    name = "mylib_test",
    srcs = ["mylib_test.py"],
    deps = [":mylib"],
)
```

### GPIO Access

This project uses **gpiozero** for GPIO control. The `.bazelrc` configures `--spawn_strategy=local` to disable Bazel's sandbox, which is required because GPIO access needs `/dev/gpiomem` which isn't available inside the sandbox.

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
