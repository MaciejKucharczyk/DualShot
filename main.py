import cv2
from CameraThread import CameraThread
from EdgeDetectionThread import EdgeDetectionThread
from ball import Ball

def main():
    camera_thread = CameraThread()
    camera_thread.start()
    edge_detection_thread = EdgeDetectionThread(camera_thread)
    edge_detection_thread.start()

    speed = [1, 1]
    ball = Ball(50, 20, speed, 10)
    while True:
        edges = edge_detection_thread.get_edges()

        if edges is not None:
            frame = camera_thread.get_frame()
            window_height, window_width = frame.shape[:2]
            # Pobranie rozmiarów ramki
            # window_width = int(frame.get(cv2.CAP_PROP_FRAME_WIDTH))
            # window_height = int(frame.get(cv2.CAP_PROP_FRAME_HEIGHT))
            if frame is not None:
                edges_resized = cv2.resize(edges, (frame.shape[1], frame.shape[0]))
                frame_with_edges = cv2.addWeighted(frame, 0.5, edges_resized, 0.5, 0)
                cv2.imshow('Edges', frame_with_edges)
                # cv2.circle(frame, (frame.shape[1]//2, frame.shape[0]//2), 10, (0,255,0), thickness=-1)
                cv2.circle(frame, (ball.x_pos, ball.y_pos), ball.radius, (0,255,0), thickness=-1)
                # ball.move(speed)
                # ball.WindowDetection(window_height, window_width)
                ball.run(speed, window_width, window_height)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    edge_detection_thread.stop()
    edge_detection_thread.join()
    camera_thread.stop()
    camera_thread.join()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
