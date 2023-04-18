import cv2
from CameraThread import CameraThread
from EdgeDetectionThread import EdgeDetectionThread

def main():
    # Tworzenie obiektu CameraThread
    camera_thread = CameraThread()
    camera_thread.start()

    # Tworzenie obiektu EdgeDetectionThread i przekazanie obiektu CameraThread do konstruktora
    edge_detection_thread = EdgeDetectionThread(camera_thread)
    edge_detection_thread.start()

    while True:
        # Pobieranie krawędzi z EdgeDetectionThread
        edges = edge_detection_thread.get_edges()

        if edges is not None:
            # Wyświetlanie krawędzi na tle takim, jakie widzi kamera
            frame = camera_thread.get_frame()
            if frame is not None:
                combined_frame = cv2.bitwise_and(frame, edges)
                cv2.imshow('Edges', combined_frame)

        # Wciśnięcie klawisza 'q' kończy pętlę
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Zatrzymywanie wątków
    edge_detection_thread.stop()
    edge_detection_thread.join()
    camera_thread.stop()
    camera_thread.join()

    # Zamykanie okien OpenCV
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
