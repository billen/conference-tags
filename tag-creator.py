from PIL import Image, ImageFont, ImageDraw
import csv




def createTag(firstname, lastname, typeOfAttendee, profession):
	im = Image.open("Nametag Template (Final).jpg")
	draw = ImageDraw.Draw(im)
	
	if (len(firstname) < 11):
		# Firstname font and placement
		font = ImageFont.truetype("roboto/Roboto-Bold.ttf", 150)
		draw.text((20, 180), firstname.upper(), font=font, fill="black")

		# Lastname font and placement
		font = ImageFont.truetype("roboto/Roboto-Regular.ttf", 100)
		draw.text((20, 330), lastname.upper(), font=font, fill=(57,102,150,255))
	else:
		# Firstname font and placement
		font = ImageFont.truetype("roboto/Roboto-Bold.ttf", 100)
		draw.text((20, 180), firstname.upper(), font=font, fill="black")

		# Lastname font and placement
		font = ImageFont.truetype("roboto/Roboto-Regular.ttf", 100)
		draw.text((20, 300), lastname.upper(), font=font, fill=(57,102,150,255))
	
	# Type font and placement
	font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf", 30)
	draw.text((800, 500), typeOfAttendee, font=font, fill="white")

	# Profession font and placement
	font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf", 30)
	draw.text((20, 500), profession, font=font, fill="white")

	
	#Save the file 
	im.save ('./tags/'+firstname+"_"+lastname+".jpg" )


def main():
	#Read the .csv for all the information for each tag
	with open('taglist2.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			print(row['First Name'], row['Last Name'], row['Profession'], row['Title'])
			createTag(row['First Name'],row['Last Name'],row['Title'], row['Profession'])


#First Name,Last Name,Profession,Title
main()
