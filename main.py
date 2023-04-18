import cv2
from CameraThread import CameraThread
from EdgeDetectionThread import EdgeDetectionThread

def main():
    camera_thread = CameraThread()
    camera_thread.start()
    edge_detection_thread = EdgeDetectionThread(camera_thread)
    edge_detection_thread.start()

    while True:
        edges = edge_detection_thread.get_edges()

        if edges is not None:
            frame = camera_thread.get_frame()
            if frame is not None:
                edges_resized = cv2.resize(edges, (frame.shape[1], frame.shape[0]))
                frame_with_edges = cv2.addWeighted(frame, 0.5, edges_resized, 0.5, 0)
                cv2.imshow('Edges', frame_with_edges)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    edge_detection_thread.stop()
    edge_detection_thread.join()
    camera_thread.stop()
    camera_thread.join()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
