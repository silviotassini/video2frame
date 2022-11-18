import cv2
import sys

def show_video_metadata(metadata):
    print("Video Dimension: height: {} width: {}".format( metadata[0], metadata[1]))
    print("N. Frames", metadata[2])
    print("Frames per secconds", metadata[3])
    print("Video duration (sec):", metadata[2] / metadata[3])

def get_video_metadata(vidcap):
    height = vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width  = vidcap.get(cv2.CAP_PROP_FRAME_WIDTH) 
    framecount = vidcap.get(cv2.CAP_PROP_FRAME_COUNT ) 
    frames_per_sec = vidcap.get(cv2.CAP_PROP_FPS)
    return [height,width,framecount,frames_per_sec]

    # equally easy to get this info from images
    # cv2image = cv2.imread(imagefilename, flags=cv2.IMREAD_COLOR  )
    # height, width, channel  = cv2image.shape
    # print ("Image Dimension: height:{} width:{}".format( height, width))
    
def vid2frame(video_file):
    vidcap = cv2.VideoCapture(video_file)
    meta = get_video_metadata(vidcap)
    show_video_metadata(meta)
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite("frame%d.jpg" % count, image)
        success, image = vidcap.read()     
        if not success:
            print("Erro no frame", count)   
        count += 1


if __name__ == "__main__":
    args = sys.argv[1:]
    if args:
        vid2frame(args[0])
    else:
        print("Uso: python video2frame.py arquivo\n \
            arquivo - Nome do arquivo de vídeo com caminho completo")
