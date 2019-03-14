import sys

images=[]
slideHorizontal=[]
slideVertical=[]
slideshow=[]
imagesVertical=[]
nlines=0
class SlideHorizontal:
    def __init__(self, img1):
        self.img1=img1
    def print(self):
        print(self.img1.id)
    def tags(self):
        return self.img1.tags

class SlideVertical(SlideHorizontal):
    def __init__(self, img1,img2):
        self.img1=img1
        self.img2=img2
    def print(self):
        print(self.img1.id,self.img2.id)
    def tags(self):
        return list(set().union(self.img1.tags,self.img2.tags))

class Image:
    def __init__(self,id,orientation,tags):
        self.id=id
        self.orientation=orientation
        self.tags=tags

def createVerticalSlides():
    i=0
    while i<len(imagesVertical):
        slideVertical.append(SlideVertical(imagesVertical[i],imagesVertical[i+1]))
        i+=2

def createSlides():
    for image in images:
        if image.orientation=='H':
            slideHorizontal.append(SlideHorizontal(image))
        else:
            imagesVertical.append(image)
    createVerticalSlides()
    for i in slideHorizontal:
        slideshow.append(i)
    for i in slideVertical:
        slideshow.append(i)

def input(file):
    fl=open(file)
    nlines=fl.readline()
    j=0
    for i in range(int(nlines)):
        line=fl.readline()
        elements=line.split()
        orientation=elements[0]
        ntags=int(elements[1])
        tags=elements[2:ntags+2]
        images.append(Image(j,orientation,tags))
        j+=1
    createSlides()
    fl.close()

def slidesScore(sh1, sh2):
    t1 = sh1.tags
    t2 = sh2.tags
    left=0
    both=0
    for tag1 in t1:
        if tag1 not in t2:
            left+=1
        else:
            both+=1
    right=(len(t1)+len(t2)-left-both)
    return min(left,both,right)


# best = imagen, cambiará cuando sea mejor la combinacion con respecto a las demás
# list = lista con la que haremos todas las permutaciones
# start = el inicio, será 0
# end = el final, será el número de elementos que haya
def permutation(list, start, end):
    if (start == end):
        return list
    else:
        for i in range(start, end + 1):
            list[start], list[i] = list[i], list[start]  # The swapping
            permutation(list, start + 1, end, best)
            list[start], list[i] = list[i], list[start]  # Backtracking

def scoreOfSlideshow(slideshow):
    ac=0
    for i in range(len(slideshow)-1):
        ac+=slidesScore(slideshow[i], slideshow[i+1])
    return ac

def bestSlideshow(permutations):
    best=0
    for i in permutations:
        current=slidesScore(i)
        if best<current:
            best=current
            slideshow=i

def bestScore(list):
    best=0
    ind=0
    for i in list:
        ac=0
        for i in range(len(list)-1):
            ac+=slidesScore(list[i], list[i+1])
        if ac:
            best = slidesScore(list[i], list[i+1])
            ind=i
    return best

def algorithm():
    perms=permutation(slideshow.copy(),0,nlines)

    return

def output():
    print(len(slideshow))
    for slide in slideshow:
        slide.print()


if __name__ == '__main__':
    for file in sys.argv[1:]:
        input(file)
        #algoritmo
        algorithm()
        #salida
        output()
