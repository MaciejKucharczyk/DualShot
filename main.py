import cv2
from CameraThread import CameraThread
from EdgeDetectionThread import EdgeDetectionThread
from Ball import Ball
# from ColorChange import ColorChanger


def main():
    camera_thread = CameraThread()
    camera_thread.start()
    edge_detection_thread = EdgeDetectionThread(camera_thread)
    edge_detection_thread.start()

    speed = [1, 2]
    ball = Ball(100, 50, speed, 2)  # x_pos, y_pos, speed, radius -> ball parameters

    ball.start()
    while True:
        edges = edge_detection_thread.get_edges()

        if edges is not None:
            frame = camera_thread.get_frame()
            window_height, window_width = frame.shape[:2]  # set hight and width of the window
            ball.set_window_size(window_width, window_height)  # set hight and width of the window for a ball 

            edges_resized = cv2.resize(edges, (frame.shape[1], frame.shape[0]))
            frame_with_edges = cv2.addWeighted(frame, 0.5, edges_resized, 0.5, 0)
            cv2.imshow('Edges', frame_with_edges)
            
            ball.move()  # move the ball
            ball.detect_collision(edges)  # detect edge collision

            cv2.circle(frame, (ball.x_pos, ball.y_pos), ball.radius, (0, 255, 0), thickness=-1)
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    edge_detection_thread.stop()
    edge_detection_thread.join()
    camera_thread.stop()
    camera_thread.join()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()