import cv2
from manager import WindowManager, CaptureManager
from object_detection import detect_objects

class start(object):

    def __init__(self):
        self._windowManager = WindowManager('Cameo',
                                            self.onKeypress)
        self._captureManager = CaptureManager(
            cv2.VideoCapture(0), self._windowManager, True)

    def run(self):
        """Run the main loop."""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame

            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self, keycode):
        """Handle a keypress.

        s -> Take a screenshot.
        q -> Quit.
        0 -> Detect objects.
        a -> To estimate age and gender.
        t -> To convert text from image to audio.

        """
        if keycode == ord('s'): # space
            self._captureManager.writeImage('screenshot.png')

        elif keycode == ord('q'): # escape
            self._windowManager.destroyWindow()

        elif keycode == ord('o'):
            temp = detect_objects()
            temp.run_object_detection(img=cv2.imread('screenshot.png'))

        elif keycode == ord('a'):
            import AgeAndGenderEstimation
            AgeAndGenderEstimation.run()

        elif keycode == ord('t'):
            import img2audio
            img2audio.run()


if __name__=="__main__":
    start().run()
