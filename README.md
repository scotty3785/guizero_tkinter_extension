# guizero_tkinter_extension

## Adding Extensions

Copy the GUIZeroTemplates.py file to the location of idlelib

Edit the 'config-extensions.def' file to contain the following.

```
[GUIZeroTemplates]
enable=True
enable_editor=True
[GUIZeroTemplates_bindings]
add_guizero_button=
add_guizero_text=
```

Two new menu option should appear in the 'Format' menu.

##Limitations
IDLE extension cannot create a new menu, they can only add to existing menus. If a specific GUIZero menu is required, the Binding.py and EditorWindow.py files require modification.