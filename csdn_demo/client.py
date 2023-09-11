from Dxr_grpc.dxr_grpc_client import Dxr_grpc_client
import cv2
 
# 初始化客户端，ip和端口号
dxr_client = Dxr_grpc_client('127.0.0.1', "50051")
 
cap = cv2.VideoCapture(0)
 
json_data = {
    'type': 'face',
}
 
while True:
    ret, frame = cap.read()
    if ret:
        # 调用get_response方法，获取处理后的图像
        res = dxr_client.get_response(frame, json_data)
        # res是一个生成器，可以通过for循环获取处理后的图像
        for i in res:
            frame = i['dst']
            cv2.imshow('frame', frame)
            k = cv2.waitKey(1)
            # 根据按键选择不同的处理方式
            if k == ord('q'):
                break
            elif k == ord('f'):
                json_data['type'] = 'face'
            elif k == ord('m'):
                json_data['type'] = 'object'
                
cap.release()
