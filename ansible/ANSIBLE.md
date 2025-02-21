# Documentation
```
PLAY [localhost] *******************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [localhost]

TASK [Ensure Docker Compose is installed] ******************************************************************************

TASK [docker : Update apt cache] ***************************************************************************************
ok: [localhost]

TASK [docker : Install Docker] *****************************************************************************************
ok: [localhost]

TASK [docker : Install Docker Compose] *********************************************************************************
ok: [localhost]

TASK [docker : Add current user to the docker group] *******************************************************************
[WARNING]: Skipping plugin (/usr/lib/python3/dist-packages/ansible/plugins/filter/core.py) as it seems to be invalid:
cannot import name 'environmentfilter' from 'jinja2.filters' (/home/julia/.local/lib/python3.10/site-
packages/jinja2/filters.py)
[WARNING]: Skipping plugin (/usr/lib/python3/dist-packages/ansible/plugins/filter/mathstuff.py) as it seems to be
invalid: cannot import name 'environmentfilter' from 'jinja2.filters' (/home/julia/.local/lib/python3.10/site-
packages/jinja2/filters.py)
ok: [localhost]

TASK [web-app : Create directory for app] ******************************************************************************
[WARNING]: Skipping plugin (/usr/lib/python3/dist-packages/ansible/plugins/filter/core.py) as it seems to be invalid:
cannot import name 'environmentfilter' from 'jinja2.filters' (/home/julia/.local/lib/python3.10/site-
packages/jinja2/filters.py)
[WARNING]: Skipping plugin (/usr/lib/python3/dist-packages/ansible/plugins/filter/mathstuff.py) as it seems to be
invalid: cannot import name 'environmentfilter' from 'jinja2.filters' (/home/julia/.local/lib/python3.10/site-
packages/jinja2/filters.py)
ok: [localhost]

TASK [web-app : Copy Docker Compose template] **************************************************************************
[WARNING]: Skipping plugin (/usr/lib/python3/dist-packages/ansible/plugins/filter/core.py) as it seems to be invalid:
cannot import name 'environmentfilter' from 'jinja2.filters' (/home/julia/.local/lib/python3.10/site-
packages/jinja2/filters.py)
[WARNING]: Skipping plugin (/usr/lib/python3/dist-packages/ansible/plugins/filter/mathstuff.py) as it seems to be
invalid: cannot import name 'environmentfilter' from 'jinja2.filters' (/home/julia/.local/lib/python3.10/site-
packages/jinja2/filters.py)
ok: [localhost]

TASK [web-app : Deploy application with Docker Compose] ****************************************************************
[WARNING]: Skipping plugin (/usr/lib/python3/dist-packages/ansible/plugins/filter/mathstuff.py) as it seems to be
invalid: cannot import name 'environmentfilter' from 'jinja2.filters' (/home/julia/.local/lib/python3.10/site-
packages/jinja2/filters.py)
ok: [localhost]

PLAY RECAP *************************************************************************************************************
localhost                  : ok=8    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
