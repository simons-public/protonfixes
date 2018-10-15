### Example using a copy of the default user_settings.sample.py renamed to user_settings.py
To just enable protonfixes, all that must be done is to add the `import protonfixes` line to the bottom of the file.
```python
#to enable these settings, name this file "user_settings.py"

user_settings = {
    #logs are saved to $HOME/steam-$STEAM_APP_ID.log, overwriting any previous log with that name
    "WINEDEBUG": "+timestamp,+pid,+tid,+seh,+debugstr,+module",

    "DXVK_LOG_LEVEL": "info",

    #Enable DXVK's HUD
#    "DXVK_HUD": "devinfo,fps",

    #Use wined3d for d3d11 instead of dxvk
#    "PROTON_USE_WINED3D11": "1",

    #Disable d3d11 entirely
#    "PROTON_NO_D3D11": "1",

    #Disable in-process synchronization primitives
#    "PROTON_NO_ESYNC": "1",
}

import protonfixes
```


### Example with protonfixes debugging turned on

```python
#to enable these settings, name this file "user_settings.py"
user_settings = {
    #logs are saved to $HOME/steam-$STEAM_APP_ID.log, overwriting any previous log with that name
    "WINEDEBUG": "+timestamp,+pid,+tid,+seh,+debugstr,+module",
    "DXVK_LOG_LEVEL": "info",
    #Enable DXVK's HUD
#    "DXVK_HUD": "devinfo,fps",
    #Use wined3d for d3d11 instead of dxvk
#    "PROTON_USE_WINED3D11": "1",
    #Disable d3d11 entirely
#    "PROTON_NO_D3D11": "1",
    #Disable in-process synchronization primitives
#    "PROTON_NO_ESYNC": "1",
}

from protonfixes import debug
import protonfixes
```