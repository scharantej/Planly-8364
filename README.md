# Flask Web Application Design for Smart Time

## HTML Files

### index.html
- Main page of the website
- Contains the user interface for inputting tasks and time slots
- Includes an HTML form with necessary fields for user inputs

### planner.html
- Displays the generated planner
- Presents the tasks and time slots in a visual and easy-to-understand format
- Provides a clean and user-friendly interface

## Routes
### /
- The home page of the application
- Renders the `index.html` file

### /create_planner
- Receives user input from the `index.html` form
- Processes the tasks and time slots
- Generates the planner based on the user's input
- Renders the `planner.html` file with the generated planner

### /delete_planner
- Allows users to delete their planner
- Removes the planner data from the database
- Redirects to the home page (`/`)