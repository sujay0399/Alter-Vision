import cv2
from manager import WindowManager, CaptureManager
#from main import OB

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

        space  -> Take a screenshot.
        tab    -> Start/stop recording a screencast.
        escape -> Quit.

        """
        if keycode == 32: # space
            self._captureManager.writeImage('screenshot.png')

        elif keycode == 27: # escape
            self._windowManager.destroyWindow()

        #elif keycode == 111:
            #OB.run(cv2.imread('screenshot.png'))

        #elif keycode == 116:
            #tess.run()


if __name__=="__main__":
    start().run()
