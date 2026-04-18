# Grazioso Salvare Rescue Animal Dashboard

## Required Functionality

This project provides Grazioso Salvare with a functional, interactive web dashboard to help identify suitable canine candidates for search-and-rescue training. The dashboard interfaces with a MongoDB database containing animal shelter data and allows users to filter, visualize, and explore this data in real-time.

### Key Features

#### Interactive Filtering

Users can filter animal data based on three specific search-and-rescue profiles using radio buttons:

- **Water Rescue**: Filters for intact females of specific water-proficient breeds under two years of age
- **Mountain/Wilderness Rescue**: Filters for intact males of specific mountain-proficient breeds under two years of age
- **Disaster/Individual Tracking**: Filters for intact males of specific tracking-proficient breeds under two years of age
- **Reset**: Clears all filters and displays all animals in the database

#### Dynamic Data Table

An interactive table displays animals matching the current filter criteria. The table supports:
- Native column sorting
- Column filtering
- Pagination for large datasets

#### Data Visualization Chart

A pie chart displays the proportional distribution of breeds for animals currently visible in the data table. The chart updates automatically as filters are applied.

#### Geolocation Mapping

A map displays the location of a selected animal. Clicking a row in the data table places a marker on the map at the animal's grid coordinates, with:
- A tooltip showing the animal's breed
- A popup showing its name

## Tools and Rationale

This project was built using a modern Python-based web stack, chosen for its efficiency, powerful data handling capabilities, and robust visualization options.

### MongoDB (The Model Component)

MongoDB was selected as the database due to its nature as a NoSQL, document-oriented database:

- **Flexibility**: Schema-less design accommodates variations from different animal shelters without requiring rigid table structures
- **Rich Query Language**: Enables complex compound filters (age, sex, breed) required by Grazioso Salvare
- **Python Integration**: PyMongo provides a simple API, allowing developers to work with database documents as native Python dictionaries

### Dash Framework (The View and Controller Components)

Dash was used to build the web application, providing both the "View" (HTML layout) and "Controller" (Python callbacks):

- **Pure Python**: Creates complex, interactive dashboards without writing separate JavaScript, HTML, and CSS
- **Reactive Callbacks**: Functions automatically triggered by user interactions (clicks, selections) for dynamic, responsive applications
- **Component Libraries**: `dash_table` for interactive tables and `dash_leaflet` for geolocation maps

### Supporting Libraries and Resources

| Library | Purpose |
|---------|---------|
| **Pandas** | Data manipulation and DataFrame structure for handling MongoDB data |
| **Plotly Express** | Creating the data visualization (pie chart) with seamless Dash/pandas integration |
| **JupyterDash** | Dash version designed to run directly inside Jupyter Notebook |

## Project Steps

1. **Module Enhancement**: Updated the `CRUD_Python_Module` - modified `__init__` to accept all connection parameters, enhanced the `read` method to support MongoDB projections

2. **Dashboard Layout**: Constructed HTML layout in `ProjectTwoDashboard.ipynb` including Grazioso Salvare logo, student identifier, `dcc.RadioItems` for filtering, `dash_table.DataTable`, and Div elements for chart and map

3. **Filtering Logic**: Implemented `update_dashboard` callback to build and execute MongoDB queries based on selected radio button, returning data to update the DataTable

4. **Chart Implementation**: Created `update_graphs` callback that takes filtered data, uses pandas to group by breed, and generates a Plotly Express pie chart

5. **Map Implementation**: Implemented `update_map` callback to extract latitude/longitude from selected table row and render a dash_leaflet map with a marker

6. **Debugging and Refinement**: Fixed data type errors (TypeError) and empty/initial states (IndexError). Added robust guard clauses and try-except blocks for application stability

## Challenge and Resolution

**Challenge**: Map not displaying when clicking radio buttons to change targets

**Resolution**: Added the `selected_rows=[0]` property to the `dash_table.DataTable` component. This forces the table to pre-select the first row upon loading, providing the map callback with initial data needed to render. This resolved the startup error and made the dashboard fully functional with interactive filters updating the map.

## Author

Oliver Flores
