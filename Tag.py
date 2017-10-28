from PIL import Image, ImageFont, ImageDraw
import csv

class TagCreator:

    def __init__(self, backgroundImageUrl, csvFileUrl):
        self.csvFileUrl = csvFileUrl
        self.backgroundImageUrl = backgroundImageUrl
        # Currently don't support custom attributes, but do that later on.
        #self.attributes = attributes

    def createTags(self):
        with open(self.csvFileUrl) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
        		print(row['First Name'], row['Last Name'])
        		self.createTag(row['First Name'], row['Last Name'])


    def createTag(self, firstname, lastname):
    	im = Image.open(self.backgroundImageUrl)
    	draw = ImageDraw.Draw(im)

    	if (len(firstname) < 11):
    		# Firstname font and placement
    		font = ImageFont.truetype("fonts/Roboto-Bold.ttf", 150)
    		draw.text((20, 100), firstname.upper(), font=font, fill="black")

    		# Lastname font and placement
    		font = ImageFont.truetype("fonts/Roboto-Regular.ttf", 100)
    		draw.text((20, 225), lastname.upper(), font=font, fill=(57,102,150,255))
    	else:
    		# Firstname font and placement
    		font = ImageFont.truetype("fonts/Roboto-Bold.ttf", 100)
    		draw.text((20, 80), firstname.upper(), font=font, fill="black")

    		# Lastname font and placement
    		font = ImageFont.truetype("fonts/Roboto-Regular.ttf", 100)
    		draw.text((20, 200), lastname.upper(), font=font, fill=(57,102,150,255))

    	# Type font and placement
    	#font = ImageFont.truetype("fonts/NotoSans-Bold.ttf", 30)
    	#draw.text((800, 500), typeOfAttendee, font=font, fill="white")

    	# Profession font and placement
    	#font = ImageFont.truetype("fonts/NotoSans-Bold.ttf", 30)
    	#draw.text((20, 500), profession, font=font, fill="white")


    	#Save the file
    	im.save ('tags/' + firstname + "_" + lastname + ".jpg" )




def main():
    # Currently don't support attributes
    #attributes = ['FirstName', 'LastName'. 'Profession', 'Title']
    tagCreator = TagCreator('background-images/<name of template image>.jpg', 'names/nameList.csv')
    tagCreator.createTags()




main()
