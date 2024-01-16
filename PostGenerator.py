import requests
import cvzone
import cv2
from PIL import Image, ImageDraw,ImageFont,ImageEnhance,ImageFilter,ImageOps
from io import BytesIO

img2 = Image.open(r"opa1.png").convert("RGBA")
coma= cv2.imread("coma.png",cv2.IMREAD_UNCHANGED)
coma1= cv2.imread("coma1.png",cv2.IMREAD_UNCHANGED)
water= cv2.imread("watermark.png",cv2.IMREAD_UNCHANGED)
#this is sthe code for a random nature image from unsplash

def linkFetch():
    url = "https://api.unsplash.com/photos/random/?query=nature&page=1&per_page=30&client_id=gfS0YHIkA1HHrD4QlmupvA7K_BL-SYBKDWCxD8GEUqo"

    response = requests.get(url)
    data = response.json()["urls"]["raw"]
    return data

img_url=linkFetch()
response = requests.get(img_url)
img = Image.open(BytesIO(response.content))
size=(1000,1000)
#resize image
img1 = img.resize(size).convert("RGBA")
#black and white
img1= img1.convert('L')
#add a black texutre
img1.paste(img2, (0,0), mask = img2)


#save the image
img1.save("hello.png")
final= Image.open(r"hello.png").convert("RGBA")
#random quote
f = open("data.txt","r")

data=f.read()
data=int(data)
print(data)

f.close()




url = 'https://type.fit/api/quotes'


r = requests.get(url)
quote = r.json()


qtext = quote[data]['text']
qauthor=quote[data]['author']
authors = '- '


#justfy



class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        num_of_words = len(words)
        start_ind, end_ind, runner = 0, 0, 0
        len_of_line, word_num_line = 0, 0
        res = []

        while True:
            runner = start_ind
            if runner >= num_of_words:
                break
            len_of_line, word_num_line = 0, 0

            #find the start and end word indexes for one line
            while runner < num_of_words:
                len_of_line = len_of_line + len(words[runner])
                word_num_line = word_num_line + 1
                if runner != start_ind:
                    len_of_line = len_of_line + 1
                if len_of_line > maxWidth:
                    break
                runner = runner + 1

            #justify one line
            if runner != num_of_words:
                end_ind = runner - 1
                if start_ind == end_ind: #one word in a line
                    oneline = words[start_ind] + " "*(maxWidth-len(words[start_ind]))
                else: #many words in a line
                    len_of_line = len_of_line - len(words[runner]) - 1
                    word_num = end_ind - start_ind + 1
                    extra_spaces = maxWidth - (len_of_line - (word_num - 1))
                    basic_pad_spaces = extra_spaces // (word_num - 1)
                    addition_pad_spaces = extra_spaces % (word_num - 1)
                    oneline = ""
                    for ind in range(start_ind, runner-1):
                        oneline = oneline + words[ind] + " "*basic_pad_spaces
                        if ind - start_ind < addition_pad_spaces:
                            oneline = oneline + " "
                    oneline = oneline + words[runner-1]
            else: #last line
                oneline = ""
                for ind in range(start_ind, num_of_words-1):
                    oneline = oneline + words[ind] + " "
                oneline = oneline + words[num_of_words-1]
                pad_spaces = maxWidth - len(oneline)
                oneline = oneline + " "*pad_spaces

            res.append(oneline)        
            start_ind = runner

        return res

split_qtext= qtext.split(" ")
x = Solution.fullJustify(0,split_qtext,24)

#justfy author
#ath= qauthor.split(" ")
#ath= Solution.fullJustify(0,qauthor,23)


#print(ath)    


#end
font = ImageFont.truetype("he.otf",70)
font2 = ImageFont.truetype("arial.ttf",30)
draw = ImageDraw.Draw(final)

qauthor = str(qauthor)
adds = 300

for i in range(0,len(x)):
    draw.text((150,adds),x[i],font=font,fill='yellow')
    adds =adds+100
    

#draw.text((100,300),x[0],font=font,fill='yellow')
#draw.text((100,400),x[1],font=font,fill='yellow')

draw.text((555,700),qauthor,font=font2,fill='yellow')

draw.text((540,700),authors,font=font2,fill ='yellow')



final.save(f"D:\programing\python\post_genrator\post\{data}{x[0]}.png")

lastedit = cv2.imread(f"D:\programing\python\post_genrator\post\{data}{x[0]}.png")
imgresult = cvzone.overlayPNG(lastedit,coma,[50,50])


cv2.imwrite(f"D:\programing\python\post_genrator\post\{data}{x[0]}.png",imgresult)
lastedit1 = cv2.imread(f"D:\programing\python\post_genrator\post\{data}{x[0]}.png")
imageresult = cvzone.overlayPNG(lastedit1,coma,[700,815])

cv2.imwrite(f"D:\programing\python\post_genrator\post\{data}{x[0]}.png",imageresult)
lastedit1 = cv2.imread(f"D:\programing\python\post_genrator\post\{data}{x[0]}.png")
imageresult = cvzone.overlayPNG(lastedit1,water,[30,200])
cv2.imwrite(f"D:\programing\python\post_genrator\post\{data}{x[0]}.png",imageresult)
#data add
f = open("data.txt","w")
num = data + 1
f.write(str(num))
f.close()
