![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Autodesk Maya](https://img.shields.io/badge/Autodesk-Maya-0696D7?style=for-the-badge)

# QuickRotateTool for Autodesk Maya

## Overview

**QuickRotateTool** is a lightweight rigging utility for quickly adjusting the rotation of selected objects and controllers in Maya. Enter a rotation increment for the **X, Y, and Z** axes, then use the buttons to apply positive or negative adjustments without repeatedly typing values in the Channel Box.

> **Easy installation:** Simply **drag and drop `QRT_DragAndDrop_OneLine.py` into the Maya viewport**. The tool automatically creates a button on your currently selected shelf.

## Features

- **Drag-and-drop installation** directly into the Maya viewport
- **Automatic shelf button** for quick access
- **Manual X / Y / Z rotation increments** with adjustable values
- **+ / − buttons** to increase or decrease each input value by `0.1`
- **Tweak All + / Tweak All −** to apply the entered rotation increments to all selected objects
- **Multiple-selection support** for adjusting several objects at once
- **Skips locked rotation attributes** instead of changing them
- **Self-contained shelf command** — no separate script path required after installation

## Installation

1. Open **Autodesk Maya**.
2. Select the **shelf tab** where you want the tool.
3. **Drag and drop `QRT_DragAndDrop_OneLine.py` into the Maya viewport.**
4. Click the new **QuickRotateTool** shelf button to open the UI.

The installer embeds the tool into the shelf command, so the original installer file does not need to remain in the same location after installation.

## How to Use

1. Select one or more objects or rig controllers.
2. Open **QuickRotateTool** from the shelf.
3. Enter the desired rotation increments in **Manual Tweak** (`X`, `Y`, `Z`).
4. Click **Tweak All +** to add those values to the current rotations, or **Tweak All −** to subtract them.

**Example:** Enter `0`, `5`, `0` and click **Tweak All +** to increase each selected object's `rotateY` by 5 degrees. Click **Tweak All −** to decrease it by 5 degrees.

## Notes

- Changes are **relative** to the current rotation values; the tool does not set an absolute orientation.
- **Tweak All** affects the standard `rotateX`, `rotateY`, and `rotateZ` attributes.
- Locked rotation channels are skipped. Other non-editable channels or connections may still cause Maya errors.
- The small `+` and `−` buttons next to the fields adjust the **input values**, not the selected object's rotation directly.
- The tool uses `maya.cmds` and is intended for use inside Autodesk Maya.

## Feedback

Created as a personal rigging workflow utility to reduce repetitive manual rotation adjustments. Suggestions and improvements are welcome.
