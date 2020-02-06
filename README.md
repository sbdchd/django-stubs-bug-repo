# django stubs bug

When not using `django.contrib.auth` app the django-stubs mypy plugin errors.


```shell
poetry install

# if we run mypy we get a traceback

❯ poetry run mypy --show-traceback --config-file mypy.ini .
./core/views.py:6: error: INTERNAL ERROR -- Please try using mypy master on Github:
https://mypy.rtfd.io/en/latest/common_issues.html#using-a-development-mypy-build
Please report a bug at https://github.com/python/mypy/issues
version: 0.761
Traceback (most recent call last):
  File "mypy/checker.py", line 399, in accept
  File "mypy/nodes.py", line 1062, in accept
  File "mypy/checker.py", line 2004, in visit_assignment_stmt
  File "mypy/checker.py", line 2046, in check_assignment
  File "mypy/checker.py", line 2746, in check_lvalue
  File "mypy/checkexpr.py", line 1932, in analyze_ordinary_member_access
  File "mypy/checkmember.py", line 126, in analyze_member_access
  File "mypy/checkmember.py", line 143, in _analyze_member_access
  File "mypy/checkmember.py", line 225, in analyze_instance_member_access
  File "mypy/checkmember.py", line 376, in analyze_member_var_access
  File "mypy/checkmember.py", line 593, in analyze_var
  File "/Users/steve/Downloads/django-attempt/.venv/lib/python3.7/site-packages/mypy_django_plugin/transformers/request.py", line 11, in set_auth_user_model_as_type_for_request_user
    model_cls = django_context.apps_registry.get_model(auth_user_model)
  File "/Users/steve/Downloads/django-attempt/.venv/lib/python3.7/site-packages/django/apps/registry.py", line 205, in get_model
    app_config = self.get_app_config(app_label)
  File "/Users/steve/Downloads/django-attempt/.venv/lib/python3.7/site-packages/django/apps/registry.py", line 162, in get_app_config
    raise LookupError(message)
LookupError: No installed app with label 'auth'.
./core/views.py:6: : note: use --pdb to drop into pdb
```
