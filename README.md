
# 3D Model Viewer

A 3D Model Viewer application built using PyQt5 and PyOpenGL. This tool allows users to load, display, and interact with 3D models in `.obj` format. The application provides an intuitive interface to rotate, zoom, and highlight specific points on the model. Ideal for designers, engineers, and anyone interested in 3D graphics.

---

## Features

- **3D Model Rendering**: Load and display `.obj` files with vertex data.
- **Model Interaction**: Rotate the model using the mouse, zoom in and out with the scroll wheel.
- **Highlight Points**: Input specific coordinates to highlight points on the model in red.
- **User-Friendly Interface**: Built with PyQt5 for a seamless and responsive UI.

---

## Preview

![Video Preview](image/IMG_2816.mp4)

---

## Installation

### Prerequisites
Ensure you have Python 3.8+ installed and the following libraries:

- PyQt5
- PyOpenGL
- numpy

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/amin-Lotfi/3d-model-viewer.git
   cd 3d-model-viewer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place your `.obj` file in the root directory and rename it to `obj.obj`.
4. Run the application:
   ```bash
   python main.py
   ```

---

## Usage

1. **Load Model**: The program automatically loads the `obj.obj` file in the root directory.
2. **Interact with the Model**:
   - **Rotate**: Click and drag the left mouse button to rotate the model.
   - **Zoom**: Use the mouse scroll wheel to zoom in or out.
3. **Highlight Point**:
   - Right-click on the window to open the coordinate input dialog.
   - Enter the coordinates (x, y, z) to highlight the desired point in red.

---

## File Structure
```
3d-model-viewer/
├── image/
│   └── IMG_2816.mp4
├── obj.obj
├── main.py
├── requirements.txt
└── README.md
```

---

## Example `.obj` File
Ensure your `.obj` file contains vertex data in the following format:

```
v 1.0 0.0 0.0
v 0.0 1.0 0.0
v 0.0 0.0 1.0
```

---

## Contributing
Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request.

---

## Contact
For any inquiries or issues, feel free to reach out at:
- Email: aminlotfi.ogl@gmail.com
- GitHub: [amin-Lotfi](https://github.com/amin-Lotfi)
