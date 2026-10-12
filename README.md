# Exact Raster Boundary

Creates a vector boundary from valid raster pixels, rather than using the rectangular raster extent. Uses QGIS/PyQGIS, GDAL/OGR, and NumPy available in the QGIS Python environment.

## Input modes

- **Single file (checkbox unchecked):** select one raster file.
- **Bulk folder (checkbox checked):** select a folder and process all supported raster files. Enable the subfolder option to search recursively.

Supported extensions: TIF, TIFF, IMG, ECW, JP2, JPG, JPEG, PNG.

Outputs are written to the selected output folder as `<raster_name>_boundary.shp`. If an output with that name already exists, a numbered suffix is used to avoid overwriting it.

## Install

In QGIS, open **Plugins → Manage and Install Plugins → Install from ZIP** and select the plugin ZIP.

## License

GNU General Public License v2 or later.
