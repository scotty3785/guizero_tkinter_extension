# guizero_tkinter_extension

## Adding Extensions

Copy the GUIZeroTemplates.py file to the location of idlelib
On windows this is C:\Python3X\Lib\idlelib
On debian/linux it is in /usr/lib/python3.X/idlelib/

Edit the 'config-extensions.def' file contained inside idlelib adding the following at the end of the file.

```
[GUIZeroTemplates]
enable=True
enable_editor=True
[GUIZeroTemplates_bindings]
add_guizero_button=
add_guizero_text=
```

Two new menu option should appear in the 'Format' menu.

## Limitations
IDLE extension cannot create a new menu, they can only add to existing menus. If a specific GUIZero menu is required, the Binding.py and EditorWindow.py files require modification.

## Future Thoughts
- [ ] Have a single menu option but a seperate GUI that appears with an option to configure/add new 'widgets'.
- [ ] Have a dedicated GUIZero top-level menu.
- [ ] Menu option to create a new GUIZero code file with imports and basic structure.

