# datasheet_cli

Simple Google Search for datasheets (pdf) of any specified component.


Install
-----
```bash
    pip install .
```

Use
-----

```bash
    # Simple search
    datasheet bc548

    # Search with manufaturer
    datasheet LPC4337 -m nxp

    # Expanded search
    datasheet lm7805 -n 20

    # String search
    datasheet "pc923 optocoupler"

    # Show help
    datasheet --help
```

