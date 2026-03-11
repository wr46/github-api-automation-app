# Runners Documentation

Runners **[runners.py](github_automation/automation/repositories/runners.py)** are runnable classes that can be added in **[Option Enum](github_automation/cli/cli.py)** and called in the **[main.py](github_automation/main.py)** file.

```python
if opt.value.has_runner:
    core.execute(opt.value.runnable)
```
Each runner class must implement **execute()** function and have one **[context_file](github_automation/configuration/context_files)** as action configuration

```python
# Example
def __init__(self):
    super().set_context('list_repositories.yaml')
```

## Note:
- Use the following configuration context [template](github_automation/configuration/context_files/template.yaml) to add new contexts