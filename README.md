# Land Cover Accuracy Toolbox
Python-based ArcGIS toolbox for assessing accuracy of land cover maps compared to a set of ground truth points. 

## Getting Started

These instructions will enable you to run the Accuracy Toolbox in ArcGIS Pro or Desktop.

### Prerequisites
Required: ArcGIS Pro 2.0 or higher AND/OR ArcGIS Desktop 10.4.1
Recommended: 64-bit Background Processing if using ArcGIS Desktop

### Installing

Download this repository and unzip it to a folder on a drive accessible to your computer. Local drives may perform better than network drives.

Open ArcGIS Pro or ArcMap:
* In ArcGIS Pro, open the catalog tab, right click on the toolbox folder, select add toolbox, and navigate to the location of the downloaded/unzipped toolbox.
* In ArcMap, open the toolbox tab, right click, select add toolbox, and navigate to the location of the downloaded/unzipped toolbox.

## Usage

### Check Reference Points
* "Reference Points" should be a point shapefile containing a field that has been attributed with vegetation classes matching those used in the land cover map.
* "Reference Field" is the field in the "Reference Points" shapefile that has been attributed with vegetation classes matching those used in the land cover map.
* "Input Raster" is the land cover or vegetation map that will be compared to the "Reference Points".
* "Raster Field" is the field in the "Input Raster" that has been attributed with the vegetation classes.
* "Workspace" folder is a folder in which temporary products will be stored until the tool finishes. "Workspace" should be empty.
* "Output Pivot Table" is the xslx spreadsheet file that will store the table showing user's and producer's accuracy per class.

## Credits

### Built With
* ArcGIS Desktop 10.4.1
* ArcGIS Pro 2.0
* Python 3
* xlsxwriter
* Notepad ++

### Authors

* **Timm Nawrocki** - *Alaska Center for Conservation Science, University of Alaska Anchorage*

### Usage Requirements

If using this tool or derivatives of this tool, please cite as follows:
Nawrocki, T.W. 2017. Land Cover Accuracy Toolbox. Git Repository. Available: https://github.com/accs-uaa/land-cover-accuracy

### License

This project is provided under the GNU General Public License v3.0. It is free to use and modify in part or in whole.
