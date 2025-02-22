# Documentation
``` bash
PLAY [localhost] ****************************************************************************************

TASK [Gathering Facts] **********************************************************************************
ok: [localhost]

TASK [docker : Update apt cache] ************************************************************************
ok: [localhost]

TASK [docker : Install Docker] **************************************************************************
ok: [localhost]

TASK [docker : Install Docker Compose] ******************************************************************
ok: [localhost]

TASK [docker : Add current user to the docker group] ****************************************************
[WARNING]: Skipping plugin (/usr/lib/python3/dist-packages/ansible/plugins/filter/core.py) as it seems
to be invalid: cannot import name 'environmentfilter' from 'jinja2.filters'
(/home/julia/.local/lib/python3.10/site-packages/jinja2/filters.py)
[WARNING]: Skipping plugin (/usr/lib/python3/dist-packages/ansible/plugins/filter/mathstuff.py) as it
seems to be invalid: cannot import name 'environmentfilter' from 'jinja2.filters'
(/home/julia/.local/lib/python3.10/site-packages/jinja2/filters.py)
ok: [localhost]

TASK [docker : Start Docker Service] ********************************************************************
[WARNING]: Skipping plugin (/usr/lib/python3/dist-packages/ansible/plugins/filter/core.py) as it seems
to be invalid: cannot import name 'environmentfilter' from 'jinja2.filters'
(/home/julia/.local/lib/python3.10/site-packages/jinja2/filters.py)
[WARNING]: Skipping plugin (/usr/lib/python3/dist-packages/ansible/plugins/filter/mathstuff.py) as it
seems to be invalid: cannot import name 'environmentfilter' from 'jinja2.filters'
(/home/julia/.local/lib/python3.10/site-packages/jinja2/filters.py)
```
