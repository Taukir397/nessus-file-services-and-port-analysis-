# nessus-file-services-and-port-analysis-
services and ports can be extracted  from a nessus file and csv format can also be downloaded 

    Set up the directory structure:

- app.py
- templates/
  - index.html
- static/
  - styles.css
- uploads/ (create this directory)
.....................................................................................................................
    Install the necessary dependencies. You can use pip to install Flask and other required packages:

$ pip install flask xmltodict

  Create the app.py file 

      Create the index.html template in the templates directory. Customize it with your desired HTML and CSS for the user interface.

    Optionally, create a styles.css file in the static directory to add custom styles to your application.

    Create the uploads directory in the same location as app.py. This directory will store the uploaded .nessus files temporarily.

    Run the Flask application:

$ python3 app.py

    Access the application in your web browser at http://localhost:5000. You should be able to upload a .nessus file, and the application will analyze it, generate a CSV file, and provide it for download.

Remember to adjust the paths and customize the HTML template and CSS styles as needed to fit your project requirements.

Please let me know if you have any further questions!
