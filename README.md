# conference-tags
Create name tags with custom backgrounds. Used usually to create name tags for conferences / events.

## How to Run
* Copy the namesListTemplate.csv to namesList.csv and add your own names
* Add an image to background-images
* Change the Tag.py to include that image name within the main method
* Run Tag.py

Next steps: <br/>
1) Create a properties that might even take positions, to allow for that freedom. <br/>
2) Add attributes that allow for more information to be displayed and pulled from the csv files. <br/>
3) Add a fonts folder to allow for custom fonts. (Add that to the properties file) <br/>
<br>
Very rough, needs a lot of work to generalize for other use.


October 28th, 2017 <br />
  - Added a class, and allowed for csv and template input. <br/>
  - To allow it to work, you need to create the folder:  tags <br/>
  - Pass into the TagCreator the path for csv file with first and lastname
  and the path for the background image.
