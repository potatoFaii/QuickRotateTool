![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Autodesk Maya](https://img.shields.io/badge/Autodesk-Maya-0696D7?style=for-the-badge)

# Channel Control Editor for Autodesk Maya

---

## Overview

**Channel Control Editor** is a lightweight rigging utility designed to help riggers quickly **show or hide standard transform attributes in Maya's Channel Box** across multiple selected controllers.

Preparing a rig often involves repeating the same Channel Box cleanup steps on dozens of controllers. Instead of editing each controller's channel settings individually, this tool provides a simple checkbox interface for applying consistent channel settings to the entire selection in one operation.

The tool can be installed by dragging its Python installer directly into the Maya viewport. It creates a shelf button for quick access.

> **Note:** This tool changes attribute locking and keyability/channel visibility settings. It does **not** delete attributes, hide controllers in the viewport, or reset attribute values.

---

## Features

- **Drag-and-drop installation** directly into the Maya viewport
- **Automatic shelf button creation** on the currently active Maya shelf
- **Batch editing** of multiple selected transform controllers
- **Checkbox-based channel selection** for Translate, Rotate, Scale, and Visibility
- **Show / Hide controls** to quickly change Channel Box availability
- **All checkbox** for selecting or clearing every supported channel group
- **Self-contained shelf command** — no external script path required after installation
- **Readable Python source** — no Base64 or compressed code payload
- **Reinstall support** — updates an existing matching shelf button instead of creating a duplicate on that shelf

---

## Supported Attributes

| Checkbox | Maya Attributes | Description |
|---|---|---|
| **Rotate** | `rx`, `ry`, `rz` | Rotation channels |

The checkboxes choose **which attributes will be affected**; they do not directly change channel settings until **ShowAttribute** or **HideAttribute** is clicked.

---

## Feedback & Contributions

This is an evolving personal rigging workflow tool.

Feedback, production suggestions, and improvement ideas are welcome. If you encounter issues or would like to suggest enhancements, feel free to open an issue or reach out.

---

## License

Provided **as-is** for personal and educational use.
