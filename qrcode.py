import cv2
from pyzbar.pyzbar import decode
import webbrowser

def leitor_qr_code():

    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        codes = decode(frame)

        for code in codes:
            (x, y, w, h) = code.rect
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            qr_code_text = code.data.decode('utf-8')
            cv2.putText(frame, qr_code_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            webbrowser.open(qr_code_text, new=2)

            print(f"Presença registrada para: {qr_code_text}")

        cv2.imshow('Leitor QR Code', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    leitor_qr_code()
