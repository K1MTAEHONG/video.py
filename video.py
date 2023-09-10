import cv2

# 녹화할 비디오 파일의 이름과 코덱 설정
video_name = 'my_video.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 비디오 스트림 가져오기
cap = cv2.VideoCapture(0)

# 비디오 파일 생성
out = cv2.VideoWriter(video_name, fourcc, 20.0, (640, 480))

while True:
    # 비디오 프레임 읽어오기
    ret, frame = cap.read()

    # 프레임 읽기에 실패한 경우 종료
    if not ret:
        break

    # 프레임 출력하기
    cv2.imshow('frame', frame)

    # 비디오 파일에 프레임 쓰기
    out.write(frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 비디오 파일과 스트림 객체 해제
out.release()
cap.release()

# 모든 창 닫기
cv2.destroyAllWindows()
